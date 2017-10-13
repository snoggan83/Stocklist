from django.db import models

class Stocklist(models.Model):
    list_title = models.CharField(max_length=250)

    def __str__(self):
        return self.list_title

class Stock(models.Model):
    stocklist = models.ForeignKey(Stocklist, on_delete=models.CASCADE)
    stock_title = models.CharField(max_length=200)
    stocktag_str = models.CharField(max_length=200)
    stocktag_num = models.IntegerField()
    in_portfolio = models.BooleanField(default=False)

    def __str__(self):
        return self.stock_title
