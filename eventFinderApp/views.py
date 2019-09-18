from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Event, Account, Category
from .forms import EventForm, AccountForm

class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

class AccountView(generic.DetailView):
    model = Account
    template_name = 'eventFinderApp/account.html'


def account(request):
    accountform = AccountForm()
    return render(request, 'eventFinderApp/account.html', {'accountform': accountform})

class CreateEventView(LoginRequiredMixin, CreateView):
   template_name = 'eventFinderApp/add-event.html'
   form_class = EventForm
   login_url = '/users/login/'
   def form_valid(self, form):
       form.instance.host = self.request.user
       print(form.cleaned_data)
       return super().form_valid(form)

# class EditEventView(LoginRequiredMixin, CreateView):
#    template_name = 'eventFinderApp/edit-event.html'
#    form_class = EventForm
#    login_url = '/users/login/'
#    def form_valid(self, form):
#        form.instance.host = self.request.user
#        print(form.cleaned_data)
#        return super().form_valid(form)