

0. Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
```

1. Instalar dependências:


```bash
pip install git+https://github.com/tfs4/siconfipy.git

pip install -r requirements.txt
```

2. Edite o conteúdo do arquivo **djangocore/configs/configs.py**

3. Gere um `.env` local

```bash
python contrib/env_gen.py
```

4. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

