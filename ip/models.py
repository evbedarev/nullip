from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Post(models.Model):
    STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline')
    )
    ip = models.CharField(max_length=250, unique_for_date='dt')
    dt = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=50,
                              default='online')
    intstates = models.IntegerField()
   # objects = models.Manager()


    class Meta:
        ordering = ('-dt',)

    def __str__(self):
        return self.ip

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #                    args=[self.publish.year,
    #                          self.publish.strftime('%m'),
    #                          self.publish.strftime('%d'),
    #                          self.slug])


# Create your models here.
