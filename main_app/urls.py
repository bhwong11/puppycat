from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'vacations', views.VacationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vacations/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('vacation/', views.Vacactions.as_view(), name="vacation"),
]