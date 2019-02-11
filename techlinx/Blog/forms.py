from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'text')

#    def clean_email(self):
#        email = self.cleaned_data.get("email")
#        email_base, proveedor = email.split("@")
#        dominio, extension = proveedor.split(".")
#        if not extension == "com":
#            raise  forms.ValidationError("Por favor utilice un email con la extension .com")

#            return email
