from django.contrib import admin
from django.contrib.auth.models import User
from .models import Stock, ETF, Cryptocurrency

# Custom Admin for User to display additional information
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Unregister the original User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Admin for Stock
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker_symbol', 'quantity', 'initial_purchase_price', 'current_price')
    search_fields = ('ticker_symbol',)

# Admin for ETF
@admin.register(ETF)
class ETFAdmin(admin.ModelAdmin):
    list_display = ('ticker_symbol', 'quantity', 'initial_purchase_price', 'current_price')
    search_fields = ('ticker_symbol',)

# Admin for Cryptocurrency
@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('crypto_name', 'quantity', 'initial_purchase_price', 'current_price')
    search_fields = ('crypto_name',)
