from django.urls import path

from dracula import views

add_name = 'dracula'

urlpatterns = [
    path('dracula/sia/', views.show_sia, name='sia'),
    path('dracula/summer', views.show_summer, name='summer')
]