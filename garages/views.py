from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.

class IndexView(ListView):
    template_name = 'garages/index.html'
    fields = (
        'name',
        'address',
        'phone',
        'description',
    )
    page_title = "Home"
    model = Garage

    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return None


class GarageDetailView(DetailView):
    page_title = "Garage View"
    model = Garage
    exclude = ()

    def get_object(self, queryset=None):
        return Garage.objects.first()

