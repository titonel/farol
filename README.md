# Farol — Sistema de Gestão Integrada (AME Caraguatatuba)

Sistema corporativo unificado para o **AME Caraguatatuba** (SECONCI-SP / SUS-OSS), integrando o controle de acesso baseado em funções (RBAC), acompanhamento gráfico de produção, gestão de prestadores/contratos e extração automatizada de dados de PDFs.

O projeto atual unifica o sistema **Farol** original com o módulo de gestão de contratos e prestadores (`cadastro`).

---

## 🚀 Funcionalidades e Módulos

### 1. Núcleo Farol (Módulo Geral)
* **Autenticação Segura**: Login corporativo com troca obrigatória de senha no primeiro acesso.
* **Controle de Acesso (RBAC)**: Estrutura em 5 níveis (Tiers) para controle de permissões.
* **Cadastros Administrativos**: Cadastro de Usuários (Tier 3+) do sistema.
* **Dashboard Executivo**: Visão geral com métricas rápidas de cadastros, atalhos dinâmicos e controle integrado de contratos.

### 2. Módulo de Produção Mensal (Consolidado)
* **Importação via Planilha**: Upload de planilhas de produção de exames, cirurgias e serviços.
* **Interface Gráfica Interativa (Chart.js)**:
  * Gráfico de Ocupação comparando vagas ofertadas versus agendamentos realizados.
  * Gráfico horizontal de alerta de desperdício por especialidade (destacando taxas superiores a 15%).
  * KPIs calculados dinamicamente no navegador (Vagas, Agendamentos e Eficiência Global).

### 3. Módulo de Contratos & Prestadores
* **Importação e Leitura do SIRESP**:
  * Identificação automática de relatórios de Consultas e Exames/Cirurgias (HTML ou XLS).
  * Parser estruturado (`producao_siresp.py` e `producao_siresp_exames.py`) que processa agendas conhecidas e dados individuais por profissional.
* **Leitor Automático de Contratos PDF**:
  * Extração de dados cadastrais (CNPJ, Razão Social, endereço, representantes, vigências e valores mensais/globais) de PDFs no padrão SECONCI-SP utilizando `pdfplumber` e `PyMuPDF`.
  * Visualização estruturada para revisão e confirmação antes de gravar no banco de dados.
* **Relatório de Prestação de Contas**:
  * Emissão automática de planilha XLSX formatada por período (ciclo de apuração de 21 a 20).
* **Segurança Integrada**:
  * Todas as rotas do módulo de Contratos & Prestadores (`/prestadores/...`) são protegidas pelo decorator de autenticação e política de primeiro acesso do Farol.

### 4. Módulo Linhas de Cuidado (Hipertensão)
* **Importação & Integração**: Importado do sistema Linha de Cuidado de Hipertensão e integrado ao ecossistema global do Farol.
* **Gestão Clínica**: Prontuário eletrônico completo, controle pressórico, SOAP (Subjetivo, Objetivo, Avaliação e Plano), e avaliações multidisciplinares.
* **Prescrições & Receituários**: Geração e exportação em PDF de receitas médicas, kits de exames e termos de contrarreferência via `xhtml2pdf`.
* **Farmácia e REMUME Regionalizada**: Cadastro de medicamentos e controle da REMUME integrada (Litoral Norte e Paraibuna).
* **Indicadores Clínicos**: Dashboard interativo com gráficos (Chart.js) de controle pressórico, faixa etária, sexo e distribuição geográfica.
* **Autenticação Unificada**: Controle de acesso profissional (Médicos, Enfermeiros, Nutricionistas, Farmacêuticos) unificado com a base de usuários do Farol.

---

## 🎨 Identidade Visual e Experiência do Usuário (UI/UX)

* **Tema Farol**: Interface limpa e moderna utilizando a fonte **Inter** do Google Fonts, com paleta corporativa premium baseada em *Slate* (Slate-900 `#0f172a`, Slate-800 `#1e293b`), destaques em azul cobalto, sombras suaves, cantos arredondados (`12px`) e animações suaves (`fade-in`) nas transições de página.
* **Tema de Contratos**: Seção de contratos mantém a identidade visual quente ("Dia Ensolarado") baseada na paleta bronze/âmbar (`#FFBF00` e `#807040`) e fonte **Lato**, integrada à navegação global do sistema.
* **Módulo Hipertensão**: Totalmente remodelado para coincidir com a identidade do Farol, adotando os tons dark slate, a tipografia Inter, os estilos de cartões com cantos arredondados, realces de navegação ativos em azul cobalto e uso nativo dos ícones Bootstrap (substituindo ícones legados).

