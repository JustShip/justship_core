from django.db import models


class TimeStampedModel(models.Model):
    """
    A model to reuse the `created_at` and `updated_at` fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Social(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self) -> str:
        return f'{self.name}: {self.url}'
