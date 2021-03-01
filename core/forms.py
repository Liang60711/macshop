from django import forms
from .models import Item

class ItemForm(forms.Form):
    # 物件資訊
    item_class = forms.CharField()
    item_city = forms.CharField()
    item_year = forms.CharField()
    item_price = forms.CharField()

    # 照片
    item_image = forms.FileField(required=False)

    # 是否保固
    warranty = forms.BooleanField(required=False)
    
    # 補充說明
    description = forms.CharField(widget=forms.Textarea)
    # class Meta():
    #     model = Item
    #     fields = '__all__'



    
