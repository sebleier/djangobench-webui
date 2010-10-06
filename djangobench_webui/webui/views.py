from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from unipath import Path
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        from django.utils import simplejson as json


def results(request):
    benchmarks = []
    for path in Path(settings.RESULTS_DIR).listdir():
        benchmarks.append(json.load(open(path)))
    return render_to_response('base.html', {'benchmarks': benchmarks},
        context_instance=RequestContext(request))

def benchmark_data(request, benchmark):
    report = open(Path(settings.RESULTS_DIR).child("%s.json" % benchmark)).read()
    return HttpResponse(content=report, mimetype='application/json')
