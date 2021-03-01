from django.db import models
from django.conf import settings
from django.shortcuts import reverse

buy_or_sell_choices = (
    ('B', 'buy'),
    ('S', 'sell'),
)

category_choices = (
    ('p', 'phone'),
    ('mb', 'macbook'),
    ('m', 'mac'),
    ('ip', 'ipad'),
    ('ap', 'airpods'),
    ('oth', 'other'),
)

label_choices = (
    ('10', 'discount 10%'),
    ('5', 'discount 5%'),
)

class Item(models.Model):
    # relation
    sell_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sell_item', on_delete=models.SET_NULL, blank=True, null=True)
    
    # 物件資訊
    item_class = models.CharField(max_length=50)
    item_city = models.CharField(max_length=10)
    item_year = models.PositiveIntegerField()
    item_price = models.PositiveIntegerField()
    item_image = models.ImageField(upload_to='item', blank=True, null=True)
    # 補充說明
    description = models.TextField(blank=True, null=True)
    # 是否保固
    warranty = models.BooleanField(default=False)
    
    
    # 是否成交
    trade = models.BooleanField(default=False)
    # 標籤(是否折扣)
    label = models.CharField(max_length=2, choices=label_choices, blank=True, null=True, default=None)
    # po文日期
    article_datetime = models.DateTimeField(auto_now_add=True)
    # slug
    slug = models.SlugField(blank=True, null=True, )

    def __str__(self):
        return f'{self.pk}'
    
    def get_absolute_url(self):
        return reverse('core: item', kwargs={
            'slug': self.slug,
        })




class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 交易次數
    trade_number = models.PositiveIntegerField()


