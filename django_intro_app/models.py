from enum import Enum
from typing import List

from django.db import models
from django.db.models import F

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


@auto_str(['id', 'name', 'color'])
class Line(models.Model):
    class Meta:
        db_table = 'line'
        indexes = [
            models.Index(fields=['color'])
        ]

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)


class Direction(models.IntegerChoices):
    INBOUND = 0
    OUTBOUND = 1


@auto_str(['id', 'name'])
class Station(models.Model):
    class Meta:
        db_table = 'station'
        indexes = [
            models.Index(fields=['name'])
        ]

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    line = models.ForeignKey(Line, on_delete=models.RESTRICT)


@auto_str(['id', 'name'])
class Branch(models.Model):
    class Meta:
        db_table = 'branch'

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    line = models.ForeignKey(Line, on_delete=models.RESTRICT)
    direction = models.IntegerField(choices=Direction, default=Direction.INBOUND)
    # access from station side:
    #   station.branches.all()
    # access from branch side:
    #   branch.stations.all()
    stations = models.ManyToManyField(Station, through="BranchStation", related_name="branches")


# Many-to-many with an extra field, so introduce a helper entity
class BranchStation(models.Model):
    class Meta:
        db_table = 'branch_station'
        ordering = [F('order').asc()]
        indexes = [
            models.Index(F('branch'), F('order').asc(), name='branch_order')
        ]
        constraints = [
            models.UniqueConstraint(fields=['branch', 'station'], name='uq_branchstation_branch_station')
        ]

    id = models.UUIDField(primary_key=True)
    station = models.ForeignKey(Station, on_delete=models.RESTRICT)
    branch = models.ForeignKey(Branch, on_delete=models.RESTRICT)
    order = models.IntegerField()


@auto_str(['id', 'name'])
class Train(models.Model):
    class Meta:
        db_table = 'train'

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=8)
    line = models.ForeignKey(Line, on_delete=models.RESTRICT)