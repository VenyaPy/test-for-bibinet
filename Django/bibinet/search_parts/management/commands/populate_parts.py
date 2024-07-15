import random
from django.core.management.base import BaseCommand
from search_parts.models import Part, Mark, Model


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        part_names = ["Engine", "Wheel", "Seat", "Door", "Window"]
        marks = list(Mark.objects.all())
        models = list(Model.objects.all())
        colors = ["Red", "Blue", "Green", "Black", "White"]

        parts = []

        for _ in range(10000):
            name = random.choice(part_names)
            mark = random.choice(marks)
            model = random.choice(models)
            price = round(random.uniform(50.0, 500.0), 2)
            json_data = {
                "color": random.choice(colors) if random.choice([True, False]) else None,
                "is_new_part": random.choice([True, False]) if random.choice([True, False]) else None,
                "count": random.randint(1, 10) if random.choice([True, False]) else None
            }
            json_data = {k: v for k, v in json_data.items() if v is not None}

            parts.append(Part(
                name=name,
                mark=mark,
                model=model,
                price=price,
                json_data=json_data,
                is_visible=True
            ))

        Part.objects.bulk_create(parts)
        self.stdout.write(self.style.SUCCESS("Parts populated successfully."))
