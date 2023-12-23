from django.db import models
# Create your models here.


class Article(models.Model):
    title = models.CharField("文章标题", max_length=128)
    image = models.ImageField("标题照片", upload_to="static\img", null=True)
    content = models.TextField("文章内容", default="空空如也")
    tag = models.CharField("文章标签", default="python", max_length=128)
    create_at = models.DateField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.title