from django.conf.urls import url 
from users import views 
 
urlpatterns = [ 
    url(r'^api/login$', views.login),
    url(r'^api/users$', views.user_list),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]