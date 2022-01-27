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
    path('vacationsList/', views.getVacations, name="getVacations"),
    path('vacationsDetail/<str:pk>', views.vacationsDetail, name="vacationsDetail"),
    path('vacationsCreate/', views.createVacations, name="createVacations"),
    path('vacationsUpdate/<str:pk>', views.updateVacations, name="updateVacations"),
    path('vacationsDelete/<str:pk>', views.deleteVacations, name="deleteVacations"),
    path('activitiesList/', views.getActivities, name="getActivities"),
    path('activitiesDetail/<str:pk>',
         views.activitiesDetail, name="activitiesDetail"),
    path('activitiesCreate/', views.createActivities, name="createActivities"),
    path('activitiesUpdate/<str:pk>',
         views.updateActivities, name="updateActivities"),
    path('activitiesDelete/<str:pk>',
         views.deleteActivities, name="deleteActivities"),
]
