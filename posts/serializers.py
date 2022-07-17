from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['userId', 'title', 'body']


class PostPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']
        extra_kwargs = {'title': {'required': False}, 'body': {'required': False}}


class PostPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']
