# 🎯 Real-Time Object Detection with YOLOv11 & OpenCV

A real-time object detection application that uses **YOLOv11** (Ultralytics) and **OpenCV** to detect and label objects through a live webcam feed.

---

## 📸 Demo

> The webcam window displays bounding boxes and class labels around detected objects in real time. Press `q` to quit.

---

## 🚀 Features

- 🔴 Live webcam feed with real-time inference
- 🟩 Bounding box drawing around detected objects
- 🏷️ Class label overlay on each detected object
- ⚡ Powered by YOLOv11 Nano (`yolo11n.pt`) for fast, lightweight detection
- 🧠 Supports **84 object classes** including custom additions like `box`, `glass`, `cap`, `pen`, `pencil`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) | Object detection model |
| [OpenCV (`cv2`)](https://opencv.org/) | Webcam capture & image rendering |
| Python 3.8+ | Core language |

---

## 📁 Project Structure

```
📦 project-root/
 ┣ 📂 yolo-Weights/
 ┃ ┗ 📄 yolo11n.pt        # YOLOv11 Nano pre-trained weights
 ┣ 📄 yolo_cam.py          # Main detection script
 ┗ 📄 README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install ultralytics opencv-python
```

### 3. Download YOLO Weights

Download the **YOLOv11 Nano** weights and place them inside the `yolo-Weights/` folder:

```bash
mkdir yolo-Weights
# Download yolo11n.pt from Ultralytics and place it here
```

> You can also let Ultralytics auto-download it by running the script — it will fetch the weights automatically on the first run if the path is valid.

---

## ▶️ Usage

```bash
python yolo_cam.py
```

- A window named **`Cam`** will open showing your live webcam feed.
- Detected objects will be highlighted with **green bounding boxes** and **blue class labels**.
- Press **`q`** to quit the application.

---

## 🗂️ Supported Classes

The model detects **84 classes**, including all standard COCO classes plus custom additions:

<details>
<summary>Click to expand full class list</summary>

```
person, bicycle, car, motorbike, aeroplane, bus, train, truck, boat,
traffic light, fire hydrant, stop sign, parking meter, bench, bird,
cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe, backpack,
umbrella, handbag, tie, suitcase, frisbee, skis, snowboard, sports ball,
kite, baseball bat, baseball glove, skateboard, surfboard, tennis racket,
bottle, wine glass, cup, fork, knife, spoon, bowl, banana, apple,
sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake, chair,
sofa, pottedplant, bed, diningtable, toilet, tvmonitor, laptop, mouse,
remote, keyboard, cell phone, microwave, oven, toaster, sink,
refrigerator, book, clock, vase, scissors, teddy bear, hair drier,
toothbrush, box, glass, cap, pen, pencil
```

</details>

---

## 📋 Requirements

- Python 3.8 or higher
- Webcam / USB camera
- `ultralytics`
- `opencv-python`

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Ultralytics YOLOv11](https://github.com/ultralytics/ultralytics) for the object detection framework
- [OpenCV](https://opencv.org/) for real-time video processing
