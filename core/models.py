from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    country = models.CharField(
        max_length = 100,
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
    primary_device = models.CharField(
        max_length = 100,
        choices=[
            ("Mobile","Mobile"),
            ("Tablet","Tablet"),
            ("Laptop","Laptop"),
            ("Smart TV","Smart TV")
        ]
    )
    devices_used = models.IntegerField()

    

class Account(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    account_age_months = models.IntegerField()
    subscription_type = models.CharField(
        max_length = 100,
        choices=[
            ("Standard", "Standard"),
            ("Basic", "Basic"),
            ("Premium", "Premium")
        ]
    )
    monthly_fee = models.FloatField(
        choices=[
            (7.99, 7.99),
            (12.99, 12.99),
            (15.99, 15.99)
        ]
    )
    payment_method = models.CharField(
        max_length = 100,
        choices=[
            ("Paypal","Paypal"),
            ("UPI", "UPI"),
            ("Credit Card","Credit Card"),
            ("Debit Card", "Debit Card")
        ]
    )

class Behavior(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    favorite_genre = models.CharField(
        max_length =100,
        choices = [
            ("Action", "Action"),
            ("Comedy", "Comedy"),
            ("Drama", "Drama"),
            ("Horror", "Horror"), 
            ("Romance", "Romance"),
            ("Documentary", "Documentary"),
            ("Sci-Fi", "Sci-Fi"),
            ("Thriller","Thriller"),
        ]
    )
    avg_watch_time_mins = models.IntegerField()
    watch_sessions_per_week = models.IntegerField()
    binge_watch_sessions = models.IntegerField()
    completion_rate = models.IntegerField(
        validators= [
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    rating_given = models.FloatField(
        validators = [
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    content_interactions = models.IntegerField()
    recommendation_click_rate = models.IntegerField(
        validators= [
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    days_since_last_login = models.IntegerField()
    churned = models.BooleanField()

