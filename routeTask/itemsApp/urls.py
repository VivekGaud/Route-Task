from django.conf.urls import url
from itemsApp import views


app_name = 'itemsApp'

urlpatterns = [
       url(r'^add_item/$',views.add_item,name='add_item'),
       url(r'^view_items/$',views.view_items,name='view_items'),
       url(r'^delete_items/(?P<item_name>[-\w]+)/$', views.delete_items, name='delete_items'),
]