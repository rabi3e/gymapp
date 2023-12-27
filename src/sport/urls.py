from django.urls import path
from .views import AdherentList


app_name = 'sport'
urlpatterns = [
    path('',AdherentList.as_view(),name='adherent_liste')
   
]
