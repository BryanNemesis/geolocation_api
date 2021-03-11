from django.urls import path
from .views import store_view, detail_view, list_view
from rest_framework_simplejwt import views as jwt_views


app_name = 'api'

urlpatterns = [
    path('store/<str:ip>/', store_view, name='store-view'),
    path('detail/<str:ip>/', detail_view, name='detail-view'),
    path('list/', list_view, name='list-view'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
