from django.http import JsonResponse
from .models import Mark, Model, Part


def mark_list(request):
    marks = list(Mark.objects.values())
    return JsonResponse(marks, safe=False)


def model_list(request):
    models = list(Model.objects.values())
    return JsonResponse(models, safe=False)
