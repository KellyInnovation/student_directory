from django.test import TestCase
from django.core.urlresolvers import reverse

class BlogViewsTests(TestCase):

	def test_views_index(self):
		index_url = reverse('students:index')

		response = self.client.get(index_url)
		self.assertEqual(response.status_code, 200)