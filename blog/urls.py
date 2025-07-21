from django.urls import path
from . import views



urlpatterns=[
   path('login/',views.log_in,name='login'),
    path('',views.my_view,name='mine'),
   path('signup',views.signup,name='signup'),
   path('record1/',views.record1,name='record1'),
   path('adds/',views.adds,name='adds'),
   path('some_path/<person>/',views.sadik,name='sadik'),
   path('deleting/<names>/',views.deletion,name='goge'),
   path('log_out',views.log_out,name='log_out')
]