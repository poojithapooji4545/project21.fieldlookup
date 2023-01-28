from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from app.models import *
def display_topic(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    qsw=Webpage.objects.all()
    qsw=Webpage.objects.filter(name__startswith='c')
    qsw=Webpage.objects.filter(name__endswith='i')
    qsw=Webpage.objects.all()
    qsw=Webpage.objects.filter(name__contains='m')
    qsw=Webpage.objects.filter(name__regex='\w{2}')
    qsw=Webpage.objects.filter(name__in=['cm','jaya'])
    qsw=Webpage.objects.filter(Q(topic_name='cricket')| Q(name='cm'))
    qsw=Webpage.objects.all()
    qsw=Webpage.objects.filter(Q(topic_name='kabaddi')& Q(name__startswith='j'))

    d={'webpages':qsw}
    return render(request,'display_webpage.html',d)

def display_access(request):
    qsa=AccessRecord.objects.all()
    qsa=AccessRecord.objects.filter(date='1999-02-07')
    qsa=AccessRecord.objects.filter(date__gt='1999-07-02')
    qsa=AccessRecord.objects.filter(date__gte='1999-07-05')
    qsa=AccessRecord.objects.filter(date__lt='1998-07-02')
    qsa=AccessRecord.objects.filter(date__lte='1998-07-02')
    qsa=AccessRecord.objects.all()
    qsa=AccessRecord.objects.filter(date__year='1997')
    qsa=AccessRecord.objects.filter(date__month='07')
    qsa=AccessRecord.objects.filter(date__day='05')
    qsa=AccessRecord.objects.filter(date__year__gt='1998')
    d={'access':qsa}
    return render(request,'display_access.html',d)
        