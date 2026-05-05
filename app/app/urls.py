from django.urls import path, include

urlpatterns = [
    path('produtos/', include('app.urls')),
]