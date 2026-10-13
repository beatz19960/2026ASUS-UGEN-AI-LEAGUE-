# AegisEdge: Privacy-First Workplace Safety Guardian

This project is an entry for the **ASUS UGen AI League Hackathon (Battlefield Lightning Track)**. 

## 📌 Project Overview
AegisEdge is a decentralized, 100% on-device AI safety monitor designed for manufacturing and construction sites. Powered by the **ASUS UGen300 AI Accelerator (Hailo-10H)**, it performs real-time Personal Protective Equipment (PPE) detection and danger zone monitoring without sending sensitive video feeds to the cloud.

## ⚙️ System Architecture (Proposed)
1. **Input:** RTSP Video stream from IP Cameras.
2. **Inference:** YOLOv8/v9 object detection quantized via Hailo Dataflow Compiler and executed on the ASUS UGen300 via HailoRT.
3. **Logic:** Spatial analysis to determine if workers in restricted zones are lacking PPE.
4. **Output:** Localized JSON metadata and immediate alert triggers (WebSocket/API).

## 🗂 Repository Structure (Stage I)
* `/docs` - Contains the Stage I Proposal Presentation (PDF).
* `/models` - Placeholder for ONNX and Hailo-quantized models (.hef).
* `/src` - Placeholder for Python inference application (HailoRT integration).
* `/data_prep` - Scripts for downloading and formatting PPE datasets.

## 🚀 Next Steps (Stage II Plan)
Upon advancing to Stage II and receiving the ASUS UGen300 hardware:
1. Compile the custom YOLO model into `.hef` format using Hailo Dataflow Compiler.
2. Develop the local Python pipeline integrating OpenCV and HailoRT.
3. Conduct performance testing (FPS, latency, power consumption).

## 📄 License
MIT License
