# AyurSage

## 🌿 Overview
**AyurSage** is an AI-powered Ayurvedic recommendation system that provides personalized health suggestions based on symptoms and diseases. It leverages Groq API and advanced AI models to offer natural remedies rooted in Ayurvedic knowledge.

## 🚀 Features
- Accepts user-input symptoms and diseases.
- Provides Ayurvedic-based treatment recommendations.
- Utilizes AI models for accurate and contextual suggestions.
- User-friendly interface built with **Streamlit**.

## 🛠 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DhruvShirsath/AyurSage-AI.git
   cd AyurSage-AI
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate     # On Windows (Command Prompt)
   ```
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On macOS/Linux
   ```
   ```bash
   python -m venv myenv
   myenv\Scripts\Activate.ps1  # On Windows (PowerShell)
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚡ Usage

1. **Set up API Key**
   - Create a `.env` file in the project root.
   - Add your Groq API key:
     ```
     GROQ_API_KEY = "your_api_key_here"
     ```

2. **Run the Application:**
   ```bash
   streamlit run AyurSage.py
   ```

3. **Enter Symptoms/Disease:**
   - Input symptoms like "fever, cough, headache".
   - Optionally, provide a disease name.
   - Get Ayurvedic treatment recommendations.

## 🔒 Security & Environment Variables
- Never expose your **GROQ_API_KEY** in public repositories.
- Store sensitive credentials in a `.env` file.
- Add `.env` and `myenv/` to `.gitignore` to prevent accidental commits.

## 🎯 Future Enhancements
- Adding more detailed Ayurvedic treatment insights.
- Voice-based symptom input.
- Integration with additional AI models for improved accuracy.

## 🤝 Contributing
We welcome contributions! Feel free to fork the repo, create a branch, and submit a PR.

## 📜 License
This project is open-source and licensed under the **MIT License**.

## 📞 Contact
For any queries or suggestions, reach out to **Dhruv Shirsath** via GitHub.