---

## 📂 Estrutura do Projeto Unificado

```
farol-project/
├── farol/                     # Configurações globais do projeto Django
├── core/                      # App principal (Autenticação, Usuários e Produção)
│   ├── models.py              # Modelos (Usuario, Cirurgia, Exame, etc.)
│   ├── views.py               # Lógica das views e dashboards
│   ├── forms.py               # Formulários
│   └── urls.py                # Rotas do Farol
├── cadastro/                  # App de Contratos (Prestadores, Contratos e Leitor PDF)
│   ├── models.py              # Modelos (Prestador, ContratoUpload, UploadProducao, etc.)
│   ├── views.py               # Lógica de Prestadores e PDF
│   ├── views_home.py          # Lógica de relatórios e SIRESP
│   ├── extrator.py            # Mapeador de dados PDF
│   ├── producao_siresp.py     # Parser de consultas
│   ├── producao_siresp_exames.py # Parser de cirurgias/exames
│   └── urls.py                # Rotas do módulo de Contratos
├── hipertensao/               # App de Linhas de Cuidado (Hipertensão)
│   ├── models.py              # Modelos (Paciente, Afericao, Atendimento, Medicamento)
│   ├── views.py               # Lógica clínica, dashboards e relatórios PDF
│   ├── forms.py               # Formulários de pacientes e fichas médicas
│   ├── decorators.py          # Controle de acesso por tipo profissional
│   ├── urls.py                # Rotas do módulo de Hipertensão
│   ├── templates/             # Fichas e prontuários da Linha de Cuidado
│   └── management/commands/   # Comandos de setup (setup_db para REMUME)
├── static/                    # Arquivos estáticos globais (CSS redesenhado, imagens)
├── templates/                 # Templates HTML globais do Farol
├── media/                     # Diretório de arquivos de contratos e planilhas enviadas
├── manage.py                  # Script de gerenciamento do Django
└── requirements.txt           # Dependências do sistema unificado
```

---

## 🛠️ Instalação e Configuração

### 1. Clonar o Repositório e Configurar Ambiente
```bash
git clone https://github.com/titonel/farol.git
cd farol
python -m venv .venv

# No Windows (PowerShell):
.venv\Scripts\Activate.ps1

# No Linux/Mac:
source .venv/bin/activate
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```
> **Nota:** Certifique-se de que dependências de processamento como `pandas`, `pdfplumber`, `PyMuPDF`, `lxml` e `cryptography` foram instaladas corretamente no ambiente virtual.

### 3. Rodar as Migrações do Banco de Dados
```bash
python manage.py migrate
```
As migrações criarão as tabelas tanto do Farol (`core`) quanto do módulo de Contratos (`cadastro`) no mesmo banco de dados SQLite.

### 4. Criar Superusuário (Administrador Tier 5)
```bash
python manage.py createsuperuser
```
Preencha o Nome, E-mail, DRT/Matrícula e Senha solicitados.

### 5. Configurar Dados Iniciais da REMUME (Hipertensão)
```bash
python manage.py setup_db
```
Este comando popula a farmácia do sistema com as dosagens e princípios ativos das REMUMEs de Caraguá, São Sebastião, Ilhabela, Ubatuba e Paraibuna.

### 6. Iniciar o Servidor
```bash
python manage.py runserver
```

Acesse o sistema em: **http://127.0.0.1:8000/**

---

## 🔑 Níveis de Acesso (RBAC)

* **Tier 1**: Usuário Operacional (Visualização básica de dados).
* **Tier 2**: Analista / Líder de Setor.
* **Tier 3**: Supervisor (Permissão para cadastrar novos usuários).
* **Tier 4**: Coordenador.
* **Tier 5**: Gerente / Administrador do Sistema (Acesso ao painel administrativo e tabelas SIGTAP).

---

## 📄 Licença

&copy; 2026, AME Caraguatatuba. Todos os direitos reservados.
