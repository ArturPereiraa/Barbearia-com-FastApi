# Projeto de Agendamento de Barbearia

Este é um projeto de exemplo para um simples sistema de agendamento de barbearia utilizando FastAPI e SQLAlchemy.

## Pré-requisitos

[python](https://www.python.org/downloads/)

### Bibliotecas necessárias
Para Instalar as bibliotecas necessárias, use o seguinte comando ápos fazer o clone do repositório para sua máquina

```bash
pip install -r requirements.txt
```

## Como rodar o projeto

1. **Clone o repositório:**

 ```bash
git clone https://github.com/ArturPereiraa/Barbearia-com-FastApi.git

cd Barbearia-com-FastApi
```

2.  Execute app.py:
```bash
python app.py
```

**Acesso à Aplicação:**

O servidor FastAPI será iniciado e estará acessível em http://localhost:8000.

A documentação se encontra em:

   [http://localhost:8000/docs](http://localhost:8000/docs)

## Funcionalidades

Este projeto utiliza o FastAPI para criar uma aplicação web para uma barbearia, oferecendo as seguintes funcionalidades principais:

1. **Cadastro de Usuário:**
   - Permite que novos usuários se cadastrem fornecendo nome, email e senha.
   - Verifica se o email já está em uso antes de cadastrar.

2. **Login e Logout:**
   - Usuários podem realizar login fornecendo email e senha.
   - Mantém a sessão do usuário ativa até o logout.
   - Permite que o usuário faça logout, encerrando a sessão.

3. **Agendamento de Serviços:**
   - Usuários autenticados podem agendar serviços (como cortes de cabelo) especificando nome, data e hora.
   - Verifica se a data e hora fornecidas estão no formato correto.
   - Os agendamentos são associados ao usuário que os criou.

4. **Visualização e Edição de Agendamentos:**
   - Usuários podem visualizar todos os agendamentos que criaram.
   - Permite a edição da data e hora dos agendamentos existentes.
   - Verifica se o agendamento existe antes de editar.

5. **Cancelamento de Agendamentos:**
   - Usuários podem cancelar agendamentos existentes.
   - Verifica se o agendamento existe antes de cancelar.

6. **Visualização de Cortes Disponíveis:**
   - Exibe uma lista de cortes de cabelo disponíveis para os clientes.

7. **Perfil do Usuário:**
   - Exibe informações do usuário como nome e email.
   - Apenas usuários autenticados podem acessar seu perfil.

8. **Arquivos Estáticos e Templates Dinâmicos:**
   - Utiliza arquivos estáticos (como CSS e imagens) para estilização.
   - Renderiza templates HTML dinamicamente usando Jinja2.

9. **Banco de Dados SQLite:**
   - Utiliza SQLAlchemy para interagir com um banco de dados SQLite (`db.sqlite3`).
   - Define modelos de dados como `Usuario` e `Agendamento` para persistência.

Essas funcionalidades fornecem uma base para uma aplicação web simples de agendamento para uma barbearia, permitindo que clientes façam agendamentos e visualizem informações relevantes sobre serviços disponíveis.


## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

- **main.py**: Configuração do FastAPI, definição de rotas e inicialização do servidor.
  
- **models/**: Definição dos modelos de dados utilizando SQLAlchemy.

- **CRUD/**: Operações de criação, leitura, atualização e exclusão (CRUD) no banco de dados.

- **Templates/**: Templates HTML usando Jinja2 para renderização dinâmica.

- **static/**: Arquivos estáticos como CSS, imagens, etc.

- **database/**: Arquivos relacionados ao banco de dados, como `db.sqlite3` (banco de dados SQLite neste caso).

- **requirements.txt**: Lista de dependências Python necessárias para o projeto.

- **README.md**: Documentação do projeto, incluindo instruções de uso, configuração e contribuição.

## Configuração do Banco de Dados
Este projeto utiliza SQLite como banco de dados padrão.

Não são necessárias configurações adicionais para o SQLite.

## Tecnologias usadas

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) 	![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)


## Contribuição

Contribuições são bem-vindas! Para contribuir com este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Clone o fork para sua máquina local:
  ```bash
   git clone https://github.com/seu-usuario/Barbearia-com-FastApi.git
   ```
3. Navegue até o diretório do projeto:
  ```bash
  cd Barbearia-com-FastApi
  ```
4. Crie uma branch para sua contribuição:
  ```bash
  git checkout -b feature/nova-feature
  ```  
5. Faça suas mudanças no código e adicione os arquivos modificados:
   ```bash
   git add .
   ```
6.Faça commit das suas mudanças:
   ```bash
   git commit -m 'Adiciona nova feature'
   ```
7. Push para a branch que você criou no seu fork:
   ```bash
   git push origin feature/nova-feature
   ```
8.Abra um pull request no repositório original e descreva suas mudanças.
 

   
