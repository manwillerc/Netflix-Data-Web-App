from django import forms
from .models import Viewer, Behavior, Account

class ViewerForm(forms.ModelForm):
    class Meta:
        model = Viewer
        fields = [
            "age",
            "gender",
            "country",
            "primary_device",
            "devices_used"
        ]

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "viewer",
            "account_age_months", 
            "subscription_type",
            "monthly_fee",
            "payment_method"
        ]

class BehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = [
            "favorite_genre",
            "avg_watch_time_mins",
            "watch_sessions_per_week",
            "binge_watch_sessions",
            "completion_rate",
            "rating_given",
            "content_interactions",
            "recommendation_click_rate",
            "days_since_last_login",
            "churned",
        ]

class PredictionForm(forms.Form):
    age = forms.IntegerField()
    gender = forms.ChoiceField(
        choices = [
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other")
        ]
    )
    country = forms.ChoiceField(
        choices=[
            ("India", "India"),
            ("USA", "USA"),
            ("Canada", "Canada"),
            ("Brazil", "Brazil"),
            ("France", "France"),
            ("Australia", "Australia"),
            ("UK", "UK"),
            ("Japan", "Japan"),
            ("Germany", "Germany"),
        ]
    )
    primary_device = forms.ChoiceField(
        choices=[
            ("Mobile","Mobile"),
            ("Tablet","Tablet"),
            ("Laptop","Laptop"),
            ("Smart TV","Smart TV")
        ]
    )
    devices_used = forms.IntegerField()
    account_age_months = forms.IntegerField()
    subscription_type = forms.ChoiceField(
        choices=[
            ("Standard", "Standard"),
            ("Basic", "Basic"),
            ("Premium", "Premium")
        ]
    )
    monthly_fee = forms.ChoiceField(
        choices=[
            (7.99, 7.99),
            (12.99, 12.99),
            (15.99, 15.99)
        ]
    )
    payment_method = forms.ChoiceField(
        choices=[
            ("Paypal","Paypal"),
            ("UPI", "UPI"),
            ("Credit Card","Credit Card"),
            ("Debit Card", "Debit Card")
        ]
    )