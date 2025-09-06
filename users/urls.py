from django.urls import path
from users.views import show_user, showUserId
urlpatterns =[
    path('show_user/', show_user),
    path('showUserId/<id>/', showUserId)
]