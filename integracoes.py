import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError


def buscar_local_api(local: str) -> list[dict] | None:
    parametros = urlencode({
        "q": f"{local}, Estado de São Paulo, Brasil",
        "format": "jsonv2",
        "limit": 5,
        "countrycodes": "br"
    })

    url = (
        "https://nominatim.openstreetmap.org/search?"
        + parametros
    )

    requisicao = Request(
        url,
        headers={
            "User-Agent": "Syntra-FIAP/1.0 (contato: glabradadev@gmail.com)"
        }
    )

    try:
        with urlopen(requisicao, timeout=10) as resposta:
            locais = json.load(resposta)

        return locais

    except HTTPError as erro:
        print("Erro HTTP:", erro.code)
        return None

    except URLError as erro:
        print("Erro de conexão:", erro.reason)
        return None

    except TimeoutError:
        print("A conexão demorou muito.")
        return None

    except json.JSONDecodeError:
        print("Erro ao interpretar a resposta da API.")
        return None

def calcular_trajeto_api(origem: dict, destino: dict) -> dict | None:
        parametros = urlencode({
            "fromPlace": f"{origem['lat']},{origem['lon']}",
            "toPlace":f"{destino['lat']},{destino['lon']}"
        })

        url = (
            "https://api.transitous.org/api/v6/plan?"
            + parametros
        )

        requisicao = Request(
            url,
            headers ={
                "User-Agent": "Syntra-FIAP/1.0 (contato: glabradadev@gmail.com)"
            }
        )

        try:
            with urlopen(requisicao, timeout=20) as resposta:
                trajetos = json.load(resposta)

            return trajetos

        except HTTPError as erro:
            print("Erro HTTP:", erro.code)
            return None

        except URLError as erro:
            print("Erro de conexão:", erro.reason)
            return None

        except TimeoutError:
            print("A conexão demorou muito.")
            return None

        except json.JSONDecodeError:
            print("Erro ao interpretar a resposta da API.")
            return None

def buscar_partidas_estacao(codigo_estacao: str) -> dict | None:
    parametros = urlencode({
        "stopId": codigo_estacao,
        "n": 60
    })

    url = "https://api.transitous.org/api/v6/stoptimes?" + parametros

    requisicao = Request(
        url,
        headers={"User-Agent": "Syntra-FIAP/1.0 (contato: glabradadev@gmail.com)"}
    )

    try:
        with urlopen(requisicao, timeout=15) as resposta:
            return json.load(resposta)

    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as erro:
        print("Não foi possível consultar as partidas:", erro)
        return None

def buscar_status_linhas() -> dict | None:
    chave = "ta_y-VXKq-FdxRdjTB9IbAIeM0ZU88q7qvS"

    url = "https://api.trilhosagora.com.br/v1/status"

    requisicao = Request(
        url,
            headers={
            "X-API-Key": chave,
            "User-Agent": "Syntra-FIAP/1.0 (projeto acadêmico)",
            "Accept": "application/json"
        }
    )

    try:
        with urlopen(requisicao, timeout=10) as resposta:
            return json.load(resposta)

    except HTTPError as erro:
        print("Código HTTP:", erro.code)
        print("Motivo:", erro.reason)
        print("Resposta da API:", erro.read().decode("utf-8", errors="replace"))
        return None

    except (URLError, TimeoutError, json.JSONDecodeError) as erro:
        print("Erro ao consultar status:", erro)
        return None

def buscar_estacao_api(nome: str) -> list | None:
    parametros = urlencode({
        "text": nome,
        "type": "STOP"
    })

    url = "https://api.transitous.org/api/v1/geocode?" + parametros

    requisicao = Request(
        url,
        headers={"User-Agent": "Syntra-FIAP/1.0 (contato: glabradadev@gmail.com)"}
    )

    try:
        with urlopen(requisicao, timeout=15) as resposta:
            return json.load(resposta)

    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None