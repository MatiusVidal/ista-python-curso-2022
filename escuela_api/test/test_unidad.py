from asyncio.windows_events import NULL
from escuela_api import api

def test_lista_estudiante():
    assert api.buscar_por_materia('java') == 'la materia java no existe'