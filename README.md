# 📚 Topic-based AI Question Generator & Evaluator

### 📖 Overview
This project is an **AI-powered learning assistant** built with **Streamlit** and **OpenAI GPT** models.  
It allows users to:
- **Generate** creative, diverse, and difficulty-graded questions for any given topic or word.
- **Evaluate** their answers and get AI-based scoring and feedback.

The goal is to make topic-based self-assessment quick, engaging, and interactive for **students**, **teachers**, and **self-learners**.

---

### ✨ Features
- **AI Question Generation**: Creates **10 diverse questions** ranging from easy to hard for a given topic.
- **AI Answer Evaluation**: Scores answers out of 100, showing correct and incorrect questions.
- **Download Support**: Export generated questions as `.txt`.
- **Interactive UI**: Two-tab interface using **Streamlit**.
- **Configurable Model**: Easily switch between `gpt-4` and `gpt-3.5-turbo`.

---

## ⚙️ Installation
```
1️⃣ Clone the Repository
bash
git clone https://github.com/your-username/ai-question-evaluator.git
cd ai-question-evaluator
2️⃣ Create & Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
```

### 🔧 Setup

1️⃣ Add Your OpenAI API Key
Create a .env file in the project root:
env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here

2️⃣ Run the App
bash
Copy
Edit
streamlit run main.py

### 🖥 Usage

Tab 1: Question Generator
Enter a topic or word (e.g., "Artificial Intelligence").

Click Enter to get 10 AI-generated questions.

Download questions if needed.

Tab 2: Evaluator
Paste your answers to the generated questions.

Click Submit to get:

Total Score (out of 100)

Correct Questions

Incorrect Questions

### ⚙️ Configuration

You can adjust settings inside the app.py and evaluate.py:

Model: Change "gpt-4" to "gpt-3.5-turbo" for faster/cheaper results.

Temperature: Adjust creativity (0.0 = more factual, 1.0 = more creative).

Max Tokens: Control the output size.

### 🏗 Architecture
```
bash
Copy
Edit
📂 ai-question-evaluator
│
├── app.py            # Question generator logic using OpenAI API
├── evaluate.py       # Answer evaluation logic
├── main.py           # Streamlit UI with two tabs
├── .env              # API key storage (ignored in Git)
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```
Flow:

User inputs topic ➡ app.py calls OpenAI ➡ Generates questions.

User inputs answers ➡ evaluate.py calls OpenAI ➡ Scores and feedback.

Results displayed in Streamlit interface.

### 🔒 Safety & Disclaimer

AI Limitations: The evaluation is subjective and based on AI interpretation, which may not always be accurate.

Not a Replacement for Teachers: Use this as a study aid, not a grading system for official assessments.

Data Privacy: No answers are stored — only processed in real-time.

API Costs: Each request to OpenAI consumes API credits. Use wisely.

### 🚀 Future Enhancements

✅ Multiple-choice question generation.

✅ Leaderboard system for competitive quizzes.

✅ User authentication & answer history tracking.

✅ PDF export of questions & results.

✅ Multi-topic quiz creation in one session.

✅ Offline mode with locally stored Q&A sets.
