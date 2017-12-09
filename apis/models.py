from django.db import models
from django.conf import settings
from django.db.models import CASCADE
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Spring(models.Model):
    name = models.CharField(max_length=100, blank=True, default="")
    description = models.CharField(max_length=200, blank=True, default="")
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _("Spring ending %s") % self.end

class Task(models.Model):
    STATUS_TODO=1
    STATUS_IN_PROCESS = 2
    STATUS_TESTING = 3
    STATUS_DONE =4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not Start')),
        (STATUS_IN_PROCESS, _('In porcess')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, default="")
    spring = models.ForeignKey(Spring, blank=True, null=True, on_delete=CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    # assign = models.ForeignKey(settings.)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name
