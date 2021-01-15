from django.views import View
from django.shortcuts import render, redirect
from vacancy.models import Vacancy
from django.core.exceptions import PermissionDenied

class VacanciesView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            resume = Vacancy.objects.create(
                description=request.POST.get("description"),
                author_id=request.user.id
            )
            return redirect("/home")
        else:
            raise PermissionDenied

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'vacancy/index.html',
            context={'content': Vacancy.objects.all()}
        )