
from django.urls import path
from . import views


urlpatterns = [
    path('all-books', views.BooksList.as_view(), name='All-books'),
    path('all-authers', views.AutherList.as_view(), name='All-authers'),
]


