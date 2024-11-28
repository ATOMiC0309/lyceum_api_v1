from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (NewView, LeaderView, TeacherView, ApplicationView, DirectionView, EducationDirectView,
                    V2DirectionView, ActiveStudentView)
routers = DefaultRouter()
routers.register('new', NewView, basename='new')
routers.register('leader', LeaderView, basename='leader')
routers.register('teacher', TeacherView, basename='teacher')
routers.register('application', ApplicationView, basename='application')
routers.register('direction', DirectionView, basename='direction')
routers.register('educationdirect', EducationDirectView, basename='educationdirect')
routers.register('activestudent', ActiveStudentView, basename='activestudent')
routers.register('v2direction', V2DirectionView, basename='v2direction')


urlpatterns = [
    path('', include(routers.urls))
]
