
import re
from rest_framework.views import APIView
from .models import Project
from rest_framework.response import Response

from .serializers import ProjectSerializer
from django.db.models import Q
from .constants import *

class ProjectDetailsView(APIView):
    def get(self,request):
        snippets = Project.objects.all()
        serializer = ProjectSerializer(snippets, many=True)
        return Response(serializer.data)
  
class FilteredDetailsView(APIView):
    def get(self,request):
        search_query = self.request.GET.get('search', '').split(" ")
        built_query = []
        for word in search_query:
            word = re.sub('[\W_]+', '', word)
            word = word.lower()
            if word:
                if word in skillset:
                    built_query.append(word)
                elif word in technologies_used:
                    built_query.append(word)


        if "backend" in built_query:
            for tech in built_query:
                if tech in backend_skills:
                    queryset = Project.objects.filter(technical_skillset__backend__icontains=tech)
                    break

        elif "frontend" in built_query:
            for tech in built_query:
                if tech in frontend_skills:
                    queryset = Project.objects.filter(technical_skillset__frontend__icontains=tech)
        
        elif "database" or "databases" in built_query:
            for tech in built_query:
                if tech in db_skills:
                    queryset = Project.objects.filter(technical_skillset__databases__icontains=tech)
        
        elif "infra" or "infrastructure" in built_query:
            for tech in built_query:
                if tech in infra_skills:
                    queryset = Project.objects.filter(technical_skillset__infrastructure__icontains=tech)
        
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)



