from django.urls import path
from recipes.views import about, contact_us, home

urlpatterns = [
    path('', home),
    path('contact-us', contact_us),
    path('about', about)
]
