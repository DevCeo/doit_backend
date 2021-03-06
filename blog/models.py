from django.db import models
from django.contrib.auth.models import User
import os


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # allow_unicode는 한글 사용할수있게
    slug = models.SlugField(max_length=200, unique=True, blank=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=50)
    #요약문
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField(null=True)

    # 이미지 저장(head_image, blank=True는 있어도되고 없어도 된다는 뜻)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]