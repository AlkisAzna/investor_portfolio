from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(validators=[EmailValidator()])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])
    bio = models.TextField(max_length=500, blank=True)
    origin = models.CharField(max_length=100)
    # Additional fields
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Investment Portfolio Model
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_value(self):
        # Calculate total value of the portfolio
        pass

# Abstract Investment Model
class Investment(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    initial_purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2) # Real-time updated
    purchase_date = models.DateTimeField()

    class Meta:
        abstract = True

# Stock Investment Model
class Stock(Investment):
    ticker_symbol = models.CharField(max_length=10)

# ETF Investment Model
class ETF(Investment):
    ticker_symbol = models.CharField(max_length=10)

# Cryptocurrency Investment Model
class Cryptocurrency(Investment):
    crypto_name = models.CharField(max_length=50)

# Virtual Trading (Optional)
class VirtualTrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=4, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    trade_quantity = models.PositiveIntegerField()
    trade_price = models.DecimalField(max_digits=10, decimal_places=2)
    trade_date = models.DateTimeField(auto_now_add=True)

# Blog Post Model
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()