import time
import asyncio
import sys
import os

# Ensure we can import environment from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from environment import DisasterEnvironment

class SensorAgent(Agent):
    class SensingBehaviour(PeriodicBehaviour):
        async def on_start(self):
            print("Sensor starting monitoring...")

        async def run(self):
            severity = self.agent.env.get_severity()
            print(f"[{time.ctime()}] Sensor Reading: Severity Level {severity}")
            
            if severity >= 8:
                print(f"!!! CRITICAL WARNING: SEVERITY {severity} !!!")
            elif severity >= 5:
                print(f"--- Warning: Elevated Severity {severity} ---")

    async def setup(self):
        print("SensorAgent initializing...")
        self.env = DisasterEnvironment()
        # Check every 2 seconds
        b = self.SensingBehaviour(period=2) 
        self.add_behaviour(b)

async def main():
    agent = SensorAgent("abeltattah@chat.between-us.online", "123Konka@")
    await agent.start()

    print("SensorAgent started. Press Ctrl+C to quit.")
    try:
        while agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await agent.stop()
        print("SensorAgent stopped")

if __name__ == "__main__":
    asyncio.run(main())
