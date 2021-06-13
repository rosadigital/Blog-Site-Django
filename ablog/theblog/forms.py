from django import forms
from .models import Post, Categories, Comment

choices = Categories.objects.all().values_list('name', 'name')

choice_list = []

for element in choices:
    choice_list.append(element)

print(choice_list)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title',}),

            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title tag',}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id': 'username', "type": "hidden"}),
            # 'author': forms.Select(attrs={'class': 'form-control', }),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', }),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Content',}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title',}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title tag',}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Content',}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'body': forms.Textarea(attrs={'class': 'form-control',}),

        }