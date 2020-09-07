from django import forms
from .models import Employee,Position

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname','emp_code','position','mobile') # '__all__'
        labels = {
           'fullname':'Full Name',
           'emp_code' : 'Employee Code',
           'position': 'Position',
           'mobile': 'Mobile'
        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ('title',)
        labels = {
            'title': 'Title'
        }
    def __init__(self,*args,**kwargs):
        super(PositionForm,self).__init__(*args,**kwargs)
