from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.core.exceptions import ValidationError

# Function to validate email uniqueness
def validate_email_uniqueness(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(f"Email {value} is already in use.")

class UserProfile(models.Model):
    """
    Extends the basic Django User model to include additional personal information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(validators=[EmailValidator(), validate_email_uniqueness])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])
    bio = models.TextField(max_length=500, null=True, blank=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    # Additional fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Investment Portfolio Model
class Portfolio(models.Model):
    """
    Represents an investment portfolio associated with a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_value(self):
        # Calculate total value of the portfolio
        return sum(investment.current_value() for investment in self.investment_set.all())

# Abstract Investment Model
class Investment(models.Model):
    """
    Abstract model representing a generic investment.
    """
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    initial_purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2) # Real-time updated
    purchase_date = models.DateTimeField()

    class Meta:
        abstract = True
    
    def current_value(self):
        """
        Calculates the current value of the investment.
        """
        return self.quantity * self.current_price

# Stock Investment Model
class Stock(Investment):
    """
    Represents a stock investment.
    """
    ticker_symbol = models.CharField(max_length=10)

# ETF Investment Model
class ETF(Investment):
    """
    Represents an ETF investment.
    """
    ticker_symbol = models.CharField(max_length=10)

# Cryptocurrency Investment Model
class Cryptocurrency(Investment):
    """
    Represents a crypto investment.
    """
    crypto_name = models.CharField(max_length=50)

# Virtual Trading
class VirtualTrade(models.Model):
    """
    Represents a virtual-mock trade made by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=4, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    trade_quantity = models.PositiveIntegerField()
    trade_price = models.DecimalField(max_digits=10, decimal_places=2)
    trade_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.trade_type} - {self.investment}"

    class Meta:
        ordering = ['-trade_date']


# Blog Post Model
class BlogPost(models.Model):
    """
    Represents a blog post created by a user.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Blog Posts"


# FAQ Model
class FAQ(models.Model):
    """
    Represents a Frequently Asked Question.
    """
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "FAQs"