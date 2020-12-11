from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.db import IntegrityError

class Genre(models.Model):
   title = models.CharField(max_length=250)
   artist = models.CharField(max_length=250, default='')
   thumbnail = models.CharField(max_length=500, default='')
   description = models.CharField(max_length=500, default='')
   time_stamp = models.DateTimeField('solved time', default=timezone.now)
   id = models.CharField(primary_key=True, max_length=32)
   order = models.IntegerField(default=0)

   def save(self, *args, **kwargs):
       if self.id:
           super(Genre, self).save(*args, **kwargs)
           return

       unique = False
       while not unique:
           try:
               self.id = uuid4().hex
               super(Genre, self).save(*args, **kwargs)
           except IntegrityError:
               self.id = uuid4().hex
           else:
               unique = True
   def __unicode__(self):
       return self.title
   def __str__(self):
       return self.title

class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=500, default='')
    thumbnail = models.CharField(max_length=500, default='')
    description = models.TextField(max_length=20000, default='')
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.id:
            super(Book, self).save(*args, **kwargs)
            return

        unique = False
        while not unique:
            try:
                self.id = uuid4().hex
                super(Book, self).save(*args, **kwargs)
            except IntegrityError:
                self.id = uuid4().hex
            else:
                unique = True

    def __unicode__(self):
        return self.title