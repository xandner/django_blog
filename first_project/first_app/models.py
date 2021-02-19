from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

#managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status="p")

class Category(models.Model):
    parent=models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='children',verbose_name='زیر دسته')
    title=models.CharField(max_length=255,verbose_name='عنوان دسته بندی')
    slug=models.SlugField(max_length=255,unique=True,verbose_name='آدرس دسته بندی')
    status=models.BooleanField(default=True,verbose_name='نمایش داده شود؟')
    position=models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"
        ordering=['-parent__id','-position']

    def __str__(self):
        return self.title

    
    

class Article(models.Model):
    choises = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=255,verbose_name='تیتر مقاله')
    slog = models.SlugField(max_length=255, unique=True,verbose_name='آدرس مقاله')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to='images',verbose_name='تصویر')
    published = models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now=True,verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True,verbose_name='زمان ویرایش')
    status = models.CharField(max_length=1, choices=choises,verbose_name='وضعیت')
    category=models.ManyToManyField(Category,verbose_name='دسته بندی',related_name='articles')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
        ordering=['-published']
    def jpublished(self):
        return jalali_converter(self.published)

    jpublished.short_description='زمان انتشار'

    def category_published(self):
        return self.category.filter(status=True)

    
    objects=ArticleManager()