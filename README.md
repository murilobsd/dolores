# Dolores

![Dolores](./dolores.jpg "Dolores")

> Dolores é o bot do grupo do [Telegram][1] da turma 2020/01 de Engenharia
>de Software.

## Features

## Instalação

De preferência crie um ambiente virtual, no exemplo abaixo criamos um ambiente
chamado *venv* com [python3][2].

```sh
$ python3 -m venv venv
$ . ./venv/bin/activate
(venv) $
```

Basta agora dentro do ambiente virtual utiliza o *[pip][3]* para instalar os pacotes
necessários para o correto funcionamento do bot.

```sh
(venv) $ pip install -r requirements.txt
```

## Rodando

Uma vez que os pacotes foram instalados, basta ter o **[token][4]** do Bot em 
mãos e passar via variável de ambiente, no caso do *linux* seria assim:

```sh
(venv) $ TOKEN=token-do-bot ./main.py
```

**Obs.:** Veja que estamos dentro do ambiente virtual.

[1]: https://telegram.org/
[2]: https://www.python.org/download/releases/3.0/
[3]: https://pypi.org/project/pip/
[4]: https://core.telegram.org/bots  
