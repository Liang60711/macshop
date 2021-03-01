from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, ListView, DetailView
from .models import Item, UserProfile
from .forms import ItemForm
import random
import string

cities = [
    '臺北市',
    '新北市',
    '桃園市',
    '臺中市',
    '臺南市',
    '高雄市',
    '新竹縣',
    '苗栗縣',
    '彰化縣',
    '南投縣',
    '雲林縣',
    '嘉義縣',
    '屏東縣',
    '宜蘭縣',
    '花蓮縣',
    '臺東縣',
    '澎湖縣',
    '金門縣',
    '連江縣',
    '基隆市',
    '新竹市',
    '嘉義市',
]



def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))


class HomeView(View):
    def get(self, *args, **kwargs):
        item = Item.objects.all()
        context = {
            'item': item,
        }
        return render(self.request, 'home.html', context)


class SellView(View):
    def get(self, *args, **kwargs):
        form = ItemForm()
        context = {
            'form': form,
            'cities': cities,
            'years': [i for i in range(2021, 2008, -1)],
        }

        return render(self.request, 'sell.html', context)
    
    def post(self, *args, **kwargs):
        form = ItemForm(self.request.POST or None)
        sell_user = self.request.user
        slug = create_ref_code()
        print(3333333333333333333333333333333333333)
        print(form)
        if form.is_valid():
            try:
                item = Item(
                    item_class=form.cleaned_data.get('item_class'),
                    item_city=form.cleaned_data.get('item_city'),
                    item_year=form.cleaned_data.get('item_year'),
                    item_price=form.cleaned_data.get('item_price'),
                    item_image=self.request.FILES.get('item_image'),
                    description=form.cleaned_data.get('description'),
                    warranty=form.cleaned_data.get('warranty'),
                    slug=slug,
                )
                item.sell_user = sell_user
                item.save()

                messages.success(self.request, 'Your item uploads success.')
                return redirect('/')
            except:
                print(1111111111111111111111111111111111111111111111111111)
                return redirect('/')
        else:
            return redirect('core:sell')


            