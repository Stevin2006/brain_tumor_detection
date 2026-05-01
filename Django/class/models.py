from django.db import models

class MRIScan(models.Model):
    image = models.ImageField(upload_to='mri_scans/')
    prediction = models.CharField(max_length=100, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scan {self.id} - {self.prediction}"