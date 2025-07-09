# 🤖 Agentic AI – KissanMitra Mobile App

Agentic AI meets agriculture: **KissanMitra** is a farmer-centric mobile application that leverages agent-based artificial intelligence to diagnose crop diseases, answer agricultural queries, and guide farmers with real-time insights.

> Built using **Java**, **Android SDK**, and **ConstraintLayout UI**, with a strong emphasis on usability, accessibility, and AI-human collaboration.

---

## 🌱 Overview

KissanMitra allows farmers to:
- 📸 Upload crop images for instant **disease diagnosis**
- 💬 Ask agricultural questions via **text or voice**
- 📈 Track **market price trends** for crops
- 🏛️ Discover active **government schemes**
- 🕒 Receive **personalized reminders**

Designed with **agentic AI principles**, the app acts not just as a tool — but as an **interactive agricultural assistant** that proactively guides and learns from the user’s behavior.

---

## 🧠 Key Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 🧠 AI Crop Diagnosis        | Upload plant images to detect diseases via ML model (future: Gemini/Firebase) |
| 🎤 Voice Search             | Speak in your language to ask crop or market-related questions               |
| 📈 Market Insights          | View live price trends for regional crops                                   |
| 🏛 Government Schemes       | Browse tailored schemes, subsidies, and updates                             |
| 🔁 Re-diagnosis & Feedback  | Re-upload crops, send results to officials, give feedback on advice          |
| ⏰ Smart Reminders          | App reminds you of pesticide use, irrigation, and harvesting schedules       |

---

## 📲 Screens in App Flow

1. **Home Screen** – quick access to Diagnose, Market, Schemes, Voice, Reminders
2. **Upload Screen** – crop image upload + text box for user query
3. **AI Scanning** – loading animation simulating agentic AI in progress
4. **Results** – disease info, treatment tips, store links, share/report buttons

---

## ⚙️ Tech Stack

| Layer        | Tool/Language                     |
|--------------|----------------------------------|
| 👨‍💻 UI        | Android XML + ConstraintLayout    |
| ☕ Backend     | Java + AppCompatActivity         |
| 🧠 AI (Planned)| Gemini AI / Firebase ML Kit      |
| 🖼 Media       | Image Picker Intent + Preview    |
| 📦 Data Layer  | (Optional) Firebase Firestore / SQLite |
| 📱 IDE         | Android Studio                   |

---

## 🚀 How to Run Locally

1. Clone this repo  
2. Open in Android Studio  
3. Sync Gradle (`constraintlayout`, `appcompat`)  
4. Run on emulator or real device (API 23+)

---

## 📂 Folder Structure

app/
├── res/
│ └── layout/
│ ├── activity_main.xml
│ ├── activity_upload.xml
│ ├── activity_loading.xml
│ └── activity_result.xml
├── java/
│ └── com/example/kissanmitra2/ui/
│ ├── MainActivity.java
│ ├── UploadActivity.java
│ ├── LoadingActivity.java
│ └── ResultActivity.java
├── AndroidManifest.xml
└── README.md


---

## 🛣️ Roadmap

- [ ] Integrate Gemini AI / Firebase ML Kit
- [ ] Multilingual voice recognition (Telugu, Hindi, Kannada)
- [ ] Add offline support for remote village areas
- [ ] Add analytics dashboard for agri officers

---

## 🤝 Acknowledgments

- Indian Farmers 👨‍🌾 – for inspiring this mission  
- [Uni](https://uni.com.ai) – for design guidance  
- Android SDK & Gemini team – for enabling developer-friendly AI access

---

## 💡 License

This project is open-source for educational and nonprofit agricultural innovation.  
© 2025 by [Ananya Inala]

---

## 🌾 Built for Farmers, Powered by AI

Agentic AI is more than a model — it's a **field assistant in your pocket.**
