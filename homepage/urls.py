from django.urls import path
from . import views

app_name ="homepage"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('new_update/<int:pk>/', views.new_update, name="new_update"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('mylist/', views.mylist, name="mylist"),
    path('mylikes/', views.mylikes, name="mylikes"),
    path('mycomments/', views.mycomments, name="comments"),

    # like
    path('like_toggle/<int:pk>/', views.like_toggle, name="like_toggle"),

    #comments
    path('create_comment/<int:pk>/', views.create_comment, name="create_comment"),
    path('delete_comment/<int:pk>/', views.delete_comment, name="delete_comment"),

    path('delete_image/<int:pk>/', views.delete_image, name="delete_image"),

]