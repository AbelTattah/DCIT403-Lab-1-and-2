import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class BasicAgent(Agent):
    class MyBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")

        async def run(self):
            print("Counter: {}".format(self.counter))
            self.counter += 1
            await asyncio.sleep(1)

        async def on_end(self):
            print("Behaviour finished")

    async def setup(self):
        print("Agent starting . . .")
        self.my_behav = self.MyBehaviour()
        self.my_behav.counter = 0
        self.add_behaviour(self.my_behav)

async def main():
    dummy = BasicAgent("abeltattah@chat.between-us.online", "123Konka@")
    await dummy.start()

    print("Agent started. Press Ctrl+C to quit.")
    try:
        while dummy.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await dummy.stop()
        print("Agent stopped")

if __name__ == "__main__":
    asyncio.run(main())
