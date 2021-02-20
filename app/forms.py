from django import forms
from .models import FileUpload
from django.core.files.storage import default_storage

# Create the form class.
class FileUploadForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('title', 'upload_file',)

class SingleUploadForm(forms.Form):
    file = forms.FileField(label='csv')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)