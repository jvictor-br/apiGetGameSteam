
# API GetGamesSteam

 Um backend API REST escrito em python, utilizando Flask



## Etiquetas

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-%203.10.5-green)](https://www.python.org/downloads/release/python-3105/)
[![Flask](https://img.shields.io/badge/Flask-2.2.2-green)](https://flask.palletsprojects.com/en/2.2.x/)
[![Flask-cors](https://img.shields.io/badge/Flask--Cors-3.0.10-green)](https://pypi.org/project/Flask-Cors/)

## GitHub

https://github.com/jvictor-br/apiGetGameSteam


## Stack utilizada

**Front-end:** HTML, CSS

**Back-end:** Python, Flask


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/jvictor-br/apiGetGameSteam
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  python ./backgame.py
```


## Uso/Exemplos
### Iniciar:
Dentro do diretório usar comando, ```python ./backgame.py```

### Uso:

Obter usuario: Fazer request GET na rota ```0.0.0.0/api```, usando appid do jogo da Steam que deseja buscar


### Exemplo:

GET ```0.0.0.0/api```

Headers ```appid:271590```

Resposta:
``` JSON
{
    "name": "Grand Theft Auto V",
    "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/271590/header.jpg?t=1678296348",
    "background": "https://cdn.akamai.steamstatic.com/steam/apps/271590/page_bg_generated_v6b.jpg?t=1678296348",
    "developers": [
        "Rockstar North"
    ],
    "publishers": [
        "Rockstar Games"
    ],
    "metacritic": {
        "score": 96,
        "url": "https://www.metacritic.com/game/pc/grand-theft-auto-v?ftag=MCD-06-10aaa1f"
    },
    "release_date": {
        "coming_soon": false,
        "date": "13/abr./2015"
    },
    "categories": [
        "Um jogador",
        "Multijogador",
        "JxJ",
        "JxJ on-line",
        "Cooperativo",
        "Cooperativo on-line",
        "Conquistas Steam",
        "Compat. total com controle",
        "Remote Play no celular",
        "Remote Play no tablet",
        "Remote Play na TV"
    ]
}
```


## Screenshots
#### Screenshot do Request acima
![App Screenshot](https://i.imgur.com/azvGcj2.png)


## Aprendizados

* Utilização de API externa
* Backend em Flask


## Relacionados

Segue alguns projetos relacionados

[SteamMatchWEB](https://github.com/jvictor-br/SteamMatchWEB)

[ApiGetUserSteam](https://github.com/jvictor-br/apiGetUserSteam)

