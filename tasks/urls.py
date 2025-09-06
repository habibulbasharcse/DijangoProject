from django.urls import path
from tasks.views import show_task ,showTaskWithPara

urlpatterns =[
    path('show_task/', show_task),
    path('showTaskWithPara/<int:id>/', showTaskWithPara)
]