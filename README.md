📊 NSU Datathon Practice Project
🧠 Project Overview

This repository contains my practice work for the NSU Datathon.
The goal of this project is to build a strong foundation in Machine Learning workflow, including data handling, preprocessing, model training, and evaluation using Python.

🎯 Objectives
Learn how to load and process datasets using Pandas
Understand basic Machine Learning pipeline
Train classification models using Scikit-learn
Handle common Python/ML errors during development
Prepare for competitive Datathon environments
🛠️ Tech Stack
Python 🐍
Pandas
NumPy
Scikit-learn
📂 Project Structure
Datathon_Practice_NSU/
│
├── Main.py          # Main ML script
├── student.csv      # Dataset file
└── README.md        # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/Datathon_Practice_NSU.git
cd Datathon_Practice_NSU
2️⃣ Install dependencies
pip install pandas numpy scikit-learn
3️⃣ Run the project
python Main.py
📊 Workflow
Load dataset (student.csv)
Preprocess data using Pandas
Split features and labels
Train ML model (e.g., Decision Tree / Classifier)
Evaluate model performance
⚠️ Common Issues & Fixes
❌ FileNotFoundError

Make sure your dataset path is correct:

df = pd.read_csv("student.csv")
❌ sklearn warning (feature mismatch)

Ensure training and prediction data have same feature structure.

🚀 Future Improvements
Add multiple ML models (Random Forest, SVM)
Improve accuracy with feature engineering
Add data visualization (Matplotlib / Seaborn)
Deploy model as a simple web app
👨‍💻 Author

Tonmoy Dey
CSE Student, American International University-Bangladesh (AIUB)

⭐ Note

This project is part of my learning journey in Machine Learning and Datathon preparation.
