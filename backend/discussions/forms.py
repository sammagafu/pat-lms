from django import forms

class TopicForm(forms.Form):
    category = forms.CharField(label='category name')
    content = forms.CharField(widget=forms.Textarea)
