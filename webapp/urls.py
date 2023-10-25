from django.contrib import admin
from django.urls import path
from webapp import views
from.models import Car
app_name='webapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('car/<int:car_id>/',views.cardetails,name='details'),
    path('add/', views.addcar,name='add'),
    # path('update/<int:car_id/',views.update,name='update')
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
