from django.urls import path
from .views import *



urlpatterns = [
    path('',index_view,name="index"),
    path('service/<slug>/',service_detail,name="service_detail"),
    path('portfolio',portfolio,name="portfolio"),
    path('portfolio_details/<slug>/',portfolio_details,name="portfolio_details"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
]
