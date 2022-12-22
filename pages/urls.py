from django.urls import path
from .views import HomePageView, SignPageView, LoginPageView

urlpatterns = [
    path('sign/', SignPageView.as_view(), name='sign'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('', HomePageView.as_view(), name='home'),
]
