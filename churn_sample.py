import streamlit as st
import pandas as pd
import joblib
import io

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# Custom CSS
# ------------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

.title{
    font-size:38px;
    font-weight:bold;
    color:#0E4C92;
}

.subtitle{
    font-size:18px;
    color:gray;
}

.stButton>button{
    width:100%;
    background:#0E4C92;
    color:white;
    border-radius:8px;
    height:50px;
    font-size:18px;
}

.stDownloadButton>button{
    width:100%;
}

.pred{
    padding:20px;
    border-radius:10px;
    background:#EAF4FF;
    border-left:8px solid #0E4C92;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# Load Model
# ------------------------------
@st.cache_resource
def load_model():
    return joblib.load("best_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error(f"Unable to load model.\n\n{e}")
    st.stop()

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("📊 Customer Churn Prediction")

st.sidebar.info("""
### Decision Tree Pipeline

✔ StandardScaler

✔ Decision Tree

✔ Probability Prediction

✔ Download Results
""")

st.sidebar.success("Model Loaded Successfully")

# ------------------------------
# Title
# ------------------------------
st.markdown("<p class='title'>Customer Churn Prediction</p>",
            unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Enter customer information to predict churn.</p>",
            unsafe_allow_html=True)

# ------------------------------
# Input Form
# ------------------------------
with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        account_length = st.number_input(
            "Account Length", 0, 500, 100)

        international_plan = st.selectbox(
            "International Plan",
            ["No", "Yes"]
        )

        voice_mail_plan = st.selectbox(
            "Voice Mail Plan",
            ["No", "Yes"]
        )

        total_day_minutes = st.number_input(
            "Total Day Minutes", 0.0, 500.0, 180.0)

        total_day_calls = st.number_input(
            "Total Day Calls", 0, 300, 100)

        total_eve_minutes = st.number_input(
            "Total Evening Minutes", 0.0, 500.0, 200.0)

        total_eve_calls = st.number_input(
            "Total Evening Calls", 0, 300, 100)

    with col2:

        total_night_minutes = st.number_input(
            "Total Night Minutes", 0.0, 500.0, 200.0)

        total_night_calls = st.number_input(
            "Total Night Calls", 0, 300, 100)

        total_intl_minutes = st.number_input(
            "Total International Minutes", 0.0, 50.0, 10.0)

        total_intl_calls = st.number_input(
            "Total International Calls", 0, 50, 4)

        customer_service_calls = st.number_input(
            "Customer Service Calls", 0, 20, 1)

        state = st.selectbox(
            "State",
            [
                "AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA",
                "HI","IA","ID","IL","IN","KS","KY","LA","MA","MD",
                "ME","MI","MN","MO","MS","MT","NC","ND","NE","NH",
                "NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC",
                "SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"
            ]
        )

        revenue = st.selectbox(
            "Revenue Segment",
            ["Low", "Medium", "High"]
        )

    predict = st.form_submit_button("Predict")

# ------------------------------
# Prediction
# ------------------------------
if predict:

    try:

        total_charges = (
            total_day_minutes*0.17 +
            total_eve_minutes*0.085 +
            total_night_minutes*0.045 +
            total_intl_minutes*0.27
        )

        total_usage = (
            total_day_minutes +
            total_eve_minutes +
            total_night_minutes +
            total_intl_minutes
        )

        service_stress = (
            customer_service_calls *
            (1 if international_plan == "Yes" else 0)
        )

        row = {}

        for col in model.feature_names_in_:
            row[col] = 0

        row["Account length"] = account_length
        row["International plan"] = 1 if international_plan == "Yes" else 0
        row["Voice mail plan"] = 1 if voice_mail_plan == "Yes" else 0
        row["Total day minutes"] = total_day_minutes
        row["Total day calls"] = total_day_calls
        row["Total eve minutes"] = total_eve_minutes
        row["Total eve calls"] = total_eve_calls
        row["Total night minutes"] = total_night_minutes
        row["Total night calls"] = total_night_calls
        row["Total intl minutes"] = total_intl_minutes
        row["Total intl calls"] = total_intl_calls
        row["Customer service calls"] = customer_service_calls
        row["Total Charges"] = total_charges
        row["Total_Usage"] = total_usage
        row["Service_Stress"] = service_stress

        state_col = f"State_{state}"
        if state_col in row:
            row[state_col] = 1

        if revenue == "Medium":
            row["Revenue_Segment_Medium"] = 1

        elif revenue == "High":
            row["Revenue_Segment_High"] = 1

        X = pd.DataFrame([row])

        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0]

        st.markdown("---")

        if prediction == 1:
            st.error("⚠ Customer is likely to Churn")
        else:
            st.success("✅ Customer is likely to Stay")

        st.markdown(
            f"""
            <div class='pred'>
            <h3>Prediction Probability</h3>

            Stay : <b>{probability[0]*100:.2f}%</b><br>

            Churn : <b>{probability[1]*100:.2f}%</b>

            </div>
            """,
            unsafe_allow_html=True
        )

        result = pd.DataFrame({
            "Prediction":[prediction],
            "Stay Probability":[probability[0]],
            "Churn Probability":[probability[1]]
        })

        csv = result.to_csv(index=False).encode()

        st.download_button(
            "📥 Download Prediction",
            csv,
            "prediction.csv",
            "text/csv"
        )

    except Exception as e:
        st.error(f"Prediction Error\n\n{e}")