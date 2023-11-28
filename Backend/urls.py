from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserProfileViewSet, PortfolioViewSet, StockListCreateView, 
                    StockDetailView, BlogPostListCreateView, BlogPostDetailView, 
                    FAQViewSet)

# Creating a router and registering our viewsets
router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
    # URLs for the router
    path('', include(router.urls)),

    # Stock URLs
    path('stocks/', StockListCreateView.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),

    # BlogPost URLs
    path('blogposts/', BlogPostListCreateView.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),

    # Additional URLs for other models like ETF, Cryptocurrency, VirtualTrade can be added here

    # Include default auth urls for the browsable API
    path('api-auth/', include('rest_framework.urls')),
]
