from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    # path('task/', views.task, name='task'),
    path('login/' ,views.userlogin,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.userlogout,name="logout"),
    path('edit/', views.todoedit, name="edit"),
    path('addtodo/',views.addtodo,name="addtodo"),
    path('todocomplete/<int:pk>',views.todocomplete,name="todocomplete"),
    path('todoclose/<int:pk>',views.todoclose,name="todoclose"),
    path('deletetodo/<int:pk>',views.deletetodo,name="deletetodo"),
    path('edittodo/<int:pk>', views.edittodo, name="edittodo"),
    path('editprofile/<int:pk>', views.editprofile, name="editprofile"),
]