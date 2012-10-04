from django.template import Context, loader
from igore.news.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import Context, RequestContext
from django.views.decorators.http import require_GET, require_POST
from igore.news.forms import CommentForm
from igore.news.shortcuts import *
import math

def index(request):
    latest_news_list = News.objects.all().order_by('-date')[0:3]
    t = loader.get_template('news/index.html')
    count = News.objects.all().count()
    x=count/3
    x=math.ceil(x)
    count=[]
    for i in range(1,x+1):
       count.append(i)
    c = Context({'latest_news_list':latest_news_list,'count':count,})
    return HttpResponse(t.render(c))

def index_pag(request,id):
    id=int(id)
    id*=3
    latest_news_list = News.objects.all().order_by('-date')[id-3:id]
    count = News.objects.all().count()
    x=count/3
    x=math.ceil(x)
    count=[]
    for i in range(1,x+1):
       count.append(i)                       
    t = loader.get_template('news/index.html')
    c = Context({'latest_news_list':latest_news_list,'count':count,})
    return HttpResponse(t.render(c))

def show_news(request, slug):
    try:
        news = News.objects.get(slug=slug)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                Comment(news=news,email=form.cleaned_data['email'],login=form.cleaned_data['login'],content=form.cleaned_data['content']).save()
            return redirect_to("/news/"+str(news.slug))
        else:
            form = CommentForm()
         
        return render_to_response('news/show.html',
                                  { 'form' : form,
                                    'news' : news,
                                    'comments' : news.comments.all().order_by('-date')
                                    }, context_instance = RequestContext(request))
    except News.DoesNotExist:
        return redirect_to("/")

    
