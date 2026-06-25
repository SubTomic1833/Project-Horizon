import asyncio
import json
import websockets
from sense_hat import SenseHat

try:
    sense = SenseHat()
    sense.clear()
    print("Project Horizon - Raw Flight Stream Engine Active!")
except Exception as e:
    print(f"Error connecting to Sense HAT: {e}")
    sense = None

throttle = 0  # Starts at 0% idle engine power

async def send_flight_data(websocket):
    global throttle
    print("Cockpit Link Connected!")
    
    while True:
        try:
            if sense:
                # Read raw angles straight off the IMU sensor
                orientation = sense.get_orientation()
                pitch = orientation['pitch']
                roll = orientation['roll']
                heading = orientation['yaw']
                
                # Convert 0-360 scale to standard flight relative pitch/roll degrees
                if roll > 180: roll -= 360
                if pitch > 180: pitch -= 360

                # Joystick input adjusts engine power quadrant directly
                for event in sense.stick.get_events():
                    if event.action == "released" or event.action == "held":
                        if event.direction == "up":
                            throttle = min(100, throttle + 5)
                        elif event.direction == "down":
                            throttle = max(0, throttle - 5)
                        elif event.direction == "middle":
                            throttle = 0

                # Clean screen - absolutely NO automatic text overlays or locks
                sense.clear()

                # Build the telemetry pack to blast down the WebSocket pipe
                packet = {
                    "pitch": pitch,
                    "roll": roll,
                    "heading": heading,
                    "throttle": throttle
                }
                
                await websocket.send(json.dumps(packet))
            
            await asyncio.sleep(1 / 30) # 30Hz refresh rate cycle
            
        except websockets.exceptions.ConnectionClosed:
            print("Cockpit Link Disconnected.")
            break
        except Exception as e:
            print(f"Stream Error: {e}")
            break

async def main():
    async with websockets.serve(send_flight_data, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        if sense: sense.clear()
