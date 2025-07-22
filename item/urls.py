from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
