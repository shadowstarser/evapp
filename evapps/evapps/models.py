from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField("url", max_length=50)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_name = ['name']

class Type(models.Model):
    T_id = models.ForeignKey()
    T_name = models.CharField((verbose_name='Subject', max_length="200"))

class Entity(models.Model):
    E_id = models.CharField(verbose_name='Nomber Event', db_index=True, max_length=10)
    E_type = models.ForeignKey(Type, verbose_name='Type Entity',  on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='User' , on_delete=models.CASCADE)
    E_Category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    E_subject = models.CharField(verbose_name='Subject', max_length="200")
    E_note = models.TextField(verbose_name='Descriptions', max_length="10000")
    E_create_date = models.DateTimeField(verbose_name="Date create", default=timezone.now)
    E_change_date = models.DateTimeField(verbose_name="Date change")
