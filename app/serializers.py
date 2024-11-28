from rest_framework.serializers import ModelSerializer
from .models import New, Direction, Teacher, EducationDirect, Leader, ActiveStudent, Application


class NewSerializers(ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class EducationDirectSerializer(ModelSerializer):
    class Meta:
        model = EducationDirect
        fields = '__all__'


class LeaderSerializer(ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'


class ActiveStudentSerializer(ModelSerializer):
    class Meta:
        model = ActiveStudent
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class DirectionSerializer(ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class V2DirectionSerializer(ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Direction
        fields = ['pk', 'direction_name', 'direction_title', 'teachers']
