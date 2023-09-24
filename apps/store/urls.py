from django.urls import path

from . import api_endpoints as views

app_name = 'store'

urlpatterns = [
    path('brand/list/', views.BrandListAPIView.as_view(), name='brand_list'),
    path('category/list/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('collection/list/', views.CollectionListAPIView.as_view(), name='collection_list'),
    path('product/list/', views.ProductListAPIView.as_view(), name='product_list'),
    path('product/retrieve/<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('review/create/', views.ReviewCreateAPIView.as_view(), name='review_create')
]
