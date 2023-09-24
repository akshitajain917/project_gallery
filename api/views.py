from django.shortcuts import render
from rest_framework.views import APIView
from .models import Project,TechincalSkillset
from rest_framework.response import Response
from .serializers import ProjectSerializer,TechincalSkillsetSerializer


class ProjectDetailsView(APIView):
    def get(self,request):
        snippets = Project.objects.all()
        serializer = ProjectSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

