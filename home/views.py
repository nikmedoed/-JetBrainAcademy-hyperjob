
# Create your views here.
from django.views import View
from django.shortcuts import render
from vacancy.models import Vacancy


from django import forms


class HomeForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)

class HomePage(View):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:

        return render(
            request,
            'home/index.html',
            context={
                'dest': "/vacancy/new" if request.user.is_staff else "/resume/new",
                'form': HomeForm()
            }
        )

