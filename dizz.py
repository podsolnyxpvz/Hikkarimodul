from .. import loader
from asyncio import sleep


@loader.tds
class HeartsMod(loader.Module):
    strings = {"name": "Dizlike"}

    @loader.owner
    async def heartcmd(self, message):
        for _ in range(10):
            for heart in ["⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀", "⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⠀ 
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
                await message.edit(heart)
                await sleep(0.3)
