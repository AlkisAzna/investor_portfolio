'''
Purpose of urls.py is to map URL patterns to specific views in the application.
This allows Django to direct requests to the appropriate view logic based on the requested URL.
'''

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import (UserViewSet, UserProfileViewSet, PortfolioViewSet, StockViewSet, 
                    ETFViewSet, CryptocurrencyViewSet, VirtualTradeViewSet, BlogPostViewSet, FAQViewSet)

# Create a router and register our viewsets with it
router = DefaultRouter()  
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'stocks', StockViewSet) 
router.register(r'etfs', ETFViewSet)
router.register(r'cryptocurrencies', CryptocurrencyViewSet)
router.register(r'trades', VirtualTradeViewSet)
router.register(r'posts', BlogPostViewSet)
router.register(r'faqs', FAQViewSet)

# API documentation
schema_view = get_schema_view(title='Investment Portfolio API')

urlpatterns = [
    # API documentation
    path('docs/', schema_view, name='api-docs'),
    
    # URLs for the router
    path('', include(router.urls)),

    # Users URLs
    path('users/', UserViewSet.as_view(), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view(), name='user-detail'),
    
    # Portfolio URLs
    path('portfolios/', PortfolioViewSet.as_view(), name='portfolio-list'),
    path('portfolios/<int:pk>/', PortfolioViewSet.as_view(), name='portfolio-detail'),
    
    # Stock URLs
    path('stocks/', StockViewSet.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockViewSet.as_view(), name='stock-detail'),
    
    # ETF URLs
    path('etfs/', ETFViewSet.as_view(), name='etf-list'),
    path('etf/<int:pk>/', ETFViewSet.as_view(), name='etf-detail'),
    
    # Crypto URLs
    path('cryptocurrencies/', CryptocurrencyViewSet.as_view(), name='crypto-list'),
    path('cryptocurrencies/<int:pk>/', CryptocurrencyViewSet.as_view(), name='crypto-detail'),

    # Trades URLs
    path('trades/', VirtualTradeViewSet.as_view(), name='trade-list'),
    path('trades/<int:pk>/', VirtualTradeViewSet.as_view(), name='trade-detail'),

    # BlogPost URLs
    path('posts/', BlogPostViewSet.as_view(), name='posts-list'),
    path('posts/<int:pk>/', BlogPostViewSet.as_view(), name='posts-detail'),

    # Include default auth urls for the browsable API
    path('api-auth/', include('rest_framework.urls')),
]
