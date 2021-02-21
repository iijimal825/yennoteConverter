from django import forms
from .models import FileUpload
from django.core.files.storage import default_storage
from django.contrib.auth.forms import AuthenticationForm

# Create the form class.
class LoginForm(AuthenticationForm):
    '''
    ログインフォーム
    '''
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       # htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'

class FileUploadForm(forms.ModelForm):
    '''
    アップロードフォーム
    '''
    class Meta:
        model = FileUpload
        fields = ('title', 'upload_file',)
