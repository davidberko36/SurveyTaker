from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 255, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(blank=True)


class Team(models.Model):
    name = models.CharField(max_length = 255, unique=True)


class TeamLeader(User):
    team_managed=models.ForeignKey(Team, on_delete = models.CASCADE)

class RegularUser(User):
    team=models.ForeignKey(Team, on_delete=models.CASCADE)



class Survey(models.Model):
    title = models.CharField(max_length=255)


class Question(models.Model):
    text = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_type=models.CharField(max_length=255)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
