from django.urls import include, path

urlpatterns = [
    path('recipes/', include('recipes.urls')),
]
