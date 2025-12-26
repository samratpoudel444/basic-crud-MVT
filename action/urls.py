from . import views
from django.urls import path

urlpatterns = [
   path('createuser/', views.createUser, name="createuser"),
   path('users/', views.showUsers, name="userlist"),
   path('deleteUser/<int:id>/', views.deleteUser, name="deleteUser"),
   path('updateUser/<int:id>/', views.updateUser, name="updateUser")
]
