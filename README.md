# AyurSage

[![Streamlit App](https://img.shields.io/badge/Live%20App-AyurSage-blue?style=for-the-badge)](https://ayursage.streamlit.app/)

## 🌿 Overview
**AyurSage** is an AI-powered Ayurvedic recommendation system that provides personalized health suggestions based on symptoms and diseases. It leverages the **Groq API** and advanced AI models to offer natural remedies rooted in Ayurvedic knowledge.

## 🚀 Live Demo
Check out the deployed version here:  
🔗 [AyurSage - Streamlit App](https://ayursage.streamlit.app/)

## 🚀 Features
- Accepts user-input symptoms and diseases.
- Provides Ayurvedic-based treatment recommendations.
- Utilizes AI models for accurate and contextual suggestions.
- User-friendly interface built with **Streamlit**.

## 🛠 Installation

### 1️⃣ Clone the Repository:
```bash
git clone https://github.com/DhruvShirsath/AyurSage-AI.git
cd AyurSage-AI
```

### 2️⃣ Create a Virtual Environment (Recommended):

#### 🔹 On Windows (Command Prompt):
```bash
python -m venv myenv
myenv\Scripts\activate
```
#### 🔹 On Windows (PowerShell):
```powershell
python -m venv myenv
myenv\Scripts\Activate.ps1
```
#### 🔹 On macOS/Linux:
```bash
python -m venv myenv
source myenv/bin/activate
```

### 3️⃣ Install Dependencies:
```bash
pip install -r requirements.txt
```

## ⚡ Usage

### 1️⃣ Set Up API Key
- Create a `.env` file in the project root.
- Add your Groq API key:
  ```
  GROQ_API_KEY="your_api_key_here"
  ```

### 2️⃣ Run the Application:
```bash
streamlit run AyurSage.py
```

### 3️⃣ Enter Symptoms/Disease:
- Input symptoms like "fever, cough, headache".
- Optionally, provide a disease name.
- Get Ayurvedic treatment recommendations instantly.

## 🔒 Security & Environment Variables
- **Never expose your `GROQ_API_KEY` in public repositories.**
- Store sensitive credentials in a `.env` file.
- Add `.env` and `myenv/` to `.gitignore` to prevent accidental commits.
- If deploying on **Streamlit Cloud**, add the API key under `st.secrets` instead of `.env`.

## 🎯 Future Enhancements
✅ Expanding the Ayurvedic treatment database for more conditions.  
✅ Implementing **voice-based symptom input** for a hands-free experience.  
✅ Integrating **LLM-based reasoning** for improved treatment accuracy.  
✅ Enhancing UI with **charts and visuals** for better recommendations.  

## 🤝 Contributing
We welcome contributions! Feel free to fork the repo, create a branch, and submit a PR.

## 📜 License
This project is open-source and licensed under the **MIT License**.

## 📞 Contact
For any queries or suggestions, reach out to **Dhruv Shirsath** via [GitHub](https://github.com/DhruvShirsath).

