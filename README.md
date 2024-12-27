# Antes de tudo

Antes te realizar os testes, será nescessario baixar o repositório.
1. Abra o terminal e clone o projeto.

    ```bash
    git clone https://github.com/MahdeMaria/TDD.git
    ```


## 2. Preparando o Ambiente Virtual (venv)

Para garantir um ambiente de desenvolvimento limpo e isolado, siga as etapas abaixo para criar e ativar um ambiente virtual Python.

### Passos:

1. Abra o terminal e navegue até o diretório raiz do projeto.

2. Crie um novo ambiente virtual:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

   - **No Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **No macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

Agora o ambiente virtual está ativado

## 3. Instalando as Dependências

Para instalar as dependências do projeto, execute o comando abaixo dentro da primeira pasta setup:

```bash
pip install -r requirements.txt
```
## 3. Execute as migrações

Para realizar as migraçõesdo projeto execute o comando abaixo:

```bash
python manage.py migrate
```

## 4. Execute o projeto

Para realizar os testes, execute o comando abaixo:

```bash
python manage.py test
```