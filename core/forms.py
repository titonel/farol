from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from .models import Usuario, Empresa, Medico, Cirurgia, Exame, ServicoMedico
import csv
import io


class LoginForm(forms.Form):
    """Formulário de login."""
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu usuário',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )


class TrocaSenhaForm(PasswordChangeForm):
    """Formulário para troca de senha no primeiro acesso."""
    old_password = forms.CharField(
        label='Senha Atual',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a senha atual'
        })
    )
    new_password1 = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a nova senha'
        })
    )
    new_password2 = forms.CharField(
        label='Confirme a Nova Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme a nova senha'
        })
    )


class UsuarioForm(forms.ModelForm):
    """Formulário para cadastro de usuários."""
    username_display = forms.CharField(
        label='Username (gerado automaticamente)',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'id': 'username_display',
            'placeholder': 'Será gerado após digitar o e-mail'
        }),
        help_text='O username será a parte do e-mail antes do @'
    )
    
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'cpf', 'drt', 'tier']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email_field'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00'
            }),
            'drt': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apenas números'
            }),
            'tier': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError('Já existe um usuário com este e-mail.')
        return email
    
    def clean_drt(self):
        drt = self.cleaned_data.get('drt')
        if drt and not drt.isdigit():
            raise ValidationError('DRT/Matrícula deve conter apenas números.')
        return drt
    
    def save(self, commit=True):
        usuario = super().save(commit=False)
        # Gera o username a partir do email
        usuario.username = self.cleaned_data['email'].split('@')[0]
        # Define a senha padrão
        usuario.set_password('ame-control')
        usuario.primeiro_acesso = True
        if commit:
            usuario.save()
        return usuario


class EmpresaForm(forms.ModelForm):
    """Formulário para cadastro de empresas."""
    
    class Meta:
        model = Empresa
        fields = [
            'razao_social', 'nome_fantasia', 'cnpj',
            'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado',
            'telefone', 'email', 'ativa'
        ]
        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00.000.000/0000-00'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000',
                'id': 'cep_field'
            }),
            'logradouro': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'logradouro_field',
                'placeholder': 'Rua, Avenida, etc.'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'numero_field',
                'placeholder': 'Número'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'complemento_field',
                'placeholder': 'Apto, Sala, Bloco, etc.'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'bairro_field',
                'placeholder': 'Bairro'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'cidade_field',
                'placeholder': 'Cidade'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'estado_field',
                'placeholder': 'UF (ex: SP)',
                'maxlength': '2',
                'style': 'text-transform: uppercase;'
            }),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'ativa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class MedicoForm(forms.ModelForm):
    """Formulário para cadastro de médicos."""
    
    class Meta:
        model = Medico
        fields = ['nome_completo', 'crm', 'cpf', 'especialidade', 'telefone', 'email', 'ativo']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'crm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: CRM/SP 123456'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00'
            }),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CirurgiaForm(forms.ModelForm):
    """Formulário para cadastro manual de cirurgias."""
    
    class Meta:
        model = Cirurgia
        fields = ['codigo_sigtap', 'descricao', 'valor', 'tipo_cirurgia', 'especialidade', 'ativa']
        widgets = {
            'codigo_sigtap': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'codigo_sigtap_field',
                'placeholder': 'Ex: 0401010019'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'descricao_field',
                'rows': 3,
                'placeholder': 'Descrição completa do procedimento'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'valor_field',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'tipo_cirurgia': forms.Select(attrs={
                'class': 'form-select',
                'id': 'tipo_cirurgia_field'
            }),
            'especialidade': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'especialidade_field',
                'placeholder': 'Ex: Cirurgia Geral'
            }),
            'ativa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CirurgiaCSVUploadForm(forms.Form):
    """Formulário para upload de arquivo CSV com cirurgias."""
    
    arquivo_csv = forms.FileField(
        label='Arquivo CSV',
        help_text='Selecione um arquivo CSV codificado em UTF-8',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.csv'
        })
    )
    
    sobrescrever = forms.BooleanField(
        label='Sobrescrever registros existentes',
        required=False,
        initial=False,
        help_text='Se marcado, irá atualizar cirurgias com código SIGTAP já cadastrado',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    def clean_arquivo_csv(self):
        arquivo = self.cleaned_data.get('arquivo_csv')
        
        if not arquivo:
            raise ValidationError('Nenhum arquivo foi enviado.')
        
        if not arquivo.name.endswith('.csv'):
            raise ValidationError('O arquivo deve ter extensão .csv')
        
        # Valida tamanho do arquivo (máximo 5MB)
        if arquivo.size > 5 * 1024 * 1024:
            raise ValidationError('O arquivo é muito grande. Tamanho máximo: 5MB')
        
        # Tenta ler o arquivo como CSV UTF-8
        try:
            arquivo.seek(0)
            conteudo = arquivo.read().decode('utf-8')
            leitor = csv.DictReader(io.StringIO(conteudo))
            
            # Verifica se as colunas necessárias existem
            colunas_necessarias = ['Codigo SIGTAP', 'Descricao', 'Valor', 'Tipo Cirurgia', 'Especialidade']
            colunas_arquivo = [col.strip() for col in leitor.fieldnames] if leitor.fieldnames else []
            
            # Aceita variações de nome de colunas
            colunas_variadas = {
                'Codigo SIGTAP': ['codigo sigtap', 'código sigtap', 'codigo', 'código', 'sigtap'],
                'Descricao': ['descricao', 'descriçao', 'descrição', 'procedimento'],
                'Valor': ['valor', 'preço', 'preco'],
                'Tipo Cirurgia': ['tipo cirurgia', 'tipo', 'categoria'],
                'Especialidade': ['especialidade', 'especialidade medica', 'especialidade médica']
            }
            
            colunas_encontradas = {}
            for col_necessaria, variacoes in colunas_variadas.items():
                encontrou = False
                for col_arquivo in colunas_arquivo:
                    if col_arquivo.lower() in variacoes:
                        colunas_encontradas[col_necessaria] = col_arquivo
                        encontrou = True
                        break
                if not encontrou:
                    raise ValidationError(
                        f'Coluna "{col_necessaria}" não encontrada no CSV. '
                        f'Colunas disponíveis: {", ".join(colunas_arquivo)}'
                    )
            
            # Reseta o ponteiro do arquivo
            arquivo.seek(0)
            
        except UnicodeDecodeError:
            raise ValidationError(
                'Erro ao decodificar o arquivo. '
                'Certifique-se de que o arquivo está codificado em UTF-8.'
            )
        except csv.Error as e:
            raise ValidationError(f'Erro ao ler o arquivo CSV: {str(e)}')
        
        return arquivo


class ExameForm(forms.ModelForm):
    """Formulário para cadastro de exames."""
    
    class Meta:
        model = Exame
        fields = ['codigo_sigtap', 'descricao', 'valor', 'tipo_exame', 'preparo', 'ativo']
        widgets = {
            'codigo_sigtap': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipo_exame': forms.Select(attrs={'class': 'form-select'}),
            'preparo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ServicoMedicoForm(forms.ModelForm):
    """Formulário para cadastro de serviços médicos."""
    
    class Meta:
        model = ServicoMedico
        fields = ['codigo_sigtap', 'descricao', 'valor', 'tipo_servico', 'especialidade', 'duracao_minutos', 'ativo']
        widgets = {
            'codigo_sigtap': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipo_servico': forms.Select(attrs={'class': 'form-select'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
            'duracao_minutos': forms.NumberInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
