from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


"""
Validates the given instance is an element in the given list of values from the given deliverable model.
"""
def validate_impact_choice(sender, instance, **kwargs):
  valid_choices = [choice[0] for choice in sender.CHOICES]
  impacts = [instance.team_impact, instance.pm_impact, instance.sponsor_impact]
  for choice in impacts:
    if  choice not in valid_choices:
      raise ValidationError(
          'Choice "{}" is not one of the permitted values: {}'.format(
              choice,
              ', '.join(valid_choices)))

"""
Validates the given date is not before todays's date
"""
def validate_date_not_in_past(end_date):
  today = datetime.datetime.today().date() 
  if end_date == None:
    raise ValidationError(
      "End date must be defined"
    )
  elif end_date < today:
    raise ValidationError(
      "End date '{}' cannot be in the past".format(end_date)
    )   

"""
Validates the given date is not after todays's date
"""
def validate_date_not_in_future(date):
  today = datetime.datetime.today().date()
  if date > today:
    raise ValidationError(
      'Date "{}" cannot be in the future'.format(date)
    )

"""
Validates the given progress float is between 0 and 1
"""
def validate_progress(value):
  if  value == None or value < 0 or value > 1:
    raise ValidationError(
      'Progress {} must be between 0 and 1 (inclusive)'.format(value)
    )

def validate_duration_is_positive(sender, instance, **kwargs):
  if instance.start_date == None or instance.end_date == None:
    raise ValidationError(
      'The start date and end date must be defined'
    )   
  elif instance.start_date > instance.end_date:
    raise ValidationError(
      'The start_date cannot be greater than the end_date'
    )
