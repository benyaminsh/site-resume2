from django.db import models

class ContactMe(models.Model):
    name = models.CharField(max_length=900,verbose_name='نام ')
    email = models.CharField(max_length=900,verbose_name='نام ')
    message = models.TextField(verbose_name='پیام ')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تماس با من'


    def __str__(self):
        return f'{self.name} - {self.email}'
