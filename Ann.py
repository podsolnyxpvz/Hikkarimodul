from .. import loader

from asyncio import sleep

@loader.tds

class DizlikeMod(loader.Module):

    strings = {"name": "Анимированный лайк и дизлайк"}

    @loader.owner

    async def dizlikecmd(self, message):

        for _ in range(1):

            for dizlike in ["🟥🟥🟥🟥🟥🟥🟥🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥\n🟥🟥🟥🟥⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥\n🟥🟥🟥🟥⬜🟥⬜🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"]:

                await message.edit(dizlike)

                await sleep(0.5)

   @loader.owner

     async def likecmd(self, message):

        for _ in range(1):

            for like in ["🟦🟦🟦🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦🟦🟦🟦🟦🟦🟦"]:

                await message.edit(like)

                await sleep(0.5)

