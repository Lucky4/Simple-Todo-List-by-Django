# -*- coding:utf-8 -*-

from rest_framework import serializers

from .models import Todo


class AddTaskSerializer(serializers.Serializer):
    todo = serializers.CharField(max_length=64)
    priority = serializers.ChoiceField(
        choices=[(0, u'common'), (1, u'middle'), (2, u'prior'),],
	style={'base_template': 'radio.html'}
    )
    expire_time = serializers.DateTimeField()


class EditTaskSerializer(serializers.Serializer):
    todo = serializers.CharField(max_length=64)
    priority = serializers.ChoiceField(
        choices=[(0, u'common'), (1, u'middle'), (2, u'prior'),],
	style={'base_template': 'radio.html'}
    )
    expire_time = serializers.CharField()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'todo', 'flag', 'priority', 'create_time', 'expire_time')
