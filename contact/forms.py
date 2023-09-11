from django import forms
from contact.models import Contact
# from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    # email = forms.EmailField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'criado na classe',
    #         }
    #     ),
    #     label='Email',
    #     help_text='texto ajuda',
    # )

    # Duas formas para atualizar atributos dos campos dos fomrs
    # por meio do init da super classe ModelForm ou criaçao de um novo widget
    # para sobrescrever o widget antigo

    # acessando o init da super classe:
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['phone'].widget.attrs.update(
    #         {
    #             'placeholder': 'placeholder atualizado pelo init',
    #         }
    #     )

    # criando a classe meta
    class Meta:
        # escolhendo o model
        model = Contact
        # escolhendo os campos que vão aparecer no formulário
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )
        # criando um novo widget e substituindo o antigo
        widgets = {

            # escolhendo o campo e alterando o tipo de input
            'first_name': forms.TextInput(
                # selecionando os atributos do input que serão inseridos no
                # html do input
                attrs={
                    # adicionando classes no textarea do html que será gerado
                    'class': 'classe-a classe-b',
                    # alterando o placeholder no textarea do html
                    'placeholder': 'First Name',
                    'help_text': 'texto ajuda',

                }
            ),
        }

    def clean(self):

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro teste', code='invalid'
        #     )
        # )
        return super().clean()

    # def clean_first_name(self):
    #     cleaned_data = self.cleaned_data.get('first_name')
    #     if cleaned_data == 'aaa':
    #         raise ValidationError(f'nome inaprópriado ({cleaned_data})')

    #     return cleaned_data
