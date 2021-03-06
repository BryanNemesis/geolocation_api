from django.urls import path
from .views import store_view, detail_view, list_view, delete_view
from rest_framework_simplejwt import views as jwt_views


app_name = 'api'

urlpatterns = [
    path('store/<str:ip>/', store_view, name='store-view'),
    path('detail/<str:ip>/', detail_view, name='detail-view'),
    path('delete/<str:ip>/', delete_view, name='delete-view'),
    path('list/', list_view, name='list-view'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
