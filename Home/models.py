from django.db import models

class Settings(models.Model):
    name = models.CharField(max_length=900,blank=True,null=True,verbose_name='نام و نام خانوداگی ')
    age = models.CharField(max_length=900,blank=True,null=True,verbose_name='سن ')
    photo = models.ImageField(upload_to="images",blank=True,null=True,verbose_name='تصویر شما ')
    title = models.CharField(max_length=900,blank=True,null=True,verbose_name='عنوان وب سایت ')
    jobside = models.CharField(max_length=900,blank=True,null=True,verbose_name='سمت شغلی - مثال back end ')
    email = models.CharField(max_length=900,blank=True,null=True,verbose_name='ایمیل ')
    phone = models.CharField(max_length=900, blank=True, null=True, verbose_name='تلفن ')
    instagram = models.CharField(max_length=900,blank=True,null=True,verbose_name='اینستاگرام ')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return f'{self.name}'


