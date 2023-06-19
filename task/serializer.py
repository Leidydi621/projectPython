from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'tile', 'description', 'done') para que me traiga todo lo que tengo le digo __all__
        fields = '__all__'


