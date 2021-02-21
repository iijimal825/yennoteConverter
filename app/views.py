from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django_pandas.io import pd
from django.core.files import File
from django.core.files.storage import default_storage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm
from .models import FileUpload
from .forms import FileUploadForm
from .kakeibo import Analyze

# Create your views here.
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'app/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'app/login.html'

"""
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form,})

account_login = Account_login.as_view()
"""

def index(request):
    """
    トップページ
    """
    file_obj = FileUpload.objects.all()
    context = {
        'file_obj': file_obj,
    }
    return render(request, 'app/index.html', context)

def detail(request, pk):
    """
    詳細ページ
    """
    file_value = get_object_or_404(FileUpload, id=pk)
    try:
        # utf-8に対応
        df = pd.read_csv(file_value.upload_file.path, index_col=0)
    except UnicodeDecodeError:
        # cp932に対応
        df = pd.read_csv(file_value.upload_file.path, index_col=0, encoding='cp932')
    context = {
            'file_value': file_value,
            'df': df,
    }
    return render(request, 'app/detail.html', context)

def analyze(request, pk):
    """
    解析結果ページ
    """
    file_value = get_object_or_404(FileUpload, id=pk)
    analyze = Analyze()
    df = analyze.run(file_value.upload_file.path, pk)
    file_value = get_object_or_404(FileUpload, id=pk)
    context = {
            'file_value': file_value,
            'df': df,
    }
    return render(request, 'app/analyze.html', context)

def new_file(request):
    """
    ファイルアップロードページ
    """
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = FileUploadForm()
    return render(request, 'app/new_file.html', {'form': form })
