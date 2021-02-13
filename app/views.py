from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import FileUpload
from django_pandas.io import pd
from .forms import SingleUploadForm


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
    df = pd.read_csv(file_value.upload_dir.path, index_col=0)
    context = {
            'file_value': file_value,
            'df': df,
    }
    return render(request, 'app/detail.html', context)

class SingleUploadView(generic.FormView):
    form_class = SingleUploadForm
    template_name = 'app/upload.html'

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)