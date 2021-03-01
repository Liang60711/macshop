from django.urls import path
from .views import (
    HomeView,
    SellView,
)

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sell/', SellView.as_view(), name='sell'),
]
