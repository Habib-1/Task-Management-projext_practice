from django.urls import path
from .import views
urlpatterns = [
        path('all_task/',views.showTask, name='all_task'),
        path('add_task/',views.add_task,name="add_task"),
        path('edit_task/<int:pk>/',views.edit_task, name='edit_task'),
        path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    
]