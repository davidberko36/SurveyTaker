from rest_framework import serializers
from .models import User, RegularUser, Team, TeamLeader, Question, Answer, Survey


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'


class RegularUserSerializer(serializers.ModelSerializer):
    model = RegularUser
    fields = '__all__'



class TeamSerializer(serializers.ModelSerializer):
    model = Team
    fields = '__all__'


class TeamLeaderSerializer(serializers.ModelSerializer):
    model = TeamLeader
    fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    model = Question
    fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
     model = Answer
     fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    model = Survey
    fields = '__all__'