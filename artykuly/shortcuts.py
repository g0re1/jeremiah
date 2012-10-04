from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
 
def redirect_to(url_or_view, *args, **kwargs):
    try:
        return HttpResponseRedirect(reverse(url_or_view, *args, **kwargs))
    except NoReverseMatch:
        return HttpResponseRedirect(url_or_view, *args, **kwargs)
