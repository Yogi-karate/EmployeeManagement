from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.employee_form,name='employee_insert'),#get and post request for insert operations
    path('<int:id>/', views.employee_form,name='employee_update'), #get and post request for update operations
    path('delete/<int:id>/', views.employee_delete,name='employee_delete'),
    path('list/', views.employee_list,name='employee_list'), # get request for retrieving
    path('position/',views.position_form,name='position_insert'),
    path('position/<int:id>/',views.position_form,name='position_update'),
    path('position/delete/<int:id>/',views.position_delete,name='position_delete'),
]