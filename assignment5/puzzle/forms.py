from django import forms

class PuzzleForm(forms.Form):
    number = forms.IntegerField(
        label='Enter a Number',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., 1995'
        })
    )
    text = forms.CharField(
        label='Enter a Text Message',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., your name or secret word'
        })
    )