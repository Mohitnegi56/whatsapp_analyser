# 📊 WhatsApp Chat Analyzer

A powerful and interactive **Streamlit web app** to analyze WhatsApp chats and uncover meaningful insights from exported `.txt` files.

👉 **Live App:**  
https://whatsappanalyser-7mxtgbpbvxsytrdynkujd5.streamlit.app/

---

## ✨ Overview

WhatsApp Chat Analyzer helps you understand communication patterns in **personal or group chats**.  
Upload your exported WhatsApp chat file and instantly get visual statistics, trends, and insights — no coding required.

---

## 🚀 Features

- 📁 Upload WhatsApp chat `.txt` files  
- 👤 User-wise & overall chat analysis  
- ✉️ Message, word, media & link statistics  
- 📆 Daily and monthly activity timelines  
- 🗓️ Weekly & monthly activity analysis  
- 🌡️ Interactive activity heatmaps  
- 😊 Emoji usage analysis  
- ☁️ WordCloud visualization  
- 📊 Clean and responsive UI built with Streamlit  

---

## 📁 How to Export WhatsApp Chat

1. Open WhatsApp  
2. Select any chat (group or personal)  
3. Tap **⋮ (three dots)** → **More** → **Export Chat**  
4. Choose **Without media**  
5. Upload the downloaded `.txt` file to the app  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **WordCloud**
- **NLTK**
- **Emoji**
- **URLExtract**

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/Mohitnegi56/whatsapp_analyser.git
cd whatsapp_analyser
pip install -r requirements.txt
streamlit run app.py
