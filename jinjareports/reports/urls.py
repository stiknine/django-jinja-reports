from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dtl/', views.DTLIndexView.as_view(), name='dtl'),
]
