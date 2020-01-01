from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ApprovalAPI', views.ApprovalsView)

urlpatterns = [
    path('form/', views.userform, name = 'userform'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject, name = 'userform')
]
