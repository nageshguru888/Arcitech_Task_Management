from django.urls import path
from .views import index, task_list, task_create, task_detail
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', index, name='task-create'),  
    path('task_list/', task_list, name='task-list'),  
    path('api/tasks/', task_create, name='task-create-api'), 
    path('api/tasks/<int:pk>/', task_detail, name='task-detail-api'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
