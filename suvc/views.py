from django.template import Context, loader
from django.http import HttpResponse
from suvc.models import News
# Create your views here.

def index(request):
    posts = News.objects.all()
    t = loader.get_template('index.html')
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))