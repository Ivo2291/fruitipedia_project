from django import forms

from fruitipedia_project.fruitipedia_app.models import ProfileModel, FruitModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['image_URL', 'age']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': '',
            'image_URL': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),

            'image_URL': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),

            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            ),
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': 'Name',
            'image_URL': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        exclude = ['nutrition']
        labels = {
            'name': 'Name',
            'image_URL': 'Image URL',
            'description': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_to_disable()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            return self.instance

    def __set_fields_to_disable(self):
        for field in self.fields.values():
            field.disabled = True


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['password', 'email']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_URL': 'Image URL',
            'age': 'Age',
        }
