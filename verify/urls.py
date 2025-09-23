# verifier_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_view, name='upload_view'),
    path('result/', views.result_view, name='result_view'),
]