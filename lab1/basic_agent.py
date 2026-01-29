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

if __name__ == "__main__":
    # Ensure to use a valid JID and password. 
    # If using embedded server, localhost should work if mapped correctly or registered.
    dummy = BasicAgent("basic_agent@localhost", "password")
    future = dummy.start()
    future.result() # Wait for agent to start

    print("Agent started. Press Ctrl+C to quit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        dummy.stop()
        print("Agent stopped")
