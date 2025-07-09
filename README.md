# 🧠 Task 02 – Customer Segmentation using K-Means Clustering

This repository contains my submission for **Task 2** of the **SkillCraft Technology Machine Learning Internship**.

I implemented a **K-Means Clustering model** to group retail store customers based on their demographics and purchase behavior — and went a step further by integrating it with a clean, modern **frontend using HTML/CSS** and a **Flask backend API** for real-time prediction.

---

## 📌 Problem Statement

> "Build a K-Means clustering model to group customers of a retail store based on their purchase history."

---

## 💡 What I Did

✅ Built an end-to-end ML system with the following pipeline:

- 📊 **Preprocessing**
  - Encoded `Gender` (Male = 1, Female = 0)
  - Scaled features using `StandardScaler`

- 🧪 **Clustering**
  - Applied **K-Means algorithm** using scikit-learn
  - Determined optimal `k` using the **Elbow Method**
  - Evaluated clustering performance using **Silhouette Score**

- 📈 **Visualization**
  - PCA-based 2D plot of cluster separation
  - Analyzed each segment using group means

- 💻 **Web Deployment**
  - Created a responsive, animated HTML/CSS **frontend**
  - Built a **Flask backend API** for predictions
  - Integrated frontend and backend into one interactive app

---

## 📁 Project Structure

```
SCT_DS_2/
│
├── app.py                        # Flask backend with /predict API
├── index.html                    # Frontend UI (served by Flask)
├── scaler.pkl                    # Saved StandardScaler for input normalization
├── kmeans_model.pkl              # Trained KMeans model
├── Mall_Customers.csv            # Original dataset
├── Clustered_Customers.csv       # Dataset with cluster labels
├── customer_segmentation.ipynb   # Full model training notebook
└── README.md                     # You're here :)
```

---

## ⚙️ Technologies Used

- Python 3, Flask, NumPy, scikit-learn, Pandas
- HTML5, CSS3, Google Fonts, JS Fetch API
- Jupyter Notebook for modeling
- Joblib for model serialization
- RESTful API integration

---

## 🚀 How to Run the Project

### ✅ Step 1: Clone the repo & install dependencies

```bash
git clone https://github.com/medhajha810/SCT_DS_2.git
cd SCT_DS_2
pip install -r requirements.txt
```

> **Note:** Create a `requirements.txt` using  
> `pip freeze > requirements.txt` if needed.

---

### ✅ Step 2: Run the Flask App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## ✨ Features of the Web App

- 🔢 Input: Gender, Age, Annual Income, Spending Score
- ⚙️ Predicts real-time **customer cluster** using KMeans model
- 🎨 Beautiful, animated UI built from scratch with HTML/CSS
- ⚡ Fast API response via Flask backend

---

## 🧪 Testing Input Format (Frontend/Backend)

```json
POST /predict
Content-Type: application/json

{
  "gender": 1,
  "age": 28,
  "income": 54,
  "score": 70
}
```

Expected response:

```json
{
  "cluster": 3
}
```

---


## 🧠 Learnings from Task 2

- Practical implementation of **unsupervised learning**
- Evaluating clustering quality using **Elbow Method** and **Silhouette Score**
- Saving models and scalers for deployment
- Serving ML models through **Flask APIs**
- Building responsive frontends and full-stack ML integration

---

## 📬 Connect With Me

- 🔗 [LinkedIn – Medha Jha](https://linkedin.com/in/medhajha810)
- 🐙 GitHub: [@medhajha810](https://github.com/medhajha810)

---

## 🔖 Tags

`#SkillCraftInternship` `#KMeans` `#CustomerSegmentation` `#Flask` `#MachineLearning` `#HTMLCSS` `#FullStackML` `#PythonProject`
