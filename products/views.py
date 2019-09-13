from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Offer
from django.views import generic
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', { 'products' : products })



def new(request):
    del request.session['num_visits']
    return HttpResponse('This is NewPage')


@login_required
def Puzzle(request):
    return render(request, 'Puzzle.html')


@login_required
def offer(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    offers = Offer.objects.all()
    return render(request, 'offer.html', { 'offers' : offers , 'num_visits' : num_visits })


class OfferListView(generic.ListView):
    model = Offer

    def get_queryset(self):
        return Offer.objects.filter(code__icontains='w')[:1]
   # context_object_name = 'Offer_list'   # your own name for the list as a template variable
    #queryset = Offer.objects.filter(code__icontains='w')[:1] # Get 5 books containing the title war
    #template_name = 'products/Offer_list.html'  # Specify your own template name/location

    #def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
     #   context = super(OfferListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
      #  context['some_data'] = 'This is just some data'
      #  return context

    #def get_queryset(self):
     #   return { 'context': Offer.objects.all() }


