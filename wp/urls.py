from django.urls import path
from Web import views

urlpatterns = [
    path('categories/', views.get_categories_list),
]