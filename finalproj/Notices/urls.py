from django.urls import path
from . import views

urlpatterns = [
    
    path('all-drives/',views.drives, name ='all-drives'),
    path('drive/<str:pk>/',views.drive, name='drive'),
    path('create-drive/',views.createDrive,name='create-drive'),
    path('update-drive/<str:pk>/',views.updateDrive, name='update-drive'),
    path('delete-drive/<str:pk>/', views.delete_drive, name='delete-drive'),
    ]
