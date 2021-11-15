from snacks.views import (SnackPageView , SnackListDetail)
from django.urls import path


urlpatterns=[
    path ('' , SnackPageView.as_view() , name= 'home' ),
    path('<int:pk>/',SnackListDetail.as_view(),name = 'list_detail')
]