from rest_framework import viewsets
from .models import User, RegularUser, Team, TeamLeader, Question, Answer, Survey
from .serializers import UserSerializer, RegularUserSerializer, TeamSerializer, TeamLeaderSerializer, QuestionSerializer, AnswerSerializer, SurveySerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegularUserViewset(viewsets.ModelViewSet):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer


class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamLeaderViewset(viewsets.ModelViewSet):
    queryset = TeamLeader.objects.all()
    serializer_class = TeamLeaderSerializer


class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewset(viewsets.ModelViewset):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class SurveyViewset(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer