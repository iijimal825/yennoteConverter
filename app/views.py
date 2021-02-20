from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django_pandas.io import pd
from django.core.files import File
from django.core.files.storage import default_storage
#from .forms import SingleUploadForm
from .models import FileUpload
from .forms import FileUploadForm
from .kakeibo import Analyze

# Create your views here.
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
        df = pd.read_csv(file_value.upload_dir.path, index_col=0, encoding='cp932')
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
