from django.db import models

# Create your models here.
class Viewer(models.Model):
    age = models.IntegerField()
    gender = models.CharField(
        max_length = 100,
        choices = [
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other")
        ]
    )
    country = models.CharField(max_length = 100)
    primary_device = models.CharField(max_length = 100)
    devices_used = models.IntegerField()

class Account(models.Model):
    viewer = models.OneToOneField(Viewer, on_delete=models.CASCADE)
    account_age_months = models.IntegerField()
    subscription_type = models.CharField(
        max_length = 100,
        choices=[
            ("Standard", "Standard"),
            ("Basic", "Basic"),
            ("Premium", "Premium")
        ]
    )
    monthly_fee = models.FloatField()
    payment_method = models.CharField(max_length = 100)

class Behavior(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length =100)
    avg_watch_time_mins = models.IntegerField()
    watch_sessions_per_week = models.IntegerField()
    binge_watch_sessions = models.IntegerField()
    completion_rate = models.IntegerField()
    rating_given = models.FloatField()
    content_interactions = models.IntegerField()
    recommendation_click_rate = models.IntegerField()
    days_since_last_login = models.IntegerField()
    churned = models.BooleanField(default=False)

