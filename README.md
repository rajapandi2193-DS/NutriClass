# 🥗 NutriClass: Food Classification Using Nutritional Data

NutriClass is a machine learning project that classifies food items based on their nutritional attributes such as calories, protein, carbohydrates, fats, sugar, fiber, sodium, and other dietary indicators. The system predicts the **exact food name** for a given nutritional profile, enabling strict and automated diet planning.

---

## 📌 Project Overview

With growing dietary awareness, accurately identifying foods based on nutritional values is essential. This project builds a multi-class classification system using tabular nutritional data to label food items and analyze what distinguishes one food from another.

---

## 🎯 Problem Statement

Develop a machine learning model that classifies food into multiple classes using nutritional features. The model should accurately predict the food name and support real-time dietary decision-making.

---

## 💼 Business Use Cases

- Smart dietary recommendation systems  
- Health monitoring and nutrition planning tools  
- Food logging applications  
- Educational nutrition platforms  
- Grocery and meal planning applications  

---

## 🧠 Skills Gained

- Data Preprocessing  
- Feature Engineering  
- Multi-class Classification  
- Model Evaluation  
- Data Visualization  

---

## 🏥 Domain

Food & Nutrition / Machine Learning  

---

## 📂 Dataset

Tabular dataset containing:

- Calories  
- Protein  
- Fat  
- Carbs  
- Sugar  
- Fiber  
- Sodium  
- Cholesterol  
- Glycemic Index  
- Water Content  
- Serving Size  
- Meal Type  
- Preparation Method  
- Is_Vegan  
- Is_Gluten_Free  

Target Column:

- Food_Name  

Total Records: 31,387  
Number of Classes: 10  

---

## 🔍 Approach

### 1. Data Understanding & Exploration
- Inspect dataset structure  
- Analyze class distribution  
- View sample records  

### 2. Data Preprocessing
- Handle missing values  
- Remove duplicates  
- Normalize numerical features  

### 3. Feature Engineering
- Encode categorical columns  
- Scale numerical features  

### 4. Model Training
Trained and evaluated:
- Logistic Regression  
- K-Nearest Neighbors  
- Decision Tree  
- Random Forest  

### 5. Model Evaluation
- Accuracy  
- Precision  
- Recall  
- F1-score  

---

## 📊 Model Performance

| Model | Accuracy |
|-----|-----|
| Random Forest | 99.12% |
| Logistic Regression | 99.12% |
| KNN | 98.90% |
| Decision Tree | 98.58% |

**Selected Final Model:** Random Forest  

---

## 🏆 Results

- High accuracy across all classes  
- Reliable food name prediction  
- Suitable for real-time diet planning  

---

## 🧾 Folder Structure

NutriClass/
│
├── data/
│ └── food_dataset.csv.xlsx
│
├── notebooks/
│ └── nutriclass_eda.ipynb
│
├── models/
│ ├── nutriclass_model.pkl
│ ├── scaler.pkl
│ └── food_encoder.pkl
│
├── src/
├── results/
└── README.md


---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  

---

## 🚀 How to Run

1. Create virtual environment  
python -m venv venv
venv\Scripts\activate


2. Install dependencies  
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl


3. Open notebook  
jupyter notebook


4. Run `nutriclass_eda.ipynb`

---

## ✅ Conclusion

The NutriClass system successfully predicts food names based on nutritional values with high accuracy. It can be integrated into diet planning applications, health monitoring tools, and food logging systems for strict and personalized nutrition management.

---

## 👨‍💻 Author

Rajapandi
