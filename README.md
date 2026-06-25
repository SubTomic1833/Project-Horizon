# Project Horizon

A custom, real-time, pseudo-3D browser flight simulator featuring a low-poly terrain rendering engine. Built to accept live motion-telemetry from a hardware control rig or fallback gracefully to full desktop keyboard and mouse controls.

## 🚀 Live Demo & Repository
* **Live Web Demo:** https://subtomic1833.github.io/Project-Horizon/
* **Code Repository:** https://github.com/SubTomic1833/Project-Horizon

---

## 🛠️ How It Works

Project Horizon runs on a custom-built, lightweight 3D projection engine rendered entirely inside a standard HTML5 `<canvas>` using pure JavaScript—no external 3D libraries (like Three.js or WebGL) required. 

### 📡 Dual-Mode Control System
1. **Hardware Mode (Pi Link):** The simulator sets up a WebSocket connection to stream real-time pitch, roll, and throttle variables directly from a **Raspberry Pi 5** equipped with an IMU sensor (like a **Sense HAT**). Moving the hardware rig manipulates the cockpit view seamlessly.
2. **Desktop Fallback Mode:** If no hardware socket is connected, the simulator automatically opens up interactive manual flight overrides so anyone can fly using standard desktop peripherals.

---

## 🕹️ Controls (Desktop Fallback)

If you are reviewing this project without the Raspberry Pi hardware rig connected, use the following interactive desktop layout to pilot the aircraft:

| Control | Input Mechanism | Action |
| :--- | :--- | :--- |
| **Pitch (Nose Up/Down)** | `W` / `S` | Pull up to climb or push down to dive |
| **Roll (Bank Left/Right)** | `A` / `D` | Bank the wings to change your aerodynamic heading |
| **Throttle (Engine Power)** | `Mouse Scroll Wheel` | Increase or decrease engine thrust ($0\% - 100\%$) |

---

## 🖥️ Flight Instruments HUD

The right-hand side of the viewport features a high-visibility, neon-styled digital aviation instrument suite mirroring standard glass cockpits:
* **Airspeed Tape (Left Track):** Displays real-time airspeed calculated in Knots (KT), dynamically scaling based on current throttle output and aerodynamic drag adjustments.
* **Altitude Tape (Right Track):** Tracks vertical height in Feet (FT) above sea level, updating instantly based on your pitch angle and forward velocity.

---

## 📦 Repository Structure

* `index.html` — The complete frontend flight simulator application containing the Canvas matrix projection engine, UI overlays, and input listeners.
* `telemetry_server.py` — The backend of the flight simulator applciation, handling the data telemetry from the Raspberry Pi 5 to the game.
