from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Portfolio, Stock, ETF, Cryptocurrency, VirtualTrade, BlogPost, FAQ

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for UserProfile model.
    """
    class Meta:
        model = UserProfile
        fields = ['user', 'surname', 'address', 'email', 'age', 'bio', 'origin', 'phone_number', 'profile_picture']

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model with nested UserProfile.
    """
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        # Update other fields as needed
        instance.save()

        profile.surname = profile_data.get('surname', profile.surname)
        # Update other profile fields as needed
        profile.save()

        return instance

class PortfolioSerializer(serializers.ModelSerializer):
    """
    Serializer for Portfolio model.
    """
    class Meta:
        model = Portfolio
        fields = ['user', 'name', 'description', 'created_at']

class StockSerializer(serializers.ModelSerializer):
    """
    Serializer for Stock model.
    """
    class Meta:
        model = Stock
        fields = ['portfolio', 'ticker_symbol', 'quantity', 'initial_purchase_price', 'current_price']

class ETFSerializer(serializers.ModelSerializer):
    """
    Serializer for ETF model.
    """
    class Meta:
        model = ETF
        fields = ['portfolio', 'ticker_symbol', 'quantity', 'initial_purchase_price', 'current_price']

class CryptocurrencySerializer(serializers.ModelSerializer):
    """
    Serializer for Cryptocurrency model.
    """
    class Meta:
        model = Cryptocurrency
        fields = ['portfolio', 'crypto_name', 'quantity', 'initial_purchase_price', 'current_price']

class VirtualTradeSerializer(serializers.ModelSerializer):
    """
    Serializer for VirtualTrade model.
    """
    user = serializers.ReadOnlyField(source='user.username')
    investment_detail = StockSerializer(source='investment', read_only=True)

    class Meta:
        model = VirtualTrade
        fields = ['user', 'investment', 'investment_detail', 'trade_type', 'trade_quantity', 'trade_price', 'trade_date']

class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for BlogPost model.
    """
    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content', 'created_at']

class FAQSerializer(serializers.ModelSerializer):
    """
    Serializer for FAQ model.
    """
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
