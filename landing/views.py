import json
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from .models import Votos


def index(request):
    context = RequestContext(request)
    votos = Votos.objects.all().first()
    return render_to_response('index.html', {'cantidad_votos': votos.cantidad}, context)


@csrf_protect
def votar(request):
    if 'csrfmiddlewaretoken' in request.POST:
        votos = Votos.objects.all().first()
        votos.cantidad += 1
        votos.save()
        ret = {'cantidad_actual': str(votos.cantidad)}
        return HttpResponse(json.dumps(ret), content_type="application/json")
    else:
        return HttpResponseForbidden()