from django.db import models


class issue(models.Model):
    issueID = models.indexesField(max_length=30)
    userID = models.textField(max_length=30)
    location = models.CharField(max_length=30)
    problem = models.CharField(max_length=30)
    time = models.timeField(max_length=30)
    status = models.CharField(max_length=30)
