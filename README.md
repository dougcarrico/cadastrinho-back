# Cadastrinho Back
Este é o back-end do projeto de MVP para a Sprint de "Desenvolvimento Full Stack Básico" da pós graduação em Engenharia de Software da PUC-Rio.

O projeto tem como objetivo ser uma aplicação de cadastro de produtos da "Una - Loja Holística".
Como parte da criação do MVP, foi feita uma entrevista com a dona da loja, minha esposa, para definir os requisitos iniciais da primeira versão da aplicação, alinhando necessidades da loja com os requisitos do MVP da sprint.

## Como executar

Clonar ou baixar o repositório em sua máquina.

**OBS:** Recomendado criar um ambiente virtual do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) com a versão 3.13.7 do python. Caso tenha problemas com execução de scripts Windows para a criação do ambiente virtual, ver sobre [Execution Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5)

Comando para criar o ambiente virtual.
```
python3.13 -m venv env
```

Comando para ativar o ambiente virtual.
```
.\env\Scripts\Activate
```

Acessar o diretório raiz pelo terminal.

Instalar libs Python descritas no arquivo 'requirements.txt' utilizando o comando abaixo.
```
pip install -r requirements.txt
```

Executar a API com o comando abaixo.
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
