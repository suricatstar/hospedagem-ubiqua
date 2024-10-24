from django.urls import path

from .views import IndexView, LoginClienteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginClienteView.as_view(), name='login'),
]
