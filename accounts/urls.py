from django.urls import path
from accounts.views import login_view
# app_name = "accounts"

urlpatterns = [
    path('accounts/', login_view, name="login"),
]