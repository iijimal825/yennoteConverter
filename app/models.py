from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
import os

# Create your models here.

class FileUpload(models.Model):
    """
    ファイルのアップロード
    """
    title = models.CharField(default='年月', max_length=100)
    upload_file = models.FileField(upload_to='csv', validators=[FileExtensionValidator(['csv',])])
    created_at = models.DateField(auto_now_add=True)
    analyzed_file = models.FileField(upload_to='xlsx', validators=[FileExtensionValidator(['xlsx',])], blank=True, null=True)

    def __str__(self):
        return self.title

    def upload_file_name(self):
        """
        アップロードファイルパスからファイル名のみを取得するカスタムメソッド
        """
        path = os.path.basename(self.upload_file.name)
        return path

    def analyzed_file_name(self):
        """
        解析後ファイルパスからファイル名のみを取得するカスタムメソッド
        """
        path = os.path.basename(self.analyzed_file.name)
        return path