from rest_framework import serializers
from students.models import Projects, Students, Skills
from django.contrib.auth.models import User


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ['url', 'id', 'project_name', 'description', 'photo', 'time_create', 'time_update', 'start_date',
                  'end_date']


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate(self, data):
        alphabet = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}
        if not (bool(alphabet.intersection(set(data['first_name'].lower())))):
            raise serializers.ValidationError("Введите имя на русском")
        elif not (bool(alphabet.intersection(set(data['last_name'].lower())))):
            raise serializers.ValidationError("Введите фамилию на русском")
        return data


    class Meta:
        model = Students
        fields = ['url', 'id', 'first_name', 'last_name', 'birth_date', 'email', 'phone', 'projects', 'skill', 'owner']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['skill_name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(many=True, view_name='students-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'students']
