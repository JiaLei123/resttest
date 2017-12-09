from django.db import models

# Create your models here.
class Spring(models):
    name = models.CharField(max_length=100, blank=True, default="")
    description = models.CharField(blank=True, default="")
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _("Spring ending %s") % self.end

class Task(models.Model):
    