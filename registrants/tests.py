from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from registrants.forms import ExtendedUserCreationForm, UserProfileForm


class FormPostTest(TestCase):
    """ To test form creation """

    # Test to make sure the userprofile form is valid
    def test_userprofile_form(self):

        form_info = {
            'location': "Toronto",
            'age': 22,
            'image': "default.jpg",
            'gender': 'M',
         }

        form = UserProfileForm(data=form_info)
        self.assertTrue(form.is_valid())

    # Test extended user form
    def test_extended_user_form(self):

        form_info = {
            'first_name': 'john',
            'last_name': 'doe',
            'username': 'doeman',
            'email': 'doe@maill.com',
            'password1': 'learncode',
            'password2': 'learncode',
        }

        form = ExtendedUserCreationForm(data=form_info)
        self.assertTrue(form.is_valid())


# Have to use override becuase according to 
# https://stackoverflow.com/questions/44160666/valueerror-missing-staticfiles-manifest-entry-for-favicon-ico
# Having whitenoise gives a ValueError: Missing staticfiles manifest, so need it for testing
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class RegistrantsViewTest(TestCase):

    # Test a single page
    def test_single_page(self):
        response = self.client.get(reverse('sign-up-page'))
        self.assertEqual(response.status_code, 200)
