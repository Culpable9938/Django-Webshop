from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  User, CartItem, Order

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2']


class CartItemForm(UserCreationForm):
    class Meta:
        model = CartItem
        fields = '__all__'

class EditProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'Country', 'Address', 'phonenumber', 'avatar']
