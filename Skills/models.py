from django.db import models

class Skills(models.Model):
    title = models.CharField(max_length=900,verbose_name='عنوان مهارت')
    percentage = models.IntegerField(default=0,verbose_name='درصد بلد بودن مهارت - مثال 30')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'مهارت ها'


    def __str__(self):
        return f'{self.title}'