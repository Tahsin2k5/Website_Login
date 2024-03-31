from django.contrib import admin
from django.urls import path
from app_one.views import user_reg_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_register/', user_reg_view, name ='user_register')
]