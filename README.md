# Get brazilian docs

#### This Rest API fetch main brazilian personal documents in texts.

Check it out at https://get-brazilian-docs.herokuapp.com/get_docs/.

### Technologies:

- Python
- Django
- Django Rest Framework
- Docker

### Highlights:

Currently search for 3 kinds of brazilian documents:

1. CPF  - citizen unique ID.
2. CNPJ - companies unique ID.
3. CEP  - brazilian zip code.

Official documents algorithms validation are applied (thanks to [validate-docbr](https://github.com/alvarofpp/validate-docbr) lib).

![is](Screenshot.png)

### Requirements:

    - Python 3+
    - Docker
  
### Instalation:

    git clone https://github.com/Gabriel-Nunes/get_br_docs.git
    cd get_br_docs
    docker build -t get_docs .
    docker run -p 8000:80 get_docs
