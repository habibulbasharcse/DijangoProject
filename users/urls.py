from django.urls import path
from users.views import show_user
urlpatterns =[
    path('show_user/', show_user)
]