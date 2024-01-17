from django.apps import AppConfig

class BackendConfig(AppConfig):
    name = 'Portfolio-Backend'
    verbose_name = "Investment Portfolio"

    def ready(self):
        # Import signals to connect them on startup
        from . import signals  
        signals.connect_signals()

        # Perform any other custom app setup
        setup_app()

def setup_app():
    """Custom app initialization."""
    from .models import Portfolio  
    Portfolio.objects.get_or_create(name='Default Portfolio')