from django.shortcuts import render

# Create your views here.


from django.views import View
from django.shortcuts import render

links = {
    'login': "/login",
    'sign up': "/signup",
    'vacancies': "/vacancies",
    'resumes': "/resumes",
    'personal profile': "/home",
    'logout': "/logout"
}

class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/index.html', context={'menu': links})
#
#
# from django.views.generic.base import TemplateView
#
#
# class ChapterView(TemplateView):
#     template_name = 'book/chapter.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         n_chapter = kwargs['n_chapter']
#         context['n_chapter'] = n_chapter
#         context['content'] = book['Chapter ' + n_chapter]
#         return context