from django.test import TestCase

from simple_search.api.models import Search

class AnimalTestCase(TestCase):
    def setUp(self):
        Search.objects.create(name="search1", matcher="MATCHER1").save()
        Search.objects.create(name="search2", matcher="MATCHER2").save()

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        search1 = Search.objects.get(name="search1")
        self.assertEqual(search1.matcher, 'MATCHER1')
