#from django.conf.urls import url 
#from tutorials import views 
# 
#urlpatterns = [ 
#    url(r'^api/tutorials$', views.tutorial_list),
#    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
#    url(r'^api/tutorials/published$', views.tutorial_list_published)
#]

from django.urls import path
from tutorials import views

urlpatterns = [
    path('api/tutorials/', views.tutorial_list),
    path('api/tutorials/<int:pk>/', views.tutorial_detail),
    path('api/tutorials/published/', views.tutorial_list_published),
]
