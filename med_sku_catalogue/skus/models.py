from django.db import models

class MedicationSKU(models.Model):
    name = models.CharField(max_length=100, unique=True)
    presentation = models.CharField(max_length=50)
    dose = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=10)

    class Meta:
        unique_together = ('name', 'presentation', 'dose', 'unit')
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.dose}{self.unit} ({self.presentation})"
