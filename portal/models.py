from django.db import models
from django.utils import timezone
import uuid
# Create your models here.

class Attend(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number=models.CharField(verbose_name='学籍番号', max_length=40)
    nationality=models.CharField(verbose_name='国籍', max_length=40)
    name=models.CharField(verbose_name='名前', max_length=40)
    kana=models.CharField(verbose_name='フリガナ', max_length=40)
    gender=models.CharField(verbose_name='男女', max_length=40)
    email=models.CharField(verbose_name='メールアドレス', max_length=40)
    abbre=models.CharField(verbose_name='ユーザーネーム', max_length=40)