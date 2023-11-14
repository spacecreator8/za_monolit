from django.contrib.auth import login

from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView

from .models import Question, Choice, User
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import RegistrationForm, MyAuthenticationForm, ProfileForm


def homeView(request):
    return render(request, 'home.html')

def regView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.password2 = 'NULL'
                new_user = form.save()
                login(request, new_user)
                # return render(request, 'polls/reg_success.html')
                return redirect('polls:login')
        else:
            return render(request, 'polls/registration.html', {'form': form})

    else:
        form = RegistrationForm()
        return render(request, 'polls/registration.html', {'form':form})

class MyLoginView(LoginView):
    template_name = 'polls/login.html'
    form = MyAuthenticationForm
    next_page = 'polls:index'

    # def get_success_url(self):
    #     return reverse_lazy('polls:index')





class Profile(UpdateView):
    model = User
    fields = ['name', 'surname', 'mail', 'avatar']
    success_url = reverse_lazy('polls:index')
    template_name = 'polls/accounts/profile.html'





class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
