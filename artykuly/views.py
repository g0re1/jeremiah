# Create your views here.

from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

from artykuly.models import Art, Comment
from artykuly.forms import CommentForm


def index(request):
    latest_arts_list = Art.objects.all().order_by('date')
    t = loader.get_template('artykuly/index.html')
    c = Context({'latest_arts_list':latest_arts_list,'user':request.user,})
    return HttpResponse(t.render(c))


def show_art(request, slug):
    try:
        art = Art.objects.get(slug=slug)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                Comment(art=art,email=form.cleaned_data['email'],login=form.cleaned_data['login'],content=form.cleaned_data['content']).save()
            return redirect("/artykuly/"+str(art.slug))
        else:
            form = CommentForm()
         
        return render_to_response('artykuly/show.html',
                                  { 'form' : form,
                                    'art' : art,
                                    'comments' : art.comments.all().order_by('-date')
                                    }, context_instance = RequestContext(request))
    except Art.DoesNotExist:
        return redirect("/")
