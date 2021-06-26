from django.db import models

# Create your models here.
class Timestampable(models.Model):
    created_at = models.DateTimeField(null=True, auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def modified(self):
        return True if self.updated_at else False