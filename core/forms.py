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