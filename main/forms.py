from django.forms import ModelForm
from customer.models import Customer
from django.core.exceptions import ValidationError

class Feedback(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName', 'phone']




    # def clean(self):
    #     phone = self.cleaned_data['phone']
    #     if Customer.objects.filter(phone=phone).exists():
    #         raise forms.ValidationError('duplicate_phone')
    #     return phone


    # def clean_phone(self):
    #     # Get the phone
    #     phone = self.cleaned_data.get('phone')

    #     # Check phone.
    #     try:
    #         match = Customer.objects.get(phone=phone)
    #     except Customer.DoesNotExist:
    #         # Unable to find a phone, this is fine
    #         return phone

    #     # A user was found with this as a phone, raise an error.
    #     raise forms.ValidationError('This phone is already in use.')
        