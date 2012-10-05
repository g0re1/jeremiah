# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from default.forms import FormularzLogowania, FormularzRejestracji
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.contrib.auth import login,authenticate,logout


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/jeremiah")

def register_page(request):
    if request.method == 'POST':
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
              username=form.cleaned_data['username'],
              password=form.cleaned_data['password1'],
              email=form.cleaned_data['email']
            )
            user.save()
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,user)
            return HttpResponseRedirect("/jeremiah")           
    else:
        form = FormularzRejestracji()
    template = get_template("registration/register.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)

def login_page(request):
    if request.method == 'POST':
        form = FormularzLogowania(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)
            return HttpResponseRedirect("/jeremiah")                         
    else: 
        form = FormularzLogowania()
    template = get_template("registration/login.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)
