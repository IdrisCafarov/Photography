from django import forms
from .models import *
from django.forms import ModelForm


class BookForm(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={

        
        'type': 'text',



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={

        
        'type': 'email',

    }
    ))

    number = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={

        
        'type': 'number',
    }))

    book_date = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={

        "autocomplete":"off",
        "placeholder":"",
        "type":"text",
        "name":"checkIn",
        "id":"datepicker",
        "class":"claender",
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        


    }))

    class Meta:
        model = Booking
        fields = ('name', 'email', 'number', 'book_date','message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class MessageForm(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={


        'type': 'email',

    }
    ))


    message = forms.CharField(widget=forms.Textarea(attrs={



    }))

    class Meta:
        model = Message
        fields = ('name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
