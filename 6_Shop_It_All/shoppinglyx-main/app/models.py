from django.db import models

# Create your models here.
class product(models.Model):

    CATEGORIES = (
    ('TROUSER','Trouser'),
    ('SUIT', 'suit'),
    ('SHORT','short'),
    ('SHIRT','shirt'),
    )


    title = models.CharField(max_length=40)
    description = models.TextField()
    brand = models.CharField(max_length=40)
    category = models.CharField(max_length=40,choices=CATEGORIES, default='TROUSER')
    selling_price = models.FloatField(null=True)
    discounted_price = models.FloatField(null=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title