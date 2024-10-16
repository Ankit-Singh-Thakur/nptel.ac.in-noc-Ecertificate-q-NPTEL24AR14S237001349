from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

# Create your models here.

def validate_pdf_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')



class Home(models.Model):
    pdf = models.FileField(upload_to='pdf/', validators=[FileExtensionValidator(['pdf']), validate_pdf_extension])
    
    def __str__(self):
        return str(self.pdf)