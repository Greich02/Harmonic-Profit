from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}))
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    referredBy = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Referred by', 'id':'ref'}))
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegisterForm, self).__init__(*args, **kwargs)
    
class ApplyForm(forms.Form):
    useLastNameFirstName = forms.MultipleChoiceField()
    removeUsername = forms.MultipleChoiceField()
    changeGender = forms.MultipleChoiceField()
    
    
    
    