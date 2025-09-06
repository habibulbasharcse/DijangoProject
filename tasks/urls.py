from django.urls import path
from tasks.views import show_task ,showTaskWithPara ,txt

urlpatterns =[
    path('show_task/', show_task),
    path('showTaskWithPara/<int:id>/', showTaskWithPara),
    path('txt/<int:id>/', txt)
]