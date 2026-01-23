# AME Control

Sistema de controle corporativo com autenticação e controle de acesso baseado em funções (RBAC).

## Características

- Sistema de login com troca obrigatória de senha no primeiro acesso
- Controle de acesso baseado em 5 níveis (Tiers)
- Cadastro de usuários, empresas e médicos
- Interface responsiva e corporativa
- Desenvolvido em Django/Python

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/titonel/ame-control.git
cd ame-control
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

## Níveis de Acesso (RBAC)

- **Tier 1**: Usuários operacionais (inserção de dados)
- **Tier 2**: Analistas e líderes de setor
- **Tier 3**: Supervisores
- **Tier 4**: Coordenadores
- **Tier 5**: Gerentes e administradores do sistema

## Licença

Todos os direitos reservados.
