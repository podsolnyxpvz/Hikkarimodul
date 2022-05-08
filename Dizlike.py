from .. import loader

from asyncio import sleep

@loader.tds

class HeartsMod(loader.Module):

    strings = {"name": "Magic of smiles"}

    @loader.owner

    async def heartscmd(self, message):

        for _ in range(10):

            for heart in ["1", "2", "3", "4", "5", "6", "7"]:

                await message.edit(heart)

                await sleep(0.3)
