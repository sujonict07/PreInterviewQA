from django.test import TestCase
from .models import PreInterviewModel
# Create your tests here.

# fields = [
#             'name',
#             'email',
#             'join_time',
#             'current_salary',
#             'salary_expection',
#             'why_join',
#             'week_day',
#             'interview_time',
#             'interested_job',
#         ]
class PreInterviewModelTestCase(TestCase):
    def setUp(self):
        PreInterviewModel.objects.create(
            name="kkk",
            email="test@mail.com",
            join_time='20th september',
            current_salary=20000,
            salary_expection=30000,
            why_join='issa',
            week_day='Sunday',
            interview_time='Morning',
            interested_job='Python expart',

        )
        PreInterviewModel.objects.create(
            name="sujon",
            email="test@mail.com",
            join_time='20th september',
            current_salary=20000,
            salary_expection=30000,
            why_join='issa',
            week_day='Sunday',
            interview_time='Morning',
            interested_job='Python expart',

        )

    def test_get_values(self):
        value = PreInterviewModel.objects.get(name='kkk')
        self.assertEqual(value.email, 'test@mail.com')
        self.assertEqual(value.current_salary,20000)
        value1 = PreInterviewModel.objects.get(name='sujon')
        self.assertEqual(value1.email, 'test@mail.com')

