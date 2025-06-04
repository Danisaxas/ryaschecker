from pyrogram import Client
from os import system
from _date import (_tokn, _hasd, loogs)
from complemet.func import iniciar_expiracion_en_background

class _Astro:

    def __init__(
        self,
        apiid: int = None,
        apihasd: str = None,
        token: str = None
    ):
        self.apiid = apiid
        self.aapihasd = apihasd
        self.token = token

    def inictSecc(self):
        self.client = Client(
            '_Astro',
            api_id=self.apiid,
            api_hash=self.aapihasd,
            bot_token=self.token,
            plugins=dict(
                root="complemet",  # Raíz de los plugins principales
                handlers="locales/handlers"  # Directorio de los handlers en locales
            )
        )
        loogs
        return self.client


if __name__ == '__main__':
    try:
        # Limpiar consola multiplataforma
        try:
            system('cls')
        except Exception:
            system('clear')

        print('Running: True \n')

        # Iniciar expiración en background con intervalo de 1 segundo
        iniciar_expiracion_en_background(interval_seconds=1)

        setcion = _Astro(21199736, _hasd, _tokn).inictSecc()

        setcion.run()

    except Exception as e:
        print(f'_Error: No se pudo conectar, revisa los datos.\n{e}')
