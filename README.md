# Cadastrinho Back
Este é o back-end do projeto de MVP para a Sprint de "Desenvolvimento Full Stack Básico" da pós graduação em Engenharia de Software da PUC-Rio.

O projeto tem como objetivo ser uma aplicação de cadastro de produtos da "Una - Loja Holística".
Como parte da criação do MVP, foi feita uma entrevista com a dona da loja, minha esposa, para definir os requisitos iniciais da primeira versão da aplicação, alinhando necessidades da loja com os requisitos do MVP da sprint.

## Como executar

- Clonar ou baixar o repositório em sua máquina.
- Criar um ambiente virtual do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- Acessar o diretório raiz pelo terminal.
- Instalar todas as libs python listadas no arquivo 'requirements.txt".

Comando para instalar dependências/bibliotecas descritas no arquivo 'requirements.txt'
```
pip install -r requirements.txt
```

Para executar a API basta executar:
```
flask run --host 0.0.0.0 --port 5000
```

Em modo desenvolvimento, é recomendado executar o parâmetro "reload", que irá reiniciar o servidor automaticamente após cada alteração no código
```
flask run --host 0.0.0.0 --port 5000 --reload
```

Abra a URL abaixo no navegador
```
http://127.0.0.1:5000/
```
