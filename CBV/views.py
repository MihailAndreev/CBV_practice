from django.http import HttpResponse
from django.shortcuts import render
from django import views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from CBV_practice.CBV.models import WRC_Car, Car_category


class MyView(views.View):
    def get(self, request):
        my_list = [1, 2, 3, 4, 5]
        context = {
            'title': 'first_CBV',
            'text': 'some text',
            'text2': 'second text',
            'my_list': my_list
        }
        return render(request, 'index.html', context)
        # return HttpResponse('This is my CVB')


class MyTemplateView(TemplateView):
    template_name = 'template_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-based with TemplateView'
        context['main'] = 'main part'
        return context


class MyDetailsView(DetailView):
    model = WRC_Car
    template_name = 'rally_cars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rally cars'
        context['main'] = 'Rally cars info'
        return context


class MyListView(ListView):
    model = WRC_Car
    template_name = 'cars_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rally cars'
        context['main'] = 'Rally cars info'
        return context


class MyCreateView(CreateView):
    model = WRC_Car
    fields = '__all__'
    template_name = 'create_car.html'
    success_url = reverse_lazy('My list view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create rally car'
        return context

class MyUpdateView(UpdateView):
    model = WRC_Car
    fields = '__all__'
    template_name = 'update_car.html'
    success_url = reverse_lazy('My list view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update rally car'
        return context


class MyDeleteView(DeleteView):
    model = WRC_Car
    fields = '__all__'
    template_name = 'delete_car.html'
    success_url = reverse_lazy('My list view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete rally car'
        return context
