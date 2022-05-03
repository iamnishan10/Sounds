#from django.urls import re_path as url
from django.urls import include, path
from django.urls import re_path as url
 
urlpatterns = [ 
    #url('', include('users.urls')),
    url('', include('users.urls')),
]