from django.db import models


class Mark(models.Model):
    name = models.CharField(max_length=255)
    producer_country_name = models.CharField(max_length=255)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['producer_country_name']),
        ]


class Model(models.Model):
    name = models.CharField(max_length=255)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]


class Part(models.Model):
    name = models.CharField(max_length=255)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    json_data = models.JSONField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['json_data']),
        ]

