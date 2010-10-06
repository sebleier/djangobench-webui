from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_websocket import accept_websocket
from unipath import Path
import subprocess
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

def get_benchmark_json(benchmark):
    return open(Path(settings.RESULTS_DIR).child("%s.json" % benchmark)).read()

def benchmark_data(request, benchmark):
    report = get_benchmark_json(benchmark)
    return HttpResponse(content=report, mimetype='application/json')

@accept_websocket
def benchmark_realtime(request, benchmark):
    message = request.websocket.wait()
    if message == "start":
        # Return first benchmark right away
        report = get_benchmark_json(benchmark)
        request.websocket.send(report)
        # Start running for benchmarks
        cmd = ['djangobench', '--vcs', 'git', '--control=1.2', '--experiment=master', '--record', '../results',]
        cmd.append(benchmark)
        while not request.websocket.closed:
            subprocess.check_call(cmd, cwd=settings.BENCHMARK_REPO_PATH, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            report = get_benchmark_json(benchmark)
            request.websocket.send(report)
        return
