import asyncio
from pyrogram.client import Client
from os import system
from _date import (tokn, hasd, loogs)
from complemet.func import expiracion_worker

class _Astro:

    def __init__(self, apiid: int, apihasd: str, token: str):
        self.apiid = apiid
        self.apihasd = apihasd
        self.token = token

    def inictSecc(self):
        if self.apiid is None or self.apihasd is None or self.token is None:
            raise ValueError("apiid, apihasd y token no pueden ser None")

        self.client = Client(
            '_Astro',
            api_id=self.apiid,
            api_hash=self.apihasd,
            bot_token=self.token,
            plugins=dict(root="complemet")
        )
        loogs
        return self.client


async def main():
    system('cls')
    print('Running: True \n')
    bot = _Astro(21199736, hasd, tokn).inictSecc()

    # Lanzar worker en segundo plano para actualizar expiracion cada 60 segundos
    asyncio.create_task(expiracion_worker(60))

    bot.run()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f'_Error: No se pudo conectar, revisa los datos.\n{e}')
