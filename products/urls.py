from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('offer', views.offer),
    path('puzzle',views.Puzzle),
    path('Offer_list', views.OfferListView.as_view(), name='Offer'),
]
