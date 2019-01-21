from django import forms

class WriteForm(forms.Form):
	title=forms.CharField(max_length=50,
		widget=forms.TextInput(attrs={'id':'fname','placeholder':'story title...!'}))
	brief=forms.CharField(max_length=150,
		widget=forms.TextInput(attrs={'id':'lname','placeholder':'small description about story ...!'}))
	description=forms.CharField(widget=forms.Textarea(attrs={'id':'subject','placeholder':'write your story here...!'}))