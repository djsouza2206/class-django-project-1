from django.contrib import admin
from django.urls import path
from recipes.views import about, contact, index

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', index),
    path('about/', about),
    path('contact/', contact),
]