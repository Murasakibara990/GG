from rest_framework import serializers
from .models import About, Comment, Team, Userr, ScoialMedia, Books, Category, Profile


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['message', 'created_at', 'updated_at']


class UserrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userr
        fields = '__all__'
        read_only_fields = ['email', 'phone']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoialMedia
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
