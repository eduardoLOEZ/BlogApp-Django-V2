from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('register/', views.register),
    path('put/', views.putUser),
    path('image/', views.uploadImage),
    path('userProfile/', views.getUserProfile),
    path('<int:pk>/', views.getSoloUser),
    path('getUsers/', views.getUsers),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)