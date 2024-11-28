from rest_framework.viewsets import ModelViewSet
from .serializers import (TeacherSerializer, DirectionSerializer, EducationDirectSerializer,
                          ActiveStudentSerializer, LeaderSerializer, NewSerializers, V2DirectionSerializer,
                          ApplicationSerializer)
from .models import Teacher, ActiveStudent, Leader, Direction, EducationDirect, Application, New


class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class DirectionView(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class EducationDirectView(ModelViewSet):
    queryset = EducationDirect.objects.all()
    serializer_class = EducationDirectSerializer


class ActiveStudentView(ModelViewSet):
    queryset = ActiveStudent.objects.all()
    serializer_class = ActiveStudentSerializer


class LeaderView(ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer


class NewView(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializers


class ApplicationView(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class V2DirectionView(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = V2DirectionSerializer
