
from .import views
from django.urls import path


urlpatterns = [
    path('', views.home,name= 'home'),
    path('about/', views.about,name= 'about'),
    path('contact/', views.contact,name= 'contact'),
    path('blogs/', views.blogs,name= 'blogs'),
    path('event_list/', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('<int:event_id>/cancel/', views.cancel_registration, name='cancel_registration'),
    path('my-registrations/', views.my_registrations, name='my_registrations'),
    path('event_form/', views.event_register_form,name='event_register_form'),
    # path('register/', views.register_event, name='register_event'),
    # path('event_list/', views.event_list,name= 'event'),
   
]