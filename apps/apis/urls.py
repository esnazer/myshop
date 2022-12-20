from django.urls import path
from apps.apis.views.users import userListAPIView, userCreateAPIView, userDetailAPIView
from apps.apis.views.users import userLocationAPIView, userLocationDetailAPIView
from apps.apis.views.users import userDateListAPIView, userDateDetailAPIView
from apps.apis.views.shop import categoryListAPIView, categoryDetailAPIView
from apps.apis.views.shop import productListAPIView, productDetailAPIView
from apps.apis.views.shop import storeListAPIView, storeDetailAPIView
from apps.apis.views.shop import stockListAPIView, stockDetailAPIView

urlpatterns = [
   path('users/', userListAPIView.as_view(), name='list_user_api'),
   path('users/create/', userCreateAPIView.as_view(), name='create_user_api'),
   path('users/<int:pk>/', userDetailAPIView.as_view(), name='detail_user_api'),
   path('users/locations/', userLocationAPIView.as_view(), name='list_locations_api'),
   path('users/locations/<int:pk>/', userLocationDetailAPIView.as_view(), name='detail_locations_api'),
   path('users/date/', userDateListAPIView.as_view(), name='list_userdate_api'),
   path('users/date/<int:pk>/', userDateDetailAPIView.as_view(), name='detail_userdate_api'),
   path('categories/', categoryListAPIView.as_view(), name='list_categories_api'),
   path('categories/<int:pk>/', categoryDetailAPIView.as_view(), name='detail_categories_api'),
   path('products/', productListAPIView.as_view(), name='list_products_api'),
   path('products/<int:pk>/', productDetailAPIView.as_view(), name='detail_products_api'),
   path('stores/', storeListAPIView.as_view(), name='list_stores_api'),
   path('stores/<int:pk>/', storeDetailAPIView.as_view(), name='detail_stores_api'),
   path('stocks/', stockListAPIView.as_view(), name='list_stocks_api'),
   path('stocks/<int:pk>/', stockDetailAPIView.as_view(), name='detail_stocks_api'),
]