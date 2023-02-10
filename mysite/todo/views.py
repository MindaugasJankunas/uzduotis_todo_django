from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import UserTaskCreateForm


def index(request):
    return render(request, 'index.html')


class UserTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'user_tasks.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('due')


class UserTaskDetailView(UserPassesTestMixin, DetailView):
    model = Task
    template_name = 'user_task.html'
    context_object_name = 'task'

    def test_func(self):
        current_task = self.get_object()
        return self.request.user == current_task.user

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


class UserTaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    # fields = ['title', 'description', 'due', 'status']
    success_url = "/todo/my_tasks"
    template_name = 'user_task_form.html'
    form_class = UserTaskCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due', 'status']
    success_url = "/todo/my_tasks"
    template_name = 'user_task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        current_task = self.get_object()
        return self.request.user == current_task.user


class UserTaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = "/todo/my_tasks"
    template_name = 'user_task_delete.html'

    def test_func(self):
        current_task = self.get_object()
        return self.request.user == current_task.user

