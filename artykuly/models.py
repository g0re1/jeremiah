from django.db import models

# Create your models here.

class User(models.Model):
        imie = models.CharField(max_length=200)
        nazwisko = models.CharField(max_length=200)
	nick = models.CharField(max_length=200)
	podpis = models.CharField(max_length=500)

	def __unicode__(self):
                return self.nick

class Art(models.Model):
        tytul = models.CharField(max_length=500)
        slug = models.SlugField(max_length=255, unique=True)
        tresc = models.TextField()
        user = models.ForeignKey(User)
        date = models.DateTimeField()
        ocena = models.FloatField()

        def __unicode__(self):
                return self.tytul

class Comment(models.Model):
    art = models.ForeignKey(Art, related_name = "comments")
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
