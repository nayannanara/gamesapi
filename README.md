# Games API

Esta API tem como objetivo extrair algumas informações de um arquivo `games.log` gerado pelo servidor de quake 3 arena. 

Para cada jogo o parser cria um json nesta estrutura:

```json
  "game_1": {
      "total_kills": 45,
      "players": ["Dono da bola", "Isgalamido", "Zeh"],
      "kills": {
        "Dono da bola": 5,
        "Isgalamido": 18,
        "Zeh": 20,
      }
    }
```

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

## Execução da API

Para executar o projeto, utilizei a [pyenv](https://github.com/pyenv/pyenv), com a versão 3.11.4 do `python` para o ambiente virtual.

Caso opte por usar pyenv, após instalar, execute:

```bash
pyenv virtualenv 3.11.4 gamesapi
pyenv activate gamesapi
pip install -r requirements.txt
```
Para subir o banco de dados, caso não tenha o [docker](https://docs.docker.com/engine/install/ubuntu/) e o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
docker-compose up -d
```

Para criar o banco de dados, execute:

```bash
make run-migrations
```

Para executar o parser e criar dados no banco, execute:

```bash
make insert-games
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs

## Consulta de games

Para visualizar os dados cadastradaos na base, execute a seguinte `request`:


_Chamada_:

```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v0/games/' \
  -H 'accept: application/json'
```

_Resposta_:

```json
[
  {
    "name": "game_1",
    "players": [
      {
        "name": "Dono da Bola"
      }
    ],
    "total_kills": 11,
    "kills": {
      "Isgalamido": -7,
      "Dono da Bola": 0,
      "Mocinha": -1
    }
  },
  {
    "name": "game_1",
    "players": [
      {
        "name": "Isgalamido"
      }
    ],
    "total_kills": 11,
    "kills": {
      "Isgalamido": -7,
      "Dono da Bola": 0,
      "Mocinha": -1
    }
  }
]
```

**Códigos de retorno da API**

Alguns códigos de retorno foram mapeados.

| Código | Descrição              |
|--------|------------------------|
|  200   |  Ok                    |
|  500   |  Internal Server Error |
## Executar testes

Os testes foram implementados com o `pytest`.

Para executar os testes, execute:

```bash
make test
```
Os testes implementados neste projeto atingem uma cobertura de 98%, para execução:

```bash
make coverage
```
Caso queira executar um teste específico, execute:

```bash
make test-matching Q=nomedoteste
```