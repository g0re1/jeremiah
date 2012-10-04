# Create your views here.

from django.template import Context, loader
from jeremiah.artykuly.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import Context, RequestContext
from django.views.decorators.http import require_GET, require_POST
from jeremiah.artykuly.forms import CommentForm
from jeremiah.artykuly.shortcuts import *

def index(request):
    latest_arts_list = Art.objects.all().order_by('date')
    t = loader.get_template('artykuly/index.html')
    c = Context({'latest_arts_list':latest_arts_list,})
    return HttpResponse(t.render(c))

def show_art(request, slug):
    try:
        art = Art.objects.get(slug=slug)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                Comment(art=art,email=form.cleaned_data['email'],login=form.cleaned_data['login'],content=form.cleaned_data['content']).save()
            return redirect_to("/artykuly/"+str(art.slug))
        else:
            form = CommentForm()
         
        return render_to_response('artykuly/show.html',
                                  { 'form' : form,
                                    'art' : art,
                                    'comments' : art.comments.all().order_by('-date')
                                    }, context_instance = RequestContext(request))
    except Art.DoesNotExist:
        return redirect_to("/")
