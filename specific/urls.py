from specific.views import *
from django.urls import path
app_name = 'specific'
urlpatterns = [
    path('specific/',specific,name='specific'),
    path('mappingspe/',mappingspe,name='mappingspe'),
]