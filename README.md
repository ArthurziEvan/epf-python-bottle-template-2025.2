# Projeto Template: POO com Python + Bottle + JSON

Este é um projeto de template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.


## 💡 Descrição do Projeto

O projeto se baseia em um um sorteador de amigo oculto, baseado em aplicações web orientadas a objetos com Python, a aplicação é responsável por cadastrar e sortear as pessoas numa sala de amigo oculto e sorteá-las e enviar o resultado por email

---

## 🗂 Estrutura de Pastas

```bash

poo-python-bottle-template/
├── app.py # Ponto de entrada do sistema
├── config.py # Configurações e caminhos do projeto
├── main.py # Inicialização da aplicação
├── requirements.txt 
├── README.md 
├── Makefile
├── .gitignore
├── .pylintrc
|
├── controllers/ # Controladores
│   ├── __pycache__
│   ├── __init__.py
│   ├── base_controller.py
│   ├── home_controller.py
│   ├── room_controller.py
│   └── user_controller.py
|
├── data/ # Armazenamento de Dados 
│   ├── session_locks
│   ├── sessions
│   ├── rooms.json
│   └── users.json
|
├── models/ # (Modelos de Dados e Entidades)
│   ├── __pycache__
│   ├── room.py
│   └── user.py
|
├── services/ # Camada de Serviço (Lógica de Negócio) - Contém regras de senha, sorteio de salas
│   ├── __pycache__
│   ├── auth_service.py
│   ├── room_service.py
│   └── user_service.py
|
├── static/ # Arquivos Estáticos
│   ├── css/
│   │   ├── helper.css
│   │   └── style.css
│   ├── html/
│   │   └── email.html
│   ├── img/
│   │   └── BottleLogo.png
│   └── js/
│       ├── helper.js
│       ├── main.js
│       └── util.js
|
├── views/ # Parte do  HTML.
│   ├── helper-final.tpl
│   ├── home.tpl
│   ├── join_room.tpl
│   ├── layout.tpl
│   ├── login.tpl
│   ├── room_form.tpl
│   ├── room.tpl
│   ├── rooms.tpl
│   ├── user_form.tpl
│   ├── users.tpl
│   ├── .gitignore
│   └── .pylintrc
|
└── venv/ # Ambiente Virtual Python
    ├── Include
    ├── Lib
    ├── Scripts
    └── pyvenv.cfg

---
```
## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.
- `home_controller.py`: gerencia a página inicial.
- `room_controller.py`:gerencia as salas de amigo oculto, seus membros e o envio de e-mails.

### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- `user.py`: classe `User`, com atributos como `id`, `name`, `email`, etc.
- `room.py`: define a estrutura da sala e gerencia o armazenamento

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON. Exemplo:
- `user_service.py`: encapsula toda a lógica de negócios relacionada a usuários.
- `auth_service.py`:fornece funções utilitárias para gerenciar o estado de login do usuário
- `room_service.py`:encapsula a lógica de negócios relacionada às salas de amigo oculto.

### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
- `layout.tpl`: estrutura base com navegação e bloco `content`.
- `users.tpl`: lista os usuários.
- `user_form.tpl`: formulário para adicionar/editar usuário.
-  `home.tpl`: página inicial com links de atalho
-  `login.tpl`: formulário para autenticação do usuário.
-  `join_room.tpl`: formulário para entrar em uma sala
-  `room.tpl`: visualização de sala.
-  `room_form.tpl`: permite criar um novo grupo ou editar o nome de um grupo existente
-  `users.tpl`: exibe uma tabela de todos os usuários registrados

### `static/`
Arquivos estáticos como:
- `css/style.css`: estilos básicos.
- `js/main.js`: scripts JS opcionais.
- `img/BottleLogo.png`: exemplo de imagem.
- `email.html`: Estrutura do email enviado 


### `data/`
Armazena os arquivos `.json` que simulam o banco de dados:
- `users.json`: onde os dados dos usuários são persistidos.
- `rooms.json`:onde os dados das salas são persistidos
---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Personalização
Para adicionar novos modelos (ex: Atividades):

1. Crie a classe no diretório **models/**.

2. Crie o service correspondente para manipulação do JSON.

3. Crie o controller com as rotas.

4. Crie as views .tpl associadas.

---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
