from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def my_view(request):
    return HttpResponse('new line')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', my_view),
]
