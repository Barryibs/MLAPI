from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsViews)
urlpatterns = [
    path('api/', include(router.urls)),
    path('status/', views.approvereject, name = 'appreject'),
    path('form/', views.cxcontact, name='cxform')
] 