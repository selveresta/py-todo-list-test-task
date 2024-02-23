from django import forms
from .models import Todo, Tag

class TodoForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    deadline_datetime = forms.DateField(
        widget=forms.SelectDateWidget()
    )

    class Meta:
        model = Todo
        fields = ["content", "tags", "deadline_datetime"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class UpdateTagForm(forms.Form):
    name = forms.CharField(max_length=100)

    def __init__(self, name, *args, **kwargs):
        super(UpdateTagForm, self).__init__(*args, **kwargs)

        self.fields["name"].initial = name
