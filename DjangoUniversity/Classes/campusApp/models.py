from django.db import models

# Create your models here.

# Creates a model of University Campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)

    # creates a model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        name_state = '{0.campus_name}: {0.state}'
        return name_state.format(self)

    # Sets the correct plural name for the model
    class Meta:
        verbose_name_plural = 'University Campuses'
