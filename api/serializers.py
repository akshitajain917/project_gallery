from rest_framework import serializers
from .models import Project, TechincalSkillset

class TechincalSkillsetSerializer(serializers.ModelSerializer):
    class Meta:
      model = TechincalSkillset
      fields = ("frontend","backend","databases","infrastructure")

class ProjectSerializer(serializers.ModelSerializer):
   technical_skillset = TechincalSkillsetSerializer()
   class Meta:
      model = Project
      fields = ('id','title','technologies','technical_skillset')

   def create(self, validated_data):
    skillset =  validated_data.pop('technical_skillset')
    data,_ = TechincalSkillset.objects.get_or_create(**skillset)
    obj = Project.objects.create(technical_skillset=data,**validated_data)
    return obj
  
