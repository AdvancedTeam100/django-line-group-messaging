from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_member, name='create-member'),
    path('search/', views.retrieve_member, name='retrieve-member'),
    path('update/<int:pk>', views.update_member, name='update-member'),
    path('delete/<int:pk>', views.delete_member, name='delete-member'),
]