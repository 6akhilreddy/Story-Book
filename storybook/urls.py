from django.urls import path
from. import views
urlpatterns = [
    path('', views.index,name='index'),
    path('readstory/<read_id>',views.readstory,name='readstory'),
    path('addstory/',views.addstory,name='addstory')
]
