from django.shortcuts import render
from django.views.generic import ListView
from .models import CarPost
from .utils import DataMixin


class Home(DataMixin, ListView):
    template_name = 'cars/index.html'
    model = CarPost

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_user_context(title='Home page')  # словарь для передачи данных с "миксина"
        return {**context, **title}

    def get_queryset(self):
        return CarPost.objects.filter(is_published=True)


def about(request):
    context = {
        'title': 'About us'
    }
    return render(request, 'cars/about.html', context=context)
