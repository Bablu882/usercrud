from django.urls import path
from.views import *


urlpatterns=[
    path('addshow',addshow,name='addshow'),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:id>/',update,name='update'),
    path('api',api_ext,name='api')

]