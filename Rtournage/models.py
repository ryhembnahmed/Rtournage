from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField()
    min_limit_alert = models.IntegerField()
    max_limit_alert = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        if self.type is None:
            return '{} - {}'.format(self.category, self.reference)
        else:
            return '{} - {}/{}'.format(self.category, self.type, self.reference)


class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="transactions")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateField(null=False, blank=False)
    transaction_type = (
        (1, "Buy"),
        (2, "Sell"),
    )
    type = models.IntegerField(choices=transaction_type, default=1)

    def save(self, *args, **kwargs):
        if self.type == 1:
            self.product.quantity += int(self.quantity)
        else:
            self.product.quantity -= int(self.quantity)

        self.product.save()
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        transaction = "Buy" if self.type == 1 else "Sell"
        return '{} : {}   =====>   {} item(s) with {} dt on {}'.format(transaction, self.product, self.quantity, self.price, self.date)
