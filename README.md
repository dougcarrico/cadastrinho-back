#API Cadastrinho
Projeto de MVP ainda em desenvolvimento

## Como executar

- Clocar o repositório
- Acessar o diretório raiz pelo terminal
- Instalar todas as libs python listadas no arquivo 'requirements.txt".
    - Recomendado utilizar ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

Comando para instalar dependÊncias/bibliotecas descritas no arquivo 'requirements.txt'
```
pip install -r requirements.txt
```

Para executar a API basta executar:
``
pip flask run --host 0.0.0.0 --port 5000
``

Em modo desenvolvimento, é recomendado executar o parâmetro "reload", que irá reiniciar o servidor automaticamente após cada alteração no código
``
pip flask run --host 0.0.0.0 --port 5000 --reload
``

Abra a URL ``http://127.0.0.1:5000/`` no navegador
