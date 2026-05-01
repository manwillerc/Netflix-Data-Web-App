from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Viewer, Account, Behavior
from django.views.generic import ListView, DetailView
from .forms import AccountForm, ViewerForm, BehaviorForm, PredictionForm
from .models import Viewer, Account, Behavior
from django.db import connection
import pandas as pd
import sklearn
import xgboost
import joblib
import json

# Create your views here.
def home(request):
    total_viewers = Viewer.objects.count()
    total_accounts = Account.objects.count()

    objects = {
        "total_viewers":total_viewers,
        "total_accounts":total_accounts
    }

    return render(request, 'core/home.html', objects)

def about(request):
    return render(request, 'core/about.html')

def analytics(request):
    return render(request, 'core/analytics.html')

def user_list(request):
    viewers = Viewer.objects.all()
    df = pd.DataFrame(list(viewers.values()))
    return render(request, "core/user_list.html", {"table_html":df.to_html(classes="table table-striped", index=False)})

def account_list(request):
    accounts = Account.objects.all()
    df = pd.DataFrame(list(accounts.values()))
    df_no_id = df.drop(columns='id')
    return render(request, "core/account_list.html", {"table_html":df_no_id.to_html(classes="table table-striped", index=False)})

def behavior_list(request):
    behaviors = Behavior.objects.all()
    df = pd.DataFrame(list(behaviors.values()))
    return render(request, "core/behavior_list.html", {"table_html":df.to_html(classes="table table-striped", index=False)})

class ViewerListView(ListView):
    model = Viewer
    template_name = 'core/viewer_list.html'
    context_object_name = "viewers"

class ViewerDetailView(DetailView):
    model = Viewer
    template_name = 'core/viewer_details.html'
    context_object_name = "viewer"

class AccountListView(ListView):
    model = Account
    template_name = 'core/account_list.html'
    context_object_name = "accounts"

class AccountDetailView(DetailView):
    model = Account
    template_name = 'core/account_details.html'
    context_object_name = "account"

class ViewerAccountDetailView(DetailView):
    model = Account
    template_name = 'core/viewer_account_details.html'
    context_object_name = "account"

    def get_object(self):
        return Account.objects.get(
            pk=self.kwargs["account_id"],
            viewer_id=self.kwargs["viewer_id"]
        )
    
class AccountViewerDetailView(DetailView):
    model = Viewer
    template_name = 'core/account_viewer_details.html'
    context_object_name = "viewer"

    def get_object(self):
        return Viewer.objects.get(
            pk=self.kwargs["viewer_id"],
            #account_id = self.kwargs["account_id"]
        )

class BehaviorDetailView(DetailView):
    model = Behavior
    template_name = 'core/behavior_details.html'
    context_object_name = "behavior"

def create_account(request):
    if request.method == "POST":
        account_form = AccountForm(request.POST)
        behavior_form = BehaviorForm(request.POST)
        if account_form.is_valid() and behavior_form.is_valid():
            account = account_form.save()
            behavior = behavior_form.save(commit=False)  # ← change this
            behavior.account = account  
            behavior.save()
            messages.success(request, "Account creates successfully")
            return redirect("account_details", pk=account.pk)
    else:
        account_form = AccountForm()
        behavior_form = BehaviorForm()

    return render(request, "core/account_form.html", {"account_form":account_form,"behavior_form":behavior_form, "account":None, "behavior":None})

def edit_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    behavior = get_object_or_404(Behavior, pk=pk)

    if request.method == "POST":
        account_form = AccountForm(request.POST, instance=account)
        behavior_form = BehaviorForm(request.POST, instance=behavior)

        if account_form.is_valid() and behavior_form.is_valid():
            account_form.save()
            behavior_form.save()
            return redirect("account_details", pk=account.pk)
    
    else:
        account_form = AccountForm(instance=account)
        behavior_form = BehaviorForm(instance=behavior)

    return render(request, "core/account_form.html", {"account_form":account_form,"behavior_form":behavior_form, "account":account, "behavior":behavior})

def delete_account(request, pk):
    account = get_object_or_404(Account, pk=pk)

    if request.method == "POST":
        account.delete()
        return redirect("account_list")
    
    return render(request, "core/account_confirm_delete.html", {"account":account})

def create_viewer(request):
    if request.method == "POST":
        viewer_form = ViewerForm(request.POST)
        if viewer_form.is_valid():
            viewer = viewer_form.save()
            messages.success(request, "Viewer created successfully")
            return redirect("viewer_details", pk=viewer.pk)
    else:
        viewer_form = ViewerForm()

    return render(request, "core/viewer_form.html", {"viewer_form":viewer_form, "viewer":None,})

def edit_viewer(request, pk):
    viewer = get_object_or_404(Viewer, pk=pk)

    if request.method == "POST":
        viewer_form = ViewerForm(request.POST, instance=viewer)

        if viewer_form.is_valid():
            viewer_form.save()
            return redirect("viewer_details", pk=viewer.pk)
    
    else:
        viewer_form = ViewerForm(instance=viewer)

    return render(request, "core/viewer_form.html", {"viewer_form":viewer_form, "viewer":viewer})

def delete_viewer(request, pk):
    viewer = get_object_or_404(Viewer, pk=pk)

    if request.method == "POST":
        viewer.delete()
        return redirect("viewer_list")
    
    return render(request, "core/viewer_confirm_delete.html", {"viewer":viewer})


def predict_churn(request):
    MODEL_PATH = "/Users/cadenmanwiller/Desktop/CIS4930/NetflixWebApp/core/models/churn_model.pkl"
    model = joblib.load(MODEL_PATH)

    churn_pred = None
    if request.method == "POST":
        prediction_form = PredictionForm(request.POST)

        if prediction_form.is_valid():
            data = prediction_form.cleaned_data
            df = pd.DataFrame([data])
            result = model.predict(df)[0]
            churn_pred = "Customer likely to churn" if (result==1) else "Customer unlikely to churn"
            
    else:
        prediction_form = PredictionForm()

    return render(request, "core/prediction_form.html", {"prediction_form":prediction_form, "churn_pred":churn_pred})

def dashboard(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT a.subscription_type, COUNT(*)
            FROM core_account a
            JOIN core_behavior b
            ON a.id = b.account_id
            WHERE b.churned = TRUE
            GROUP BY a.subscription_type;
        """)
        rows = cursor.fetchall()

    
        label = [row[0] for row in rows]
        values = [row[1] for row in rows]

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT a.age, AVG(c.watch_sessions_per_week)
            FROM core_viewer a
            JOIN core_account b
            ON a.id = b.viewer_id
            JOIN core_behavior c
            ON b.id = c.account_id
            GROUP BY a.age;
        """)
        rows = cursor.fetchall()

    
        age = [row[0] for row in rows]
        avg_watch_session = [row[1] for row in rows]

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT a.country, 
                    SUM(b.monthly_fee * b.account_age_months) AS total_profit
            FROM core_viewer a
            JOIN core_account b
            ON a.id = b.viewer_id
            GROUP BY a.country
            ORDER BY total_profit DESC;
        """)
        rows = cursor.fetchall()

    
        country = [row[0] for row in rows]
        total_revenue = [row[1] for row in rows]

    return render(request, "core/dashboard.html", {"label":label, "values":values, "age":age,"avg_watch_session":avg_watch_session, "country":country, "total_revenue":total_revenue})