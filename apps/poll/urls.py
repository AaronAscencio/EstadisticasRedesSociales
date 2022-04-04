from unicodedata import name
from django.urls import path
from apps.poll.views import IndexView


app_name = 'index'

urlpatterns = [
    path('',IndexView.as_view(),name="index_view")
]