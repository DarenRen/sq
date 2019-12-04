from django.db import models
from django.utils.translation import gettext as _

class sq(models.Model):
    runs_from = models.BooleanField(
            default=True,
            help_text_= ('wheter squirrel was seen running from humans, seeing them as a threat.'))
    indifferent = models.BooleanField(
        default=True,
        help_text_ = ('whether squirrel was indifferent to human presence'))

    Approaches = models.BooleanField(
        default=True,
        help_text_ = ('whether squirrel was seen approaching human, seeking food.'))
    
    Tail_twitches = models.BooleanField(
            default=True,
            help_text_ = ('whether squirrel was seen twitching its tail.'))

    Tail_Flags = models.BooleanField(
            default=True,
            help_text_ = ("wheter Squirrel was seen flagging its tail. "))

    Moans = models.BooleanField(
            default=True,
            help_text_ = ('whether squirrel was heard moaning about the presence of air predator' ))

    Quaas  = models.BooleanField(
            default=True,
            help_text_ = ('whether squirrel was heard quaaing about the presence of group predator'))

    Kuks = models.BooleanField(
        default=True,
        help_text_ = ('whether squirrel was heard kukking'))
   
    Other_Activities = models.CharField(
            max_length = 100.
            help_text_ = ('describe squirrels other activities'))

    Foraging = models.BooleanField(
            default=True,
            help_text_ = ('whether squirrel was seen foraging for food'))

    Eating = models.BooleanField(
            default=True,
            help_text_ = ('whether squirrel was seen eating'))

    Climbing  = models.BooleanField(
            default=True,
            help_text_ = ('whether Squirrel was seen climbing'))





# Create your models here.
