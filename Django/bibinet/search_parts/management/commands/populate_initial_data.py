from django.core.management.base import BaseCommand
from search_parts.models import Mark, Model


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        marks = [
            {"name": "Toyota", "producer_country_name": "Japan", "is_visible": True},
            {"name": "Ford", "producer_country_name": "USA", "is_visible": True},
            {"name": "Volkswagen", "producer_country_name": "Germany", "is_visible": True},
            {"name": "Hyundai", "producer_country_name": "South Korea", "is_visible": True},
            {"name": "Renault", "producer_country_name": "France", "is_visible": True}
        ]

        models = [
            {"name": "Camry", "mark_name": "Toyota", "is_visible": True},
            {"name": "Corolla", "mark_name": "Toyota", "is_visible": True},
            {"name": "Focus", "mark_name": "Ford", "is_visible": True},
            {"name": "Mustang", "mark_name": "Ford", "is_visible": True},
            {"name": "Golf", "mark_name": "Volkswagen", "is_visible": True}
        ]

        for mark_data in marks:
            mark, created = Mark.objects.get_or_create(name=mark_data["name"],
                                                       defaults=mark_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Mark {mark.name} created.'))

        for model_data in models:
            mark = Mark.objects.get(name=model_data["mark_name"])
            model, created = Model.objects.get_or_create(name=model_data["name"],
                                                         mark=mark,
                                                         defaults={'is_visible': model_data['is_visible']})
            if created:
                self.stdout.write(self.style.SUCCESS(f'Model {model.name} created.'))
