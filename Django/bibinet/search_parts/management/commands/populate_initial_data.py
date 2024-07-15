from django.core.management.base import BaseCommand


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
