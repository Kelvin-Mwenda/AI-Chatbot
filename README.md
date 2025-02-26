# 🤖 AI Chatbot Project
Creating a simple AI chatbot

## 📌 Project Overview
The **AI Chatbot** is a Python-based chatbot designed to assist users with logical reasoning and mathematical queries. It leverages OpenAI's GPT model to provide well-structured responses. The project follows best practices, including the use of a virtual environment for dependency management.

---

## 🚀 Project Objectives & Achievements

### ✅ Objectives:
- Develop a chatbot capable of responding to user queries with logical and mathematical accuracy.
- Implement OpenAI's GPT model to generate structured responses.
- Utilize a virtual environment to ensure a clean and organized development setup.

### 🎯 Achievements:
- Successfully integrated OpenAI's GPT API for conversational responses.
- Created a structured Python script (`pyBot.py`) to handle user input and AI-generated responses.
- Implemented a `.gitignore` file to secure API keys and ignore unnecessary files.
- Used `requirements.txt` for easy dependency management.

---

## 📂 Project Structure

```plaintext
AI-Chatbot/
│── myenv/                     # Virtual environment (ignored in .gitignore)
│── Include/                    # System files (ignored)
│── Lib/                        # Dependencies (ignored)
│── Scripts/                    # Python environment scripts
│── .env                        # Environment variables (ignored)
│── .gitignore                  # Git ignore file
│── pyBot.py                    # Main chatbot script
│── pyvenv.cfg                  # Virtual environment configuration
│── requirements.txt             # Project dependencies

```

## 🔧 Installation Guide

Follow these steps to **download, set up, and run** the AI Chatbot on your local machine.

### 1️⃣ Clone the Repository
To get a local copy of the project, run:

```bash
    git clone https://github.com/Kelvin-Mwenda/AI-Chatbot.git
    cd AI-Chatbot
```

2️⃣ Set Up a Virtual Environment
A virtual environment ensures dependency isolation. Create and activate it:

On Windows:
```bash
    python -m venv myenv
    myenv\Scripts\activate
```

On macOS/Linux:
```bash
    python3 -m venv myenv
    source myenv/bin/activate
```

3️⃣ Install Dependencies
Use the requirements.txt file to install all required packages:
```bash
    pip install -r requirements.txt
```

4️⃣ Add Your OpenAI API Key
Create a .env file in the project directory and add your API key:
```bash
    OPENAI_API_KEY=your_api_key_here
```

5️⃣ Run the Chatbot
After setting up, execute the chatbot:
```bash
    python pyBot.py
```

### 🛠️ Features & Functionality
- Conversational AI: Uses OpenAI's GPT model for intelligent responses.
- Secure API Handling: API keys stored in .env for security.
- Dependency Management: Uses requirements.txt for easy installation.
- Virtual Environment: Ensures a clean development setup.
  
#❗ Important Notes
Ensure your API key is valid before running the chatbot.

If you encounter dependency issues, try upgrading pip:

```bash
    pip install --upgrade pip
```

Deactivate the virtual environment when done:
```bash
    deactivate
```

### 📌 Future Enhancements
- Add a graphical interface for better user interaction.
- Implement support for additional AI models.
- Enhance response handling for more complex queries.

  
### 📜 License
This project is open-source and available under the MIT License.

### 🤝 Contribution
Contributions are welcome! Feel free to submit a pull request or open an issue for discussion.

Happy coding! 🚀
