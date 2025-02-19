from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Diary(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    date = models.DateField(verbose_name='日付',default=timezone.now)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    text = models.CharField(verbose_name='本文',max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時',default=timezone.now())
    updated_at = models.DateTimeField(verbose_name='編集日時',blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Todo(models.Model):
    time = models.DateField(verbose_name="作成日", default=timezone.now)
    memo = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
