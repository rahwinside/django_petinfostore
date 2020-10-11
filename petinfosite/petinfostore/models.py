from django.db import models

class Person(models.Model):
    given_name = models.CharField('given name',max_length=50)
    surname = models.CharField(max_length=50)
    def __str__ (self):
        return self.given_name + " " + self.surname

class Pet(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__ (self):
        return self.owner.__str__() + "'s " + self.name
