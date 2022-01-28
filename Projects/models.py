from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=900,blank=True,null=True,verbose_name='عنوان پروژه ')
    photo = models.ImageField(upload_to="Projectphotos")
    link = models.CharField(max_length=900,verbose_name='لینک پروژه ')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'پروژه ها'


    def __str__(self):
        return f'{self.title}'