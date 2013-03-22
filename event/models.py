from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    # http://www.barcoo.com/de/w/4260031874056
    barcode = models.CharField(max_length=200)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.URLField(max_length=200)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(max_length=4)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    product = models.ForeignKey(Product)
    ACTIONS = (
        ('B', 'Einkauf'),
        ('C', 'Konsum'),
        ('R', 'Pfand'),
        ('A', 'Guthaben'),
    )
    action = models.CharField(max_length=2, choices=ACTIONS, blank=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        # return " ".join([str(self.user), str(self.action), str(self.product), str(self.timestamp), str(self.amount), str(self.value)])
        return self.timestamp.strftime("%Y-%m-%d %H:%M") + " " + str(self.user) + ": " + str(self.get_action_display()) + " " + str(self.amount) + "x " + str(self.product) + " (EUR " + str(self.value) + ")"
