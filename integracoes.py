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