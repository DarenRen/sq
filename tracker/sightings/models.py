from django.db import models
from django.utils.translation import gettext as _

class Sq(models.Model):
    
    X = models.FloatField(
        help_text = _('longitude coordinate'),
    )
    
    Y = models.FloatField(
        help_text = _('longtitude coordinate'),
    )
    
    Unique_Squirrel_ID = models.CharField(
        max_length = 100,
        help_text = _('identification tag for each squirrel'),
    )
    
    AM = 'am'
    PM = 'pm'
    OTHER = ''
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
        (OTHER, ''),
    )
    Shift = models.CharField(
        max_length = 20,
        choices = SHIFT_CHOICES,
        default = OTHER,
    )
    
    Date = models.DateField(
        help_text =_('month, day, and year (MMDDYYYY)'),
    )
    
    ADULT = 'adult'
    JUVENILE = 'juvenile'
    OTHER = ''
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        (OTHER, ''),
    )
    Age = models.CharField(
        max_length = 20,
        choices = AGE_CHOICES,
        default = OTHER,
    )
    
    GRAY = 'gray'
    BLACK = 'black'
    CINNAMON = 'cinnamon'
    OTHER = ''
    PRICOLOR_CHOICES = (
        (GRAY, 'Gray'),
        (BLACK, 'Black'),
        (CINNAMON, 'Cinnamon'),
        (OTHER, ''),
    )
    Primary_Fur_Color = models.CharField(
        max_length = 20,
        choices = PRICOLOR_CHOICES,
        default = OTHER,
    )
    
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    OTHER = ''
    LOCATION_CHOICES = (
        (ADULT, '"Ground Plane'),
        (JUVENILE, 'Above Ground'),
        (OTHER, ''),
    )
    Location = models.CharField(
        max_length = 20,
        choices = LOCATION_CHOICES,
        default = OTHER,
    )
    
    Specific_Location = models.CharField(
        max_length = 100,
        help_text = _('commentary on the squirrel location'),
    )

    Running = models.BooleanField(
        default = True
    )

    Chasing = models.BooleanField(
        default = True
    )

    Climbing  = models.BooleanField(
        default = True,
    )

    Eating = models.BooleanField(
        default = True,
    )

    Foraging = models.BooleanField(
        default = True,
    )

    Other_Activities = models.CharField(
        max_length = 100,
        help_text = _('describe squirrels other activities'),
    )

    Kuks = models.BooleanField(
        default = True,
    )

    Quaas  = models.BooleanField(
        default = True,
    )

    Moans = models.BooleanField(
        default = True,
    )

    Tail_Flags = models.BooleanField(
        default = True,
    )

    Tail_Twitches = models.BooleanField(
        default = True,
    )

    Approaches = models.BooleanField(
        default = True,
    )

    Indifferent = models.BooleanField(
        default = True,
    )

    Runs_From = models.BooleanField(
        default = True,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
