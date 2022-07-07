from django.db import models


class People(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}, {self.city}"

# Create your models here.
class Transaction(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE,related_name="history")
    amount = models.IntegerField()
    direction = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.person} moves {self.amount}"

class New_Members(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    reference = models.ManyToManyField(People, blank=True, related_name="member")

    def __str__(self):
        return f"{self.first} {self.last}"