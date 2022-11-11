from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Topic, Reply
from django.contrib.auth.decorators import login_required
from .forms import TopicForm
# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('discussions')
    else:
        topics = Topic.objects.all()
        form = TopicForm()
    return render(request,'discussion/index.html',{'form':form,'topics':topics})
