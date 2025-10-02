# main.py

import asyncio
from src.classes import Game

async def main():
    game = Game()
    await game.run()  # <-- run must also be async

# This will be called automatically by Pygbag when loaded in browser
asyncio.run(main())
