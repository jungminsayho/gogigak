import json

from django.http.response import JsonResponse
from django.views import View

from products.models import Category, Product

class ListingView(View):
    def get(self, request):
        category = Category.objects.get(name=request.GET['category'])
        products = Product.objects.filter(category=category.id)

        results = []
        for product in products:
            results.append({
                'name': product.name,
                'price': product.price,
                'grams': product.grams,
                'thumbnail': product.thumbnail,
                'isOrganic': product.is_organic
            })

        return JsonResponse({'results': results}, status=200)
        
## 판매수 리뷰수 parameter 어떻게 들어가는지 확인(ListingView에 추가할지 새로만들지)
