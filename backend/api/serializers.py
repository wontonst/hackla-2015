from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Mood, LANGUAGE_CHOICES, STYLE_CHOICES

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood

    def create(self, validated_data):
        """
        Create and return a new `Mood` instance, given the validated data.
        """
        return Mood.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Mood` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login')
