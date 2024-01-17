'''
The views.py file contains the view logic that controls the request and response flow for the web application. 
It acts as the bridge between the models and the serializers to the frontend.
'''

from rest_framework import viewsets, generics, permissions, filters, pagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import status

from .models import UserProfile, Portfolio, Stock, ETF, Cryptocurrency, VirtualTrade, BlogPost, FAQ
from .serializers import (UserSerializer, UserProfileSerializer, PortfolioSerializer, StockSerializer, 
                          ETFSerializer, CryptocurrencySerializer, VirtualTradeSerializer, 
                          BlogPostSerializer, FAQSerializer)


'''
Configure custom pagination classes to paginate response data.
- StandardPagination is good for most endpoints.
- LargeResultsSetPagination can be used for endpoints expecting large datasets.
'''
class StandardPagination(pagination.PageNumberPagination):
    page_size = 100
    page_query_param = 'page_size'
    max_page_size = 1000

class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 1000
    page_query_param = 'page_size'
    max_page_size = 10000
    
'''
VIEWSETS
- Viewsets provide the standard CRUD operations for models.
'''

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # Queryset filters and orders Users 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

     # Can override default viewset methods for custom logic
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        # Paginate list view
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = self.get_object() 
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    # Customizing the create behavior
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()

    # Customizing the update behavior
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
        
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UserProfiles to be viewed or edited.
    """
    queryset = UserProfile.objects.all().order_by('user')
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardPagination

class PortfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Portfolios to be viewed or edited.
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

class StockViewSet(viewsets.ModelViewSet): 
    """
    API endpoint that allows Stocks to be viewed or edited.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['portfolio', 'ticker_symbol']
    pagination_class = StandardPagination

class CryptocurrencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cryptocurrencies to be viewed or edited.
    """
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [permissions.IsAuthenticated]

class ETFViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ETFs to be viewed or edited.
    """
    queryset = ETF.objects.all() 
    serializer_class = ETFSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BlogPostViewSet(viewsets.ModelViewSet):  
    """
    API endpoint that allows blog posts to be viewed or edited.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAdminUser]

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows FAQs to be viewed.
    """
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]
    
class VirtualTradeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows virtual trades to be viewed or edited
    """
    queryset = VirtualTrade.objects.all()
    serializer_class = VirtualTradeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LargeResultsSetPagination