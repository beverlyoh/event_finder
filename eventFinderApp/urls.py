from django.urls import path
from . import views

app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('account/', views.account, name='account'),
    # event-finder/add-event
    path('add-event/', views.CreateEventView.as_view(), name='add_event')

]