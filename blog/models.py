from django.db import models
from django.conf import settings
from django.utils import timezone
#User = settings.AUTH_USER_MODEL()



class Documents(models.Model):
    docfile = models.ImageField(upload_to='documents/%Y/%m/%d')
    text = models.TextField(null=True,blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']


class Comments(models.Model):
    """Ксласс комментариев к новостям
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    new = models.ForeignKey(
         Documents,
         verbose_name="Новость",
         on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)
