from django.urls import path, include
from .views import *


urlpatterns = [
    path('chat/', ChatGPTView.as_view(), name='chat')

]