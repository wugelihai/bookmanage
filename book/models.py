from django.db import models


# Create your models here.
# 准备纾解列表信息的模型
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        # 把模型以字符串的方式输
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo)
