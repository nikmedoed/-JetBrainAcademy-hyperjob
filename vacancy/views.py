from django.views import View
from django.shortcuts import render
from vacancy.models import Vacancy

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/index.html', context={'content': Vacancy.objects.all()})