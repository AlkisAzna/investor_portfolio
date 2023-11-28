from rest_framework import viewsets, generics, permissions
from .models import UserProfile, Portfolio, Stock, ETF, Cryptocurrency, VirtualTrade, BlogPost, FAQ
from .serializers import (UserProfileSerializer, PortfolioSerializer, StockSerializer, 
                          ETFSerializer, CryptocurrencySerializer, VirtualTradeSerializer, 
                          BlogPostSerializer, FAQSerializer)

# Using ViewSets
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

# Using APIView for custom behavior
class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

# Similar views can be created for ETF, Cryptocurrency, VirtualTrade, BlogPost, FAQ

# BlogPost example with APIView
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAdminUser]  # Assuming only admin can create posts

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAdminUser]

# FAQ example with ReadOnlyModelViewSet
class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]  # Read-only and available to all users
