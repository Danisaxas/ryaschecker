from pyrogram import Client
from os import system
from _date import (_tokn,
                   _hasd,
                   loogs)

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
   # try:
    if _Astro:
        system('cls')
        print('Running: True \n')
        setcion = _Astro(21199736, _hasd, _tokn).inictSecc()
        setcion.run()
    else:
        None
 #   except:
    print('_Error: Nose pudo conectar, Revices los datos.')
else:
    None
