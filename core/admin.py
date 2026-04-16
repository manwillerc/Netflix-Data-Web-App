from django.contrib import admin
from .models import Viewer, Account, Behavior

# Register your models here.
class ViewerAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "age", 
        "gender", 
        "country", 
        "primary_device"
    )
    search_fields = (
        "country", 
        "gender"
    )
    list_filter = (
        "gender", 
        "country"
    )

admin.site.register(Viewer, ViewerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "viewer",
        "account_age_months", 
        "subscription_type", 
        "monthly_fee", 
        "payment_method"
    )
    search_fields = (
        "subscription_type", 
        "payment_method"
    )
    list_filter = (
        "subscription_type", 
        "payment_method"
    )

admin.site.register(Account, AccountAdmin)

class BehaviorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "viewer",
        "favorite_genre",
        "avg_watch_time_mins",
        "watch_sessions_per_week",
        "completion_rate",
        "churned",
    )

    search_fields = (
        "favorite_genre",
        "viewer__country",
    )

    list_filter = (
        "favorite_genre",
        "churned",
        "watch_sessions_per_week",
    )