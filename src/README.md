# AegisEdge Source Code Architecture (`/src`)

This directory is designated for the core Python application driving the real-time AI inference, spatial safety analysis, and alert routing for AegisEdge.

## 🏗️ Planned Pipeline Structure (Stage II Implementation)

Upon receiving the **ASUS UGen300 USB AI Accelerator** in Stage II, the source code will be organized into the following modules:

```text
src/
├── main.py              # Application entry point & main event loop
├── camera_stream.py     # Multi-threaded RTSP / USB camera stream receiver
├── hailo_inference.py   # HailoRT Python API interface (HEF model loading & execution)
├── spatial_logic.py     # Restricted zone geofencing & PPE compliance checking
├── tracker.py           # Multi-object tracking (e.g., BYTETracker / SORT)
└── alert_system.py      # Local alert dispatcher (WebSocket / MQTT / Webhook)
