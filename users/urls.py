from django.urls import path
from users.views import show_user, showUserId,userName
urlpatterns =[
    path('show_user/', show_user),
    path('showUserId/<id>/', showUserId)
    path('userName/<string:name>/', userName)
]