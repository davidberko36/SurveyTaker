from rest_framework import viewsets
from .models import User, RegularUser, Team, TeamLeader, Question, Answer, Survey
from .serializers import UserSerializer, RegularUserSerializer, TeamSerializer, TeamLeaderSerializer, QuestionSerializer, AnswerSerializer, SurveySerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
