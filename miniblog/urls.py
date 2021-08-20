from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('singup/',views.user_singup,name='singup'),
     path('add/',views.add_post,name='add'),
    path('update/<int:id>/',views.update_post,name='update'),
    path('delete/<int:id>/',views.delete_post,name='delete'),
    
    
    
]

