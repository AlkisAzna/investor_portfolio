from rest_framework import serializers
from .models import UserProfile, Portfolio, Stock, ETF, Cryptocurrency, VirtualTrade, BlogPost, FAQ

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class ETFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETF
        fields = '__all__'

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'

class VirtualTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualTrade
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
