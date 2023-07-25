from django import forms
from django.forms import ModelForm
from .models import Manager

class ManagerForm(forms.ModelForm):  
    Start_Date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    End_Date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:  
        model = Manager
        fields = "__all__"  
        widgets = {
            'MemberId': forms.TextInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Group_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'etc': forms.TextInput(attrs={'class': 'form-control'})
            # Add any other fields with custom classes here
        }
        labels = {
            'MemberId': 'メンバーID',
            'Name': '名前',
            'Group_Name': 'グループ名',
            'etc': 'その他',
            'Start_Date': '開始日',
            'End_Date': '締め切日'
        }