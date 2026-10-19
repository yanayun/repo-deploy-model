"""
Sesi 6 — AI Deployment 101: Iris Classification App

Aplikasi web interaktif untuk prediksi species Iris menggunakan model ML.
Model dilatih di sesi_4_ml_lite.ipynb dan di-load di sini.

Jalankan dengan: streamlit run iris_app.py
"""

from mlflow import tensorflow
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

from time import sleep


# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="Iris Species Predictor", page_icon="🌸", layout="centered"
)


# ============================================================================
# LOAD MODEL & DATA
# ============================================================================
@st.cache_resource
def load_model(model_type):
    """Load trained model based on type (cached for performance)"""
    try:
        sleep(2)  # Simulate loading time
        if model_type == "Logistic Regression":
            return joblib.load("iris_logistic_model.pkl")
        elif model_type == "Random Forest":
            return joblib.load("iris_forest_model.pkl")
        elif model_type == "SVM":
            return joblib.load("iris_svm_model.pkl")
        elif model_type == "neural network":
            return tensorflow.keras.models.load_model("iris_nn_model.h5")
        else:  # Decision Tree
            return joblib.load("iris_tree_model.pkl")
    except FileNotFoundError as e:
        st.error(
            f"❌ Model file not found! Please run sesi_4_ml_lite.ipynb first to train and save the models.\n\nError: {e}"
        )
        st.stop()


# def function_a():
#     pass

# def function_b():
#     pass


# function_a(function_b())


# @function_a # Python's decorator
# def function_b():
#     pass


# function_b() -> function_a(function_b())

# closure


@st.cache_resource
def load_metadata():
    """Load iris metadata (cached for performance)"""
    try:
        # Load feature and target names
        with open("iris_feature_names.txt", "r") as f:
            feature_names = [line.strip() for line in f.readlines()]

        with open("iris_target_names.txt", "r") as f:
            target_names = [line.strip() for line in f.readlines()]

        return feature_names, target_names
    except FileNotFoundError as e:
        st.error(f"❌ Metadata files not found!\n\nError: {e}")
        st.stop()


feature_names, target_names = load_metadata()

# ============================================================================
# HEADER
# ============================================================================
st.title("🌸 Iris Species Predictor")
st.markdown("**Powered by Machine Learning** | Built with ❤️ by AI Builders")
st.write("Masukkan ukuran bunga iris untuk memprediksi speciesnya.")

st.markdown("---")

# ============================================================================
# SIDEBAR: INFO & INSTRUCTIONS
# ============================================================================
st.sidebar.header("📖 About")
st.sidebar.info("""
**Iris Species Classification**

Model ini memprediksi 3 jenis bunga iris:
- 🌺 Setosa
- 🌻 Versicolor
- 🌼 Virginica

Berdasarkan 4 fitur:
- Sepal Length & Width
- Petal Length & Width
""")

st.sidebar.markdown("---")

# Model selection
st.sidebar.header("🤖 Model Selection")
model_choice = st.sidebar.selectbox(
    "Pilih model ML:",
    ["Logistic Regression", "Decision Tree", "Random Forest", "SVM"],
    help="Pilih algoritma yang akan digunakan untuk prediksi",
)

# # Load model on demand based on selection
# model = None
# if model_choice == "Logistic Regression":
#     model = joblib.load("iris_logistic_model.pkl")
# elif model_choice == "Random Forest":
#     model = joblib.load("iris_forest_model.pkl")
# elif model_choice == "SVM":
#     model = joblib.load("iris_svm_model.pkl")
# elif model_choice == "neural network":
#     model = tensorflow.keras.models.load_model("iris_nn_model.h5")
# else:  # Decision Tree
#     model = joblib.load("iris_tree_model.pkl")

model = load_model(model_choice)  # Load model based on selection

# Set model info based on selection
if model_choice == "Logistic Regression":
    model_info = "📊 Logistic Regression - Model linear untuk klasifikasi"
else:
    model_info = "🌳 Decision Tree - Model berbasis aturan keputusan"

st.sidebar.info(model_info)

st.sidebar.markdown("---")
st.sidebar.markdown("**Fullstack Bangalore**")
st.sidebar.markdown("📷 @fullstackbangalore")

# ============================================================================
# INPUT FORM
# ============================================================================
st.subheader("🔧 Input Features")
st.write("Sesuaikan nilai di bawah ini:")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider(
        "Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.8, step=0.1
    )
    sepal_width = st.slider(
        "Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.0, step=0.1
    )

with col2:
    petal_length = st.slider(
        "Petal Length (cm)", min_value=1.0, max_value=7.0, value=4.3, step=0.1
    )
    petal_width = st.slider(
        "Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.3, step=0.1
    )

# Create input array for prediction
input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Display input as dataframe
input_df = pd.DataFrame(input_features, columns=feature_names)
st.write("**Input yang akan diprediksi:**")
st.dataframe(input_df, width="stretch")

st.markdown("---")

# ============================================================================
# PREDICTION
# ============================================================================
st.subheader("🎯 Prediction Result")

# Show active model
st.info(f"**Active Model:** {model_choice}")

if st.button("🚀 Predict Species", type="primary"):
    with st.spinner("Model sedang berpikir..."):
        # Make prediction
        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0]

        predicted_species = target_names[prediction]
        confidence = prediction_proba[prediction] * 100

        # Display result with emoji
        species_emoji = {"setosa": "🌺", "versicolor": "🌻", "virginica": "🌼"}
        emoji = species_emoji.get(predicted_species, "🌸")

        st.success(f"### {emoji} Predicted Species: **{predicted_species.upper()}**")
        st.metric("Confidence", f"{confidence:.1f}%")

        # Show probability distribution
        st.write("**Probability Distribution:**")
        prob_df = pd.DataFrame(
            {
                "Species": target_names,
                "Probability": [f"{p * 100:.1f}%" for p in prediction_proba],
            }
        )
        st.dataframe(prob_df, width="stretch")

        # Visual: bar chart of probabilities
        st.bar_chart(
            pd.DataFrame({"Probability": prediction_proba}, index=target_names)
        )

        st.balloons()

st.markdown("---")

# ============================================================================
# SAMPLE DATA REFERENCE
# ============================================================================
with st.expander("📊 Lihat Sample Data Iris"):
    st.write("Referensi rentang nilai dari dataset Iris:")
    iris = load_iris(as_frame=True)
    sample = iris.frame.sample(10).copy()
    sample["species"] = sample["target"].map(lambda i: iris.target_names[i])
    st.dataframe(sample[feature_names + ["species"]], width="stretch")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.caption("✅ AI kamu sekarang hidup di web! Share link ini ke teman-teman.")
st.caption(
    "💡 **Reflection:** Apa yang membuat AI ini bermanfaat? Bagaimana cara improve-nya?"
)
