# universalUser

O objetivo deste projeto é criar servidor de "usuário universal", onde com ele sera possível ser integrado em todos os canais da empresa para que o cliente tenha a mesma conta e histórico independente do canal que ela acesse, seguindo o conceito Omnichannel.

## Como instalar e rodar? 🚀

Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

`# Este passo é para baixar o projeto`
```bash
git clone https://github.com/<your_user>/universalUser.git
```
Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

`# Entrar na pasta`

```bash
cd e2-kanvas
```

`# Criar um ambiente virtual`

```bash
python3 -m venv venv
```

`# Entrar no ambiente virtual`

```bash
source venv/bin/activate
```

Então, para instalar as dependências, basta:

```bash
pip install -r requirements.txt
```

Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:

```bash
./manage.py migrate
```

Então, para rodar, basta digitar o seguinte, no terminal:

```bash
./manage.py runserver
```

E o sistema estará rodando em http://127.0.0.1:8000

## Utilização 🖥️

Para utilizar este sistema, é necessário utilizar um web browser.

## Rotas:

### Sobre Usuários:

**POST** /api/account/

Cria um novo usuário.

Insira os dados no formulário corretamente e click em “Enviar”

Sobre Autenticação:

A API funcionará com autenticação baseada em token.

**POST** /api/login/

fazendo login (serve para qualquer tipo de usuário):

Insira seu nome de usuário e senha nos campos corretamente.

Se estiver tudo certo recebera um token que sera usado posteriormente

### Observação:

`Este projeto não esta com o MVP finalizado.`
