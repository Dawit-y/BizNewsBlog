from django.urls import path
from . import views

# app_name = 'post'

urlpatterns = [
    path('', views.home, name='home' ),
    # path('post/<int:pk>/', views.post_detail, name="post_detail")
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]