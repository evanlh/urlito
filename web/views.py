from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from web.models import Url

# Create your views here.
def index(request):
    if request.method == 'POST':
        long_url = request.POST['url']
        validate = URLValidator()
        extraclass = ''
        try:
            validate(long_url)
        except ValidationError, e:
            error = "Invalid URL, please provide another"
            return render_to_response('index.html', {'error': error, 'extraclass': 'has-error'}, context_instance=RequestContext(request))

        url = Url(url=long_url)
        url.save()
        return render_to_response('shortened.html',
                                  {'url': 'http://' + request.get_host() + '/' + url.short_url},
                                  context_instance=RequestContext(request))

    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def resolver(request, short_url):
    id = Url.decode(short_url)
    try:
        url = Url.objects.get(pk=id)
    except Url.DoesNotExist:
        raise Http404
    # log request
    return HttpResponseRedirect(url.url)
