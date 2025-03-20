from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Diary(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    date = models.DateField(verbose_name='日付',default=timezone.now)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    text = models.CharField(verbose_name='本文',max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時',default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時',blank=True,null=True)
    tags = models.ManyToManyField(Tag,verbose_name= 'タグ', blank=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(verbose_name="作成日", default=timezone.now)
    memo = models.TextField()
    is_completed = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.memo[:20]}..."