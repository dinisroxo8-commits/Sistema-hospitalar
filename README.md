# 📚 Coleção de Projetos Python - Sistemas de Gestão

**Autor:** [Dinis dos Santos Roxo]  
**Curso:** 10º Ano - Programação  
**Data:** Janeiro 2026

---

## 📋 Índice

1. [Introdução](#introdução)
2. [Requisitos](#requisitos)
3. [Projetos Incluídos](#projetos-incluídos)
   - [Sistema Escolar - Gestão de Alunos](#1-sistema-escolar---gestão-de-alunos)
   - [Cantina Escolar - Sistema de Reservas](#2-cantina-escolar---sistema-de-reservas)
   - [Missão Escape Room](#3-missão-escape-room)
   - [Sistema Hospitalar](#4-sistema-hospitalar)
4. [Como Executar](#como-executar)
5. [Funcionalidades Técnicas](#funcionalidades-técnicas)
6. [Conclusão](#conclusão)

---

## 🎯 Introdução

Este repositório contém **quatro projetos Python** desenvolvidos como parte do curso de Programação. Cada projeto demonstra competências diferentes em programação, incluindo manipulação de estruturas de dados, validação de inputs, controlo de fluxo e organização de código.

Os sistemas foram desenvolvidos com foco em:
- ✅ Facilidade de utilização
- ✅ Validação robusta de dados
- ✅ Código limpo e organizado
- ✅ Interface de consola intuitiva

---

## 💻 Requisitos

### Software Necessário
- **Python 3.7+** (recomendado: Python 3.10 ou superior)
- Sistema Operativo: Windows, Linux ou macOS

### Bibliotecas Utilizadas
Todos os projetos utilizam apenas bibliotecas padrão do Python:
- `os` - Limpeza de ecrã e operações do sistema
- `statistics` - Cálculos estatísticos (médias)
- `random` - Geração de números e escolhas aleatórias
- `datetime` - Validação e manipulação de datas

**Não são necessárias instalações adicionais!**

---

## 📁 Projetos Incluídos

### 1. Sistema Escolar - Gestão de Alunos

#### 📝 Descrição
Sistema completo para gerir alunos e as suas notas escolares, com cálculo automático de médias individuais e da turma.

#### ⚙️ Funcionalidades
- **Cadastrar aluno** - Registo com código automático e 3 notas
- **Listar alunos** - Visualização de todos os alunos com notas e médias
- **Mostrar médias** - Médias individuais e média geral da turma
- **Eliminar aluno** - Remoção com confirmação de segurança
- **Sistema de códigos** - Atribuição automática de códigos únicos

#### 🔑 Características Técnicas
- Gestão automática de códigos (preenchimento de lacunas)
- Validação de entrada de notas (apenas números)
- Cálculo de médias com biblioteca `statistics`
- Confirmação antes de eliminar

#### 💡 Exemplo de Uso
```
1 - Cadastrar aluno
Nome: João Silva
1ª Nota: 15.5
2ª Nota: 17.0
3ª Nota: 16.5
✓ Aluno cadastrado com código 1
```

---

### 2. Cantina Escolar - Sistema de Reservas

#### 📝 Descrição
Sistema avançado de gestão de reservas para cantina escolar, com ementa variada, controlo de duplicados e emissão de faturas mensais.

#### ⚙️ Funcionalidades
- **Cadastrar aluno** - Registo com validação de nome e código (1-9999)
- **Listar alunos** - Visualização de todos os alunos cadastrados
- **Mostrar ementa** - Listagem de pratos e bebidas com preços
- **Fazer reserva** - Sistema completo de marcação de almoços
- **Listar reservas** - Consulta de reservas por aluno
- **Fatura mensal** - Relatório mensal com total a pagar
- **Cancelar reserva** - Remoção com confirmação

#### 🍽️ Ementa Disponível

**Pratos:**
- Arroz de pato (3.50€)
- Bacalhau à brás (4.00€)
- Frango assado (3.20€)
- Lasanha (3.80€)
- Empadão (3.60€)

**Bebidas:**
- Água (0.50€)
- Sumo (1.00€)
- Leite (0.80€)
- Refrigerante (1.20€)

#### 🔑 Características Técnicas
- **Validação de nomes** - Mínimo 3 caracteres, apenas letras
- **Validação de códigos** - Números entre 1-9999
- **Validação de datas** - Formato dd/mm/aaaa com verificação de datas reais
- **Detecção de anos bissextos** - Para validação correta de fevereiro
- **Prevenção de duplicados** - Um aluno não pode ter duas reservas no mesmo dia
- **Cálculo automático** - Soma de prato + bebida

#### 💡 Exemplo de Uso
```
✅ RESERVA EFETUADA COM SUCESSO!
Aluno: Maria Santos
Data: 23/01/2026
Prato: Bacalhau à brás (4.00€)
Bebida: Sumo (1.00€)
TOTAL: 5.00€
```

---

### 3. Missão Escape Room

#### 📝 Descrição
Jogo interativo educacional que combina desafios de programação, matemática e lógica num ambiente de Escape Room virtual.

#### 🎮 Funcionalidades
- **Jogar desafio** - Três tipos de desafios disponíveis
- **Loja** - Sistema de compra de itens com moedas
- **Estado do jogador** - Visualização de estatísticas
- **Missões** - Sistema de objetivos com recompensas
- **Relatório final** - Resumo completo da partida

#### 🎯 Desafios Disponíveis

**1. Matemática Rápida**
- Operações básicas (+, -, ×)
- Números aleatórios entre 2-12
- Resposta imediata

**2. Quiz Python**
- Perguntas sobre conceitos de programação
- Temas: tipos de dados, estruturas, ciclos
- Normalização de respostas (ignora acentos)

**3. Palavra Secreta**
- Adivinhar palavra com 4 tentativas
- Dicas: primeira letra e tamanho
- Palavras relacionadas com programação

#### 🛒 Itens da Loja
- **Lanterna** (4 moedas) - Ajuda a ver pistas melhor
- **Chave** (6 moedas) - Desbloqueia porta extra
- **Mapa** (3 moedas) - Mostra progresso
- **Café** (2 moedas) - Recupera energia (+3)

#### 🏆 Sistema de Missões
1. Vencer 2 desafios → 5 moedas
2. Comprar 1 item na loja → 3 moedas
3. Ganhar 10 moedas no total → 5 moedas

#### 🔑 Características Técnicas
- Sistema de energia (cada desafio consome 1)
- Moedas aleatórias por vitória (2-5)
- Histórico de eventos completo
- Validação de nomes (apenas letras)
- Inventário dinâmico
- Verificação automática de missões

#### 💡 Mecânica de Jogo
```
⚡ Energia: 10 → Cada desafio consome 1
🪙 Moedas: 5 (iniciais) → Ganhas 2-5 por vitória
🏆 Objetivo: Completar as 3 missões
```

---

### 4. Sistema Hospitalar

#### 📝 Descrição
Sistema completo de gestão hospitalar para pacientes e consultas, com controlo de estados e reorganização automática de IDs.

#### ⚙️ Funcionalidades
- **Cadastrar paciente** - Registo com ID automático
- **Listar pacientes** - Visualização de todos os pacientes
- **Marcar consulta** - Agendamento com data, hora e tipo
- **Listar consultas** - Todas as consultas do sistema
- **Consultas de paciente** - Filtro por paciente específico
- **Próxima consulta** - Mostra próxima consulta agendada
- **Alterar estado** - Mudar entre agendada/realizada/cancelada
- **Eliminar paciente** - Remoção com reorganização de IDs

#### 📊 Estados de Consulta
1. **Agendada** - Consulta marcada e pendente
2. **Realizada** - Consulta já efetuada
3. **Cancelada** - Consulta cancelada

#### 🔑 Características Técnicas
- **IDs automáticos** - Geração sequencial com preenchimento de lacunas
- **Reorganização de IDs** - Após eliminação, mantém IDs sequenciais
- **Relacionamento de dados** - Ligação entre pacientes e consultas
- **Filtros inteligentes** - Apenas pacientes com consultas em certas funções
- **Validação de inputs** - Verificação de IDs e opções

#### 📋 Dados Armazenados

**Paciente:**
- ID (gerado automaticamente)
- Nome
- Idade
- Contacto

**Consulta:**
- ID do paciente
- Data (dd/mm/aaaa)
- Hora (hh:mm)
- Tipo de consulta
- Estado (agendada/realizada/cancelada)

#### 💡 Exemplo de Uso
```
Paciente: António Costa
Idade: 45
Contacto: 912345678
✓ Paciente cadastrado com ID 1

Consulta marcada:
Data: 25/01/2026
Hora: 14:30
Tipo: Cardiologia
Estado: Agendada
```

---

## 🚀 Como Executar

### Passo 1: Verificar Instalação do Python
```bash
python --version
```
ou
```bash
python3 --version
```

### Passo 2: Executar um Projeto

**No Windows:**
```bash
python nome_do_ficheiro.py
```

**No Linux/macOS:**
```bash
python3 nome_do_ficheiro.py
```

### Passo 3: Seguir as Instruções no Ecrã
Cada programa apresenta um menu interativo. Basta escolher a opção desejada digitando o número correspondente.

### 🛑 Para Sair
- Escolher a opção "Sair" no menu
- Ou pressionar `Ctrl + C` para forçar encerramento

---

## 🔧 Funcionalidades Técnicas

### Estruturas de Dados Utilizadas

#### Listas
```python
alunos = []           # Lista de dicionários
pacientes = []        # Armazenamento dinâmico
reservas = []         # Coleção de reservas
```

#### Dicionários
```python
aluno = {
    'codigo': 1,
    'nome': 'João Silva',
    'notas': [15.5, 17.0, 16.5]
}
```

### Funções Principais

#### Validação
- `validar_nome()` - Verifica se nome tem apenas letras
- `validar_codigo()` - Garante código entre 1-9999
- `validar_data()` - Valida formato e existência de data
- `validar_mes_ano()` - Valida mês (1-12) e ano (2024-2030)

#### Gestão
- `limpar()` / `limpar_tela()` - Limpa o ecrã (compatível Windows/Linux)
- `buscar_aluno()` / `buscar_paciente()` - Procura por ID
- `obter_proximo_codigo()` - Gera IDs únicos automaticamente

#### Cálculos
- `statistics.mean()` - Calcula médias
- `random.randint()` - Gera números aleatórios
- `random.choice()` - Escolha aleatória de listas

### Técnicas de Programação

✅ **Modularização** - Código organizado em funções  
✅ **Validação robusta** - Verificação de todos os inputs  
✅ **Estruturas de dados** - Listas e dicionários aninhados  
✅ **Controlo de fluxo** - if/elif/else, while, for  
✅ **List comprehensions** - Filtragem eficiente de dados  
✅ **Tratamento de erros** - try/except para inputs inválidos  
✅ **Interface limpa** - Limpeza de ecrã e formatação  

---

## 📈 Competências Demonstradas

### Programação Básica
- ✓ Variáveis e tipos de dados
- ✓ Operadores aritméticos e lógicos
- ✓ Estruturas condicionais (if/else)
- ✓ Ciclos (while/for)

### Programação Intermédia
- ✓ Funções e parâmetros
- ✓ Listas e dicionários
- ✓ Manipulação de strings
- ✓ Módulos e imports

### Programação Avançada
- ✓ Estruturas de dados complexas
- ✓ List comprehensions
- ✓ Validação de dados
- ✓ Gestão de estados
- ✓ Algoritmos de procura

### Boas Práticas
- ✓ Código limpo e legível
- ✓ Comentários explicativos
- ✓ Nomes descritivos
- ✓ Modularização
- ✓ Interface user-friendly

---

## 🎓 Conclusão

Esta coleção de projetos demonstra uma progressão clara no domínio de Python, desde sistemas básicos de gestão até jogos interativos complexos. Cada projeto aplica conceitos fundamentais de programação de forma prática e útil.

### Objetivos Alcançados
✅ Criação de sistemas funcionais e completos  
✅ Implementação de validação robusta de dados  
✅ Utilização eficaz de estruturas de dados  
✅ Desenvolvimento de interfaces intuitivas  
✅ Aplicação de boas práticas de programação  
