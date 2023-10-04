import folium
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, CreateView, DetailView
from .models import CarPost, Search, Car
from .utils import DataMixin
from .forms import ContactForm, CarPostForm


class AddCarView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CarPostForm
    template_name = 'cars/add_car.html'
    login_url = reverse_lazy('home')  # redirect if user is not authorized
    raise_exception = True  # access is forbidden
    success_url = reverse_lazy('/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add Car")
        return {**context, **c_def}


class HomeView(DataMixin, ListView):
    template_name = 'cars/index.html'
    model = CarPost

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        title = self.get_user_context(title="Home page")

        return {**context, **title}


class CarDetails(DataMixin, DetailView):
    model = CarPost
    template_name = 'cars/car_detail.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'car'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_user_context(title='Car details')

        return {**context, **title}


def about(request):
    context = {
        'title': 'About us'
    }
    return render(request, 'cars/about.html', context=context)


class ContactFormView(DataMixin, FormView, View):
    template_name = 'cars/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('cars:home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.get_user_context(title='Contact')
        return {**context, **title}

    def form_valid(self, form):
        return redirect('cars:home')


class MapView(ListView):
    template_name = 'cars/map.html'
    model = Search

    def get_context_data(self, *, object_list=None, **kwargs):
        title = 'Map'
        form = folium.Figure(height=1000, width=1100)
        m = folium.Map(location=[-0.43, 0.32], tiles="openstreetmap", zoom_start=2.2, min_zoom=2,
                       max_bounds=True).add_to(form)
        for branch in self.model.objects.filter(active=True):
            folium.Marker([branch.lng, branch.lat], tooltip='Click for more', popup="Branch").add_to(m)

        # Get HTML Representation of Map Object
        map_html = m._repr_html_()

        context = {
            'title': title,  # Corrected title assignment
            'map': map_html
        }
        return context

    def get_queryset(self):
        pass
