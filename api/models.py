from django.db import models

from .enums import STATUS

# Create your models here.
class Timestampable(models.Model):
    created_at = models.DateTimeField(null=True, auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def modified(self):
        return True if self.updated_at else False

class Activatable(models.Model):
    status = models.CharField(choices=STATUS, max_length=10, default=STATUS.ACTIVE)

    class Meta:
        abstract = True

class Feedback(Timestampable):
    subject = models.CharField(max_length=100)
    feedback = models.TextField()
    file = models.FileField(upload_to='feedback/', null=True, blank=True)
    
    user = models.ForeignKey('users.CRUser', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.feedback