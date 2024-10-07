from django.urls import path
from .views import MenuItemView, category_detail

urlpatterns = [
    path('menu_items/', MenuItemView.as_view(), name='menu_items'),
    path('menu_items/<int:pk>/', MenuItemView.as_view(), name='menu_items_single'),
    path('category/<int:pk>/', category_detail, name='category-detail'),  # Ensure the name matches 'category-detail'
]
