from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from catalog.models import Journal
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class JournalListView(ListView):
    model = Journal
    template_name = 'catalog/journal_list.html'
    paginate_by = 20

class JournalDetailView(DetailView):
    model = Journal
    template_name = 'catalog/journal_detail.html'
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        try:
            obj = queryset.filter(name_slug=slug).get()
        except ObjectDoesNotExist:
            raise Http404('No found matching the query')
        return obj

def show(request,slug):
    return HttpResponse("OK %s" % slug)