from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'apply', views.ApplyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.SendMessageView.as_view(), name='send_message'),

]




