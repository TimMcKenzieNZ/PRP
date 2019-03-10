from django.test import TestCase, Client
from django.core.exceptions import ValidationError
import datetime
from contextlib import contextmanager
from .modelAttributeValidators import validate_date_not_in_past, validate_progress, validate_date_not_in_future, validate_duration_is_positive
from .models import Project, Programme, Deliverable, Update, Initiative, TeamMember
from .utils import generate_update_log

class ValidationErrorTestMixin(object):

  @contextmanager
  def assertValidationErrors(self, fields):
    """
    Asserts a Validation Error is raised containing all (and only) the specified fields
    """
    try:
      yield
      raise AssertionError("ValidationError not raised") # We are expecting a Validation Error!
    except ValidationError as e:
        self.assertEqual(set(fields), set(e.message_dict.keys())) # check all given fields are in error


class ProjectValidationTests(ValidationErrorTestMixin, TestCase):

  # This test raises Integrity errors if you try to save the project
  def test_project_essential_fields_are_not_none(self):
    """
    Tests if validation errors are thrown for undefined fields
    """
    p = Project(name="Witch-blair", description="Handcam shinanigans", cost=10)
    with self.assertValidationErrors(['end_date', 'progress', 'image', 'priority', 'start_date']):
      p.full_clean()


class ValidatorTests(TestCase):

  def test_validate_process_edge_case_1(self):
    """
    Should not error for values >= 0 and <= 1
    """
    error_thrown = False
    try:
      validate_progress(-0.0)
    except ValidationError:
      error_thrown = True
    self.assertFalse(error_thrown)


  def test_validate_process_edge_case_2(self):
    """
    Should not error for values >= 0 and <= 1
    """
    with self.assertRaises(ValidationError) as e:
      validate_progress(1.00000000000001)
    self.assertEqual(e.exception.message, 'Progress 1.00000000000001 must be between 0 and 1 (inclusive)')


  def test_validate_process_edge_case_3(self):
    """
    Should not error for values >= 0 and <= 1
    """
    with self.assertRaises(ValidationError) as e:
      validate_progress(-0.00000000000000000000000001)
    self.assertEqual(e.exception.message, 'Progress -1e-26 must be between 0 and 1 (inclusive)')


  def test_validate_date_not_in_past(self):
    """
    Checking edge case when dates are the same
    """
    date = datetime.datetime.today().date()
    error_thrown = False
    try:
      validate_date_not_in_past(date)
    except ValidationError:
      error_thrown = True
    self.assertFalse(error_thrown)


  def test_validate_date_not_in_future(self):
    """
    Checking edge case when dates are the same
    """
    date = datetime.datetime.today().date()
    error_thrown = False
    try:
      validate_date_not_in_future(date)
    except ValidationError:
      error_thrown = True
    self.assertFalse(error_thrown)


  def test_validate_duration_is_positive(self):
    """
    Checking edge case when dates are the same
    """
    date = datetime.datetime.today().date()
    p = Programme(name="TV", description="Television", vision="the future", image="nope", start_date=date, end_date=date, slug="TV")
    error_thrown = False
    try:
      validate_duration_is_positive(Programme, p)
    except ValidationError:
      error_thrown = True
    self.assertFalse(error_thrown)


  def test_generate_update_log_blue_sky(self):
    """
    Checking if an update object is created as expected when an existing deliverable is updated
    """
    date = datetime.datetime.today().date()
    t = TeamMember(email="this@this.com", position='tester obviously', image ="nope", contact_number=1)
    t.save()

    i = Initiative(name='Init', description="desc", start_date=date,
      end_date=date, progress=0, status='Not Started', adapter_id=1, adapter_ref=1, order=1)
    i.save()
    initiative = Initiative.objects.get(pk=1)

    d = Deliverable(name="del", description="desc", end_date=date, progress=0, team_impact='none', pm_impact='none',
      sponsor_impact='none', order=1, status='Not Started', status_message='', initiative=initiative)
    d.author=TeamMember.objects.get(pk=1)
    d.log="testing"
    d.save()

    # An update is created at deliverable creation
    update_num = Update.objects.all().count()
    self.assertEqual(update_num, 1)

    # Everytime the deliverable is saved, an update is created
    generate_update_log(Deliverable, d) 
    update_num = Update.objects.all().count()
    self.assertEqual(update_num, 2)


class APITests(TestCase):
  """Tests the server API"""


  def setUp(self):
    self.c = Client()


  def test_search_programmes(self):
    response = self.c.get('/api/programmes')
    self.assertEquals(response.status_code, 200)


  def test_post_programme_should_fail(self):
    data = {
      "data": {
        "type": "programme",
        "attributes": {
          "name": "name",
          "description": "desc",
          "vision": "vision",
          "image": "nope",
          "start_date": "2018-04-04",
          "end_date": "2018-04-04",
          "slug": "slug",
          "members": []
        }
      }
    }
    response = self.c.post('/api/programmes', data)
    self.assertEquals(response.status_code, 405) # 405: Method not supported by resource


  # def test_deliverable_update(self):
  #   data = {
  #     "data": {
  #         "type": "deliverable",
  #         "attributes": {
  #       "sponsor_impact": "moderate",
  #       "team_impact": "moderate",
  #       "pm_impact": "moderate"
  #         }
  #     }
  #   }
  #   response = self.c.put('/api/deliverables/1', data)
  #   self.assertEquals(response.status_code, 201)

  # def test_post_update(self):
  #   data = {
  #     "data": {
  #         "type": "updates",
  #         "attributes": {
  #             "description": "Testing.",
  #             "date": "2018-04-04",
  #             "log": "Sponser impact changed from 'None' to 'High'. PM impact changed from 'None' to 'Moderate'.",
  #             "author": "http://localhost:8000/api/team_members/1",
  #             "deliverable": "http://localhost:8000/api/deliverables/14"
  #         }
  #     }
  #   }
  #   response = self.c.post('/api/updates', data)
  #   print(response)
  #   self.assertEquals(response.status_code, 200)

