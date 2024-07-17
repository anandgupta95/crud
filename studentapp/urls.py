from django.urls import path
from studentapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('deletestudent/<id>',views.deletestudent,name='deletestudent'),
    path('updatestudent/<id>',views.updatestudent,name='updatestudent'),
    path('updatecode/',views.updatecode,name='updatecode')


]