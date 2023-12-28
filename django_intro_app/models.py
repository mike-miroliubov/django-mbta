from typing import List

from django.db import models

# Create your models here.


def auto_str(fields: List[str]):
    """
    A decorator that auto-generates a __str__ method for a class
    """
    # to create a parameterized decorator, this one is a factory that builds a decorator
    def decorator(cls):
        def __str__(self):
            return '%s(%s)' % (
                type(self).__name__,
                # this is a generator
                ', '.join('%s=%s' % (field, getattr(self, field)) for field in fields)
            )

        cls.__str__ = __str__
        return cls

    return decorator


@auto_str(['id', 'name', 'order'])
class Station(models.Model):
    class Meta:
        db_table = 'station'

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    order = models.IntegerField()


@auto_str(['id', 'name', 'color'])
class Line(models.Model):
    class Meta:
        db_table = 'line'

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)


@auto_str(['id', 'name'])
class Branch(models.Model):
    class Meta:
        db_table = 'branch'

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    line = models.ForeignKey(Line, on_delete=models.RESTRICT)


@auto_str(['id', 'name'])
class Train(models.Model):
    class Meta:
        db_table = 'train'

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=8)
    line = models.ForeignKey(Line, on_delete=models.RESTRICT)