from pyrogram import Client
from os import system
from _date import (_tokn,
                   _hasd,
                   loogs)
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
        self.client = Client('_Astro',
                             api_id=self.apiid,
                             api_hash=self.aapihasd,
                             bot_token=self.token,
                             plugins=dict(root="complemet")
                             )
        loogs
        return self.client


if __name__ == '__main__':
    if _Astro:
        # limpiar consola windows/linux
        try:
            system('cls')
        except Exception:
            system('clear')

        print('Running: True \n')

        setcion = _Astro(21199736, _hasd, _tokn).inictSecc()

        # Iniciar la expiracion en background
        iniciar_expiracion_en_background(interval_seconds=60)

        setcion.run()
    else:
        None

    print('_Error: No se pudo conectar, revisa los datos.')
