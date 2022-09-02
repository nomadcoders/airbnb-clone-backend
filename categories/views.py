from django.http import JsonResponse
from .models import Category


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "ok": True,
            "categories": all_categories,
        }
    )
