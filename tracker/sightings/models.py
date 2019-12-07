from django.db import models
from django.utils.translation import gettext as _
class Sq(models.Model):
    
    Longitude = models.FloatField(
        default = None,
        help_text = _('longitude coordinate'),
    )
    
    Latitude = models.FloatField(
        default = None,
        help_text = _('latitude coordinate'),
    )
    
    Unique_Squirrel_ID = models.CharField(
        max_length = 100,
        help_text = _('identification tag for each squirrel'),
        primary_key = True,
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
        help_text =_('YYYY-MM-DD'),
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
        max_length = 15,
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
        (ADULT, 'Ground Plane'),
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
        default = None,
        help_text = _('commentary on the squirrel location'),
    )

    Running = models.BooleanField(
        default = False,
    )

    Chasing = models.BooleanField(
        default = False,
    )

    Climbing  = models.BooleanField(
        default = False,
    )

    Eating = models.BooleanField(
        default = False,
    )

    Foraging = models.BooleanField(
        default = False,
    )

    Other_Activities = models.CharField(
        max_length = 100,
        default = None,
        help_text = _('describe squirrels other activities'),
    )

    Kuks = models.BooleanField(
        default = False,
    )

    Quaas  = models.BooleanField(
        default = False,
    )

    Moans = models.BooleanField(
        default = False,
    )

    Tail_Flags = models.BooleanField(
       default = False,
    )

    Tail_Twitches = models.BooleanField(
        default = False,
    )

    Approaches = models.BooleanField(
        default = False,
    )

    Indifferent = models.BooleanField(
        default = False,
    )

    Runs_From = models.BooleanField(
        default = False,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
