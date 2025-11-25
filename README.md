# dsii-Lucas-Cruz

Aula de Desenvolvimento de Sistemas ministrada pelo Professor Roberto Itai

  

# Aula 01 de PYTHON

  

Algoritimo de apresentação de dos comandos de print e input.

  

# Aula 05 de PYTHON

  

Arquivo lista []

  

lista = []

  

obs: o índice começa pelo 0, exemplo:

  

>       0 1 2 3 4

lista = [1, 2, 3, 4.0, 'cinco']

  

>           0 1 2  0 1 2
> 
> lista = [[1, 2, 3],[4, 5, 6]] ------> print(lista[1][1])
> 
>            0       0



# 25/11

# AtividadeGráfica - Sistema de Cadastro com Interface Gráfica

Sistema de cadastro de pessoas desenvolvido em Python utilizando a biblioteca Tkinter para interface gráfica.

## Descrição

Aplicação desktop com interface gráfica que permite cadastrar, listar e gerenciar informações de pessoas. O sistema armazena os dados em memória durante a execução.

## Funcionalidades

- **Cadastro de Pessoas**: Formulário com validação de campos
- **Campos do Formulário**:
  - Nome (obrigatório)
  - Sobrenome (obrigatório)
  - Idade (obrigatório, apenas números entre 0-150)
  - Sexo (obrigatório, opções: Masculino/Feminino)
- **Listagem**: Visualização de todos os cadastros realizados em uma janela separada
- **Limpeza**: Botão para limpar os campos do formulário
- **Validações**: Sistema completo de validação de dados antes do cadastro
- **Mensagens**: Feedback visual com mensagens de sucesso e avisos

## Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: Biblioteca padrão para interface gráfica

## Como Executar

```bash
cd AtividadeGráfica
python cadastro.py
```

## Estrutura do Código

### Classe SistemaCadastro

Classe principal que gerencia toda a aplicação.

**Métodos:**

- `__init__(self, root)`: Inicializa a interface gráfica e componentes
- `validar_campos(self)`: Valida todos os campos do formulário antes de cadastrar
- `cadastrar(self)`: Realiza o cadastro de uma nova pessoa
- `listar(self)`: Exibe todos os cadastros em uma janela separada
- `limpar(self)`: Limpa todos os campos do formulário

### Componentes da Interface

- **Labels**: Identificação dos campos
- **Entry**: Campos de texto para Nome, Sobrenome e Idade
- **Radiobutton**: Seleção de sexo
- **Buttons**: Botões de ação (Cadastrar, Listar, Limpar)
- **Toplevel**: Janela secundária para listagem

## Validações Implementadas

1. Verificação de campos vazios
2. Validação de idade (apenas números inteiros)
3. Validação de intervalo de idade (0-150)
4. Verificação de seleção de sexo
5. Remoção de espaços em branco extras

## Armazenamento

Os dados são armazenados em uma lista (self.cadastros) durante a execução do programa. Cada cadastro é um dicionário com as seguintes chaves:
- nome
- sobrenome
- idade
- sexo

## Interface Visual

- Layout organizado com grid e pack
- Cores nos botões para melhor identificação visual
- Janela de tamanho fixo (400x350)
- Feedback de status após cada ação
- Scrollbar na janela de listagem para múltiplos cadastros
