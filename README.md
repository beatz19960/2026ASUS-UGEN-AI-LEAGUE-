# AegisEdge: Privacy-First Workplace Safety Guardian

This project is an entry for the **ASUS UGen AI League Hackathon (Battlefield Lightning Track)**.

## 📌 Project Overview
AegisEdge is a decentralized, 100% on-device AI safety monitor designed for manufacturing and construction sites. Powered by the **ASUS UGen300 USB AI Accelerator (Hailo-10H, 8GB LPDDR4)**, it performs real-time Personal Protective Equipment (PPE) detection and danger zone monitoring without sending sensitive video feeds to the cloud.

## ⚙️ Target Hardware Specification
* **Target Hardware:** ASUS UGen300 USB AI Accelerator (UGen300-USB-8G)
* **AI Chipset:** Hailo-10H NPU (Up to 40 TOPS @ INT4 / 20 TOPS @ INT8)
* **Memory:** 8GB LPDDR4 (4266 MT/s)
* **Interface:** USB 3.1 Gen2 Type-C (10Gbps, Plug & Play)
* **Power Consumption:** ~2.5W (Typical)

## ⚙️ System Architecture (Proposed)
1. **Input:** RTSP Video stream from IP Cameras or USB Video input.
2. **Inference:** YOLOv8/v9 object detection quantized via Hailo Dataflow Compiler and executed on the ASUS UGen300 USB Accelerator via HailoRT.
3. **Logic:** Spatial analysis to determine if workers in restricted zones are lacking PPE.
4. **Output:** Localized JSON metadata and immediate alert triggers (WebSocket/API).

## 🗂 Repository Structure (Stage I)
- `/docs` - Contains the Stage I Proposal Presentation (PDF).
- `/models` - Placeholder for ONNX and Hailo-quantized models (`.hef`).
- `/src` - Placeholder for Python inference application (HailoRT integration).
- `/data_prep` - Scripts for downloading and formatting PPE datasets.

## 🚀 Next Steps (Stage II Plan)
Upon advancing to Stage II and receiving the **ASUS UGen300-USB-8G** hardware:
1. Compile the custom YOLO PPE detection model into Hailo Executable Format (`.hef`) using the Hailo Dataflow Compiler SDK.
2. Develop the host Python application incorporating OpenCV and HailoRT C++/Python API over the USB 3.1 Gen2 interface.
3. Conduct local performance benchmarks (FPS, inference latency, host CPU utilization, and thermal/power efficiency).


