from django.db import models

class OPProject(models.Model):
    openproject_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OPUser(models.Model):
    openproject_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OPStatus(models.Model):
    openproject_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class WorkPackage(models.Model):
    openproject_id = models.IntegerField(unique=True)
    subject = models.CharField(max_length=255)
    project = models.ForeignKey(OPProject, on_delete=models.CASCADE)
    status = models.ForeignKey(OPStatus, null=True, on_delete=models.SET_NULL)
    assignee = models.ForeignKey(OPUser, null=True, on_delete=models.SET_NULL)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.subject
