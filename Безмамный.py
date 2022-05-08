from .. import loader

from asyncio import sleep

@loader.tds

class HeartsMod(loader.Module):

    strings = {"name": "Дизлайк"}

    @loader.owner

    async def dizcmd(self, message):

        for _ in range(1):

            for diz in ["\n⣀⣤⣤⣤⣤⣀\n", "\n⣀⣤⣤⣤⣤⣀\n⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦\n", "⣀⣤⣤⣤⣤⣀\n⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦\n⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧\n", "\n⣀⣤⣤⣤⣤⣀\n⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦,\n⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧\n⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿⠀", "\n⣀⣤⣤⣤⣤⣀\n⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦\n⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧\n⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿\n⢻⣿⣧⣤⣤⡄⠀⣧⣤⣿⣿⡟\n", "\n⣀⣤⣤⣤⣤⣀\n⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦\n⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧\n⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿\n⢻⣿⣧⣤⣤⡄⠀⣧⣤⣿⣿⡟\n⠻⣿⣿⣿⣿⣾⣿⣿⣿⠟\n", "⣀⣤⣤⣤⣤⣀\n⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦\n⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧\n⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿\n⢻⣿⣧⣤⣤⡄⠀⣧⣤⣿⣿⡟\n⠻⣿⣿⣿⣿⣾⣿⣿⣿⠟\n⠉⠛⠛⠛⠛⠉\n"]:

                await message.edit(diz)

                await sleep(0.5)

