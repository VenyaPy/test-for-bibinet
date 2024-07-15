from django.http import JsonResponse
from django.db.models import Q, Sum
from django.views.decorators.csrf import csrf_exempt

from .models import Mark, Model, Part
import json


def mark_list(request):
    marks = list(Mark.objects.values())
    return JsonResponse(marks, safe=False)


def model_list(request):
    models = list(Model.objects.values())
    return JsonResponse(models, safe=False)


@csrf_exempt
def search_part(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        mark_name = body.get('mark_name')
        part_name = body.get('part_name')
        params = body.get('params', {})
        mark_list = body.get('mark_list')
        price_gte = body.get('price_gte')
        price_lte = body.get('price_lte')
        page = body.get('page', 1)

        query = Q()

        if mark_name:
            query &= Q(mark__name__icontains=mark_name)

        if part_name:
            query &= Q(name__icontains=part_name)

        if mark_list:
            query &= Q(mark__id__in=mark_list)

        if 'color' in params:
            query &= Q(json_data__color=params['color'])

        if 'is_new_part' in params:
            query &= Q(json_data__is_new_part=params['is_new_part'])

        if price_gte is not None:
            query &= Q(price__gte=price_gte)

        if price_lte is not None:
            query &= Q(price__lte=price_lte)

        parts = Part.objects.filter(query)

        total_count = parts.count()
        total_sum = parts.aggregate(total_sum=Sum('price'))['total_sum'] or 0

        start = (page - 1) * 10
        end = start + 10
        parts = parts[start:end]

        response = [
            {
                "mark": {
                    "id": part.mark.id,
                    "name": part.mark.name,
                    "producer_country_name": part.mark.producer_country_name
                },
                "model": {
                    "id": part.model.id,
                    "name": part.model.name
                },
                "name": part.name,
                "json_data": part.json_data,
                "price": part.price
            }
            for part in parts
        ]

        return JsonResponse({
            "response": response,
            "count": total_count,
            "summ": total_sum
        }, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)