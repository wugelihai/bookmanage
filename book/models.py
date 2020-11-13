from django.db import models

# Create your models here.
# 准备纾解列表信息的模型

"""
1.orm
    表-->类
    字段-->属性
    
2.模型需要集成自models.Model

3.模型类会自动为我们添加生成一个主键

4.属性名=属性选项（选项）

    属性名：不要使用Python，mysql关键字
        不要使用连续的下换线
        
    属性选项：和mysql的类型类似的
    
    选项：charfiled必须设置max_length
        varchar(M)
        null  是否为空
        unique 唯一
        default 设置默认值
        verbose_name 主要是admin后台显示
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        # 把模型以字符串的方式输
        return self.name


class PeopleInfo(models.Model):
    # 选项：
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    # 发布日期
    pub_date = models.DateField(null=True)
    # 阅读量
    readcount = models.IntegerField(default=0)
    # 点赞次数
    commentcount = models.IntegerField(default=0)
    # 是否逻辑删除
    id_del = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'admin'


# 准备任务列表信息的模型
class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # 外键 on_delete主表数据对从表有影响
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
