import re
from rest_framework.views import APIView
from .models import Project
from rest_framework.response import Response
from .serializers import ProjectSerializer
from .constants import *

# Return list of projects
class ProjectDetailsView(APIView):
    def get(self,request):
        snippets = Project.objects.all()
        serializer = ProjectSerializer(snippets, many=True)
        return Response(serializer.data)
  
#Return list of filtered projects according to query
class FilteredDetailsView(APIView):
    def get(self,request):
        search_query = self.request.GET.get('search', '').split(" ")
        built_query = []

        # filtering query on basis of keywords present in db
        for word in search_query:
            word = re.sub('[\W_]+', '', word)
            word = word.lower()
            if word:
                if word in skillset:
                    built_query.append(word)
                elif word in technologies_used:
                    built_query.append(word)

        # return queryset according to skill present in db 
        if BACKEND in built_query:
            for tech in built_query:
                if tech in backend_skills:
                    queryset = Project.objects.filter(technical_skillset__backend__icontains=tech)
                    break

        elif FRONTEND in built_query:
            for tech in built_query:
                if tech in frontend_skills:
                    queryset = Project.objects.filter(technical_skillset__frontend__icontains=tech)
        
        elif DB or DATABASES in built_query:
            for tech in built_query:
                if tech in db_skills:
                    queryset = Project.objects.filter(technical_skillset__databases__icontains=tech)
        
        elif INFRASTRUCTURE in built_query:
            for tech in built_query:
                if tech in infra_skills:
                    queryset = Project.objects.filter(technical_skillset__infrastructure__icontains=tech)
        
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)



