from django.shortcuts import render

# Create your views here.
from .models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodTypes, Goods


def home(request):
    wheels_list = Wheel.objects.all()
    nav_list = Nav.objects.all()
    must_buy_list = Mustbuy.objects.all()
    shop_list = Shop.objects.all()
    shop1 = shop_list[0]
    shop2 = shop_list[1:3]
    shop3 = shop_list[3:7]
    shop4 = shop_list[7:11]
    main_list = MainShow.objects.all()
    return render(request, 'axf/home.html',
                  {"wheels_list": wheels_list,
                   'nav_list': nav_list,
                   'must_buy_list': must_buy_list,
                   "shop1": shop1, "shop2": shop2,
                   "shop3": shop3, "shop4": shop4,
                   'main_list': main_list})


def market(request, categoryid, cid, sortid):
    leftSlider = FoodTypes.objects.all()

    if cid == '0':
        productList = Goods.objects.filter(categoryid=categoryid)
    else:
        productList = Goods.objects.filter(categoryid=categoryid, childcid=cid)

    # 排序
    if sortid == '1':
        productList = productList.order_by("productnum")
    elif sortid == '2':
        productList = productList.order_by("price")
    elif sortid == '3':
        productList = productList.order_by("-price")

    group = leftSlider.get(typeid=categoryid)
    childList = []
    # 全部分类:0#进口水果:103534#国产水果:103533
    childnames = group.childtypenames
    arr1 = childnames.split("#")
    for str in arr1:
        # 全部分类:0
        arr2 = str.split(":")
        obj = {"childName": arr2[0], "childId": arr2[1]}
        childList.append(obj)

    return render(request, 'axf/market.html',
                  {"leftSlider": leftSlider, "productList": productList, "childList": childList,
                   "categoryid": categoryid, "cid": cid})


def cart(request):
    return render(request, 'axf/cart.html')


def mine(request):
    return render(request, 'axf/mine.html')


from django.contrib.staticfiles.finders import FileSystemFinder, AppDirectoriesFinder

def login(request):
    pass
def register(request):
    pass