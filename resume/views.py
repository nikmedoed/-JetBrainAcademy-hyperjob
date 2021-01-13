from django.views import View
from django.shortcuts import render
from resume.models import Resume

class ResumesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/index.html', context={'content': Resume.objects.all()})