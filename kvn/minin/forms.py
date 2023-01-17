from django import forms
from .models import *
from django.forms import ModelForm, TextInput

class ComandForm(ModelForm):
    class Meta:
      model = Comand
      fields = ['first_evaluation', 'second_appreciation', 'third_assessment', 'fourth_assessment', 'fifth_assessment']

      widjets = {
          'first_evaluation': TextInput(attrs={
             'class': 'form-control',
              'label': 'Оценка первого судьи'
          }),
          'second_appreciation': TextInput(attrs={
             'class': 'form-control',
          }),
          'third_assessment': TextInput(attrs={
             'class': 'form-control',
          }),
          'fourth_assessment': TextInput(attrs={
             'class': 'form-control',
          }),
          'fifth_assessment': TextInput(attrs={
             'class': 'form-control',
          }),
      }