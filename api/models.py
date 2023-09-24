from django.db import models

# Create your models here.

class TechincalSkillset(models.Model):
    frontend = models.CharField(max_length=500,null=True,blank=True)
    backend = models.CharField(max_length=500,null=True,blank=True)
    databases = models.CharField(max_length=500,null=True,blank=True)
    infrastructure = models.CharField(max_length=500,null=True,blank=True)


class Project(models.Model):
    title  = models.CharField(max_length=100)
    technologies = models.CharField(max_length=500)
    technical_skillset = models.ForeignKey(TechincalSkillset, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title