from .. import loader
from asyncio import sleep


@loader.tds
class DizMod(loader.Module):
    strings = {"name": "Дизлайк"}

    @loader.owner
    async def heartscmd(self, message):
        for _ in range(10):
            for diz in ["⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀", "⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀ 
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀", "⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀ 
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀ 
⠀⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧⠀", "⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀ 
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀ 
⠀⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧⠀ 
⠀⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿⠀", "⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀ 
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀ 
⠀⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧⠀ 
⠀⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿⠀ 
⠀⢻⣿⣧⣤⣤⡄⠀⣧⣤⣿⣿⡟⠀", "⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀ 
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀ 
⠀⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧⠀ 
⠀⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿⠀ 
⠀⢻⣿⣧⣤⣤⡄⠀⣧⣤⣿⣿⡟⠀ 
⠀⠀⠻⣿⣿⣿⣿⣾⣿⣿⣿⠟⠀⠀ 
⠀", "⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀ 
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀ 
⠀⣼⣿⣿⠉⠉⠉⠉⡏⠉⣿⣿⣧⠀ 
⠀⣿⣿⡿⠀⠀⠀⠀⡇⠀⣿⣿⣿⠀ 
⠀⢻⣿⣧⣤⣤⡄⠀⣧⣤⣿⣿⡟⠀ 
⠀⠀⠻⣿⣿⣿⣿⣾⣿⣿⣿⠟⠀⠀ 
⠀⠀⠀⠀⠉⠛⠛⠛⠛⠉⠀⠀⠀⠀"]:
                await message.edit(diz)
                await sleep(0.3)