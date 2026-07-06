# 📊 Customer Churn Prediction using Machine Learning

A professional **Customer Churn Prediction** web application built with **Streamlit** and powered by a trained **Decision Tree Classifier Pipeline**. The application predicts whether a customer is likely to churn based on their account and usage information.

---

## 🚀 Features

* Modern and responsive Streamlit interface
* Interactive customer input form
* Decision Tree Pipeline (`best_model.pkl`)
* Real-time churn prediction
* Prediction probability (Stay vs. Churn)
* Download prediction results as CSV
* Error handling for smooth user experience
* Easy deployment on Streamlit Community Cloud

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

## 📂 Project Structure

```text
Customer_Churn_App/
│── app.py
│── best_model.pkl
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

---

## 📥 Input Features

The application accepts customer information such as:

* Account Length
* International Plan
* Voice Mail Plan
* Total Day Minutes
* Total Day Calls
* Total Evening Minutes
* Total Evening Calls
* Total Night Minutes
* Total Night Calls
* Total International Minutes
* Total International Calls
* Customer Service Calls
* State
* Revenue Segment

---

## 📈 Output

The model provides:

* Customer Churn Prediction
* Prediction Probability
* Stay Probability
* Churn Probability
* Downloadable CSV report

---

## 📊 Machine Learning Model

* Algorithm: Decision Tree Classifier
* Model Type: Scikit-learn Pipeline
* Saved Model: `best_model.pkl`

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

This project can be deployed on:

* Streamlit Community Cloud
* Render
* Railway
* Hugging Face Spaces
* AWS EC2
* Azure App Service

---

## 🤝 Contributing

Contributions, feature requests, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abdul Kadir**

If you found this project helpful, consider giving it a ⭐ on GitHub.
