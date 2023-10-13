from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model() # vozvr polzovatel kot propisan v nastrojkah, kotorie pereopredelili AUTH_USER_MODEL
#propisali tam svoego polzovatelja, a ne djangovsk

#dlja pereopredelenija polzovatela (unasleduemsja ot bazovogo klassa)
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
          label=_("Email"),
          max_length=254,
          widget=forms.EmailInput(attrs={"autocomplete": "email"}),
     )
    
    class Meta(UserCreationForm.Meta): #toze unasleduem
        model = User #nah polzovatel
        fields = ("username", "email")
