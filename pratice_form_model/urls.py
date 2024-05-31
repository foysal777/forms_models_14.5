
from django.contrib import admin
from django.urls import path,include
from form_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.form , name='form'),
   
    path('form_app/' ,include('form_app.urls')),
    path('model_app/' ,include('model_app.urls')),
]
