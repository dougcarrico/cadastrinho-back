# Cadastrinho Back
Este é o back-end do projeto de MVP para a Sprint de "Desenvolvimento Full Stack Básico" da pós graduação em Engenharia de Software da PUC-Rio.

O projeto tem como objetivo ser uma aplicação de cadastro de produtos da "Una - Loja Holística".
Como parte da criação do MVP, foi feita uma entrevista com a dona da loja, minha esposa, para definir os requisitos iniciais da primeira versão da aplicação, alinhando necessidades da loja com os requisitos do MVP da sprint.

## API externa - Shipping Calculate (Melhor Envio)

É utilizada a API do Melhor Envio para a rota POST de cálculo de frete (/shipping_calculate).
Para mais informações sobre a API, ver os links abaixo:
- https://docs.melhorenvio.com.br/docs/cotacao-de-fretes
- https://docs.melhorenvio.com.br/reference/calculo-de-fretes-por-produtos

### Como gerar o token para uso do shipping calculate da Melhor Envio
- Criar conta no https://melhorenvio.com.br/ 
- Clicar em "Integrações"
- Clicar em "Permissões de acesso"
- Clicar em "Gerar um novo token"
- Clicar em "Li e concordo" e clicar em avançar
- Definir um nome para o token
- Em "Permissões" clicar em "Shipping calculate (Cotação de fretes)"
- Clicar em "Gerar token"
- Copiar o token e salvar em algum local seguro

## Configurar arquivo de variáveis de ambiente (Serve para rodar com docker ou sem docker)
- Criar um arquivo com o nome ".env" na pasta pai da pasta raiz do back-end. Como no exemplo abaixo, que o arquivo ".env" é irmão da pasta "cadastrinho-back", pasta raiz do back-end.
```
/.env
/cadastrinho-back/
```
- Adicionar o conteúdo abaixo no arquivo ".env", substituindo "meu_token" pelo token de shipping calculate da Melhor Envio
```
SHIPPING_CALCULATE_TOKEN=meu_token
```

## Como executar com Docker

Clonar ou baixar o repositório em sua máquina.

Ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegar até o diretório raiz do projeto, aquele que contém o Dockerfile e o requirements.txt, no terminal. Executar como administrador o comando abaixo para construir a imagem Docker

```
docker build -t back-image:py3-13 .
```

Assim que a imagem estiver criada, utilizar o comando abaixo para executar o container.

```
docker run --env-file ../.env --name back-container -d -p 5000:5000 back-image:py3-13
```
- `--env-file ../.env` define o arquivo de variáveis a ser utilizado
- `--name back-container` define o nome do container
- `-d` define que o container rodará em plano de fundo e imprime o id do container no terminal
- `-p 5000:5000` define as portas utilizadas
- `back-image:py3-13` define a imagem a ser utilizada para criação do container

Acessar a url abaixo no navegador para visualizar a API em execução

```
http://localhost:5000
```

## Como executar sem Docker

Clonar ou baixar o repositório em sua máquina.

**OBS:** Recomendado criar um ambiente virtual do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) com a versão 3.13.7 do python. Caso tenha problemas com execução de scripts Windows para a criação do ambiente virtual, ver sobre [Execution Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5)

Acessar o diretório pai do diretório raiz do projeto. Executar o comando abaixo para criar o ambiente virtual.
```
python3.13 -m venv env
```

Utilizar o comando abaixo para ativar o ambiente virtual.
```
.\env\Scripts\Activate
```

Acessar o diretório raiz do projeto pelo terminal.

Utilizar o comando abaixo para instalar libs Python descritas no arquivo 'requirements.txt'.
```
pip install -r requirements.txt
```

Utilizar o comando abaixo para Executar a API.
```
flask run --host 0.0.0.0 --port 5000
```

Em modo desenvolvimento, é recomendado executar o parâmetro "reload", que irá reiniciar o servidor automaticamente após cada alteração no código. Como no exemplo abaixo.
```
flask run --host 0.0.0.0 --port 5000 --reload
```

Abrir a URL abaixo no navegador.
```
http://127.0.0.1:5000/
```