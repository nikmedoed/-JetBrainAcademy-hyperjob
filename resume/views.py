from django.views import View
from django.shortcuts import render, redirect
from resume.models import Resume

class ResumesView(View):

    def post(self, request, *args, **kwargs):
            resume = Resume.objects.create(
                description=request.POST.get("description"),
                author_id=request.user.id
            )
            return redirect("/home")

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'resume/index.html',
            context={'content': Resume.objects.all()}
        )