#from django .http import HttpResponse
from django.shortcuts import render,redirect
from .forms import SignUpForm, FeedbackForm
from .models import Feedback
from django.contrib.auth.models import User
# Create your views here.

def CAcc(request):
      form = SignUpForm()
      if request.method =='POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('/')
      else:
            form = SignUpForm()

      return render (request, 'Pages/CAcc.html',{'form':form})



def is_valid_username(username):
    try:
        user = User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False

def Fdbk(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if not is_valid_username(username):
                form.add_error('username', 'Invalid username')
            else:
                text = form.cleaned_data['text']
                feedback = Feedback.objects.create(username=username, text=text)
                return redirect('thx')
    else:
        form = FeedbackForm()

    return render(request, 'Pages/Fdbk.html', {'form': form})


def Thx(request):
      return render (request, 'Pages/Thx.html')

