# Histórico de Alterações - AME Control

## [2026-01-23] - Melhorias no Cadastro de Usuários

### Alterado
- **Campo DRT**: Renomeado para "DRT/Matrícula" e agora aceita apenas números
- **Username**: Agora é exibido no formulário de cadastro (campo readonly) e é gerado automaticamente a partir do e-mail
- **Senha Padrão**: Todos os novos usuários são criados com a senha `ame-control`

### Como Atualizar

Se você já tem o sistema instalado, execute:

```bash
# 1. Atualize o código
git pull origin main

# 2. Aplique as migrações
python manage.py migrate

# 3. Reinicie o servidor
python manage.py runserver
```

### Detalhes das Mudanças

#### 1. Campo DRT/Matrícula
- **Antes**: Campo "DRT" que aceitava qualquer texto
- **Agora**: Campo "DRT/Matrícula" que aceita apenas números
- **Validação**: O sistema valida que apenas dígitos sejam inseridos

#### 2. Campo Username
- **Visibilidade**: Agora aparece no formulário de cadastro
- **Comportamento**: É preenchido automaticamente conforme o usuário digita o e-mail
- **Exemplo**: 
  - E-mail: `saulo.bastos@amecaragua.org.br`
  - Username gerado: `saulo.bastos`

#### 3. Senha Padrão
- **Senha**: `ame-control`
- **Primeiro Acesso**: O usuário será obrigado a trocar a senha no primeiro login
- **Segurança**: A senha é armazenada de forma criptografada no banco de dados

### Interface do Formulário

O formulário de cadastro agora inclui:
1. Nome Completo
2. E-mail
3. **Username (gerado automaticamente - readonly)**
4. CPF
5. DRT/Matrícula (apenas números)
6. Nível de Acesso (Tier)

### Card Informativo

Um novo card foi adicionado à lateral direita do formulário exibindo:
- **Senha Padrão**: `ame-control`
- Informação sobre troca obrigatória no primeiro acesso

---

## [2026-01-23] - Versão Inicial

### Adicionado
- Sistema de autenticação com login e logout
- Troca obrigatória de senha no primeiro acesso
- Sistema RBAC com 5 níveis (Tiers)
- Cadastro de usuários (Tier 3+)
- Cadastro de empresas (todos os usuários)
- Cadastro de médicos (todos os usuários)
- Dashboard com estatísticas
- Interface responsiva e corporativa
- CSS único centralizado
