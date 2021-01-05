
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from send_email_app import views


router = routers.DefaultRouter()
router.register('register',views.RegisterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
