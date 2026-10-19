"""
Sesi 6 — AI Deployment 101: Streamlit Basics

Demo komponen dasar Streamlit untuk membuat web app interaktif.
Jalankan dengan: streamlit run streamlit_basics.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================================
# 1) PAGE CONFIG & TITLE
# ============================================================================
st.set_page_config(
    page_title="Streamlit Basics Demo", page_icon="🚀", layout="centered"
)

st.title("🚀 Welcome to Streamlit Basics")
st.write(
    "**Tagline:** From code to app in minutes. Learn Streamlit fundamentals to build interactive web apps for your AI projects."
)

st.markdown("---")

st.markdown("""
# Ini title gede
## Ini subtitle kecil
### Ini sub-subtitle lebih kecil
###### Ini sub-subtitle paling kecil

**Bold text**  
*Italic text*  
`Code snippet`

`inline code snippet`

```python
print("Hello, Streamlit!")
```            

```python
def hello_world():
    print("Hello, Streamlit!")
```
            
```javascript
function helloWorld() {
    console.log("Hello, Streamlit!");
}
```
""")

# ============================================================================
# 2) TEXT & MARKDOWN
# ============================================================================
st.header("1️⃣ Text & Markdown")
st.write("Streamlit allows you to write text easily:")
st.markdown("""
- **Bold text**
- *Italic text*
- `Code snippet`
- [Link to docs](https://docs.streamlit.io)
""")

st.markdown("---")

# ============================================================================
# 3) INPUT WIDGETS
# ============================================================================
st.header("2️⃣ Input Widgets")

# Text input
user_name = st.text_input("Masukkan nama kamu:", placeholder="e.g., Budi")
if user_name:
    st.success(f"Halo, **{user_name}**! Selamat datang di dunia AI Deployment.")

st.warning(
    "⚠️ Ini hanya demo, data kamu tidak akan disimpan atau digunakan untuk apa pun."
)
st.error("❌ Jangan masukkan informasi sensitif atau pribadi di sini!")

# Slider
age = st.slider("Pilih umur kamu:", min_value=15, max_value=60, value=25, step=1)
st.info(f"Umur yang dipilih: **{age}** tahun")

# Slider
water_ph = st.slider(
    "Pilih pH air:", min_value=0.0, max_value=14.0, value=7.0, step=0.1
)
st.info(f"pH air yang dipilih: **{water_ph}**")

# Select box
favorite_language = st.selectbox(
    "Bahasa pemrograman favorit:", ["Python", "JavaScript", "Java", "C++", "Go"]
)
st.write(f"Kamu memilih: **{favorite_language}**")

# Checkbox
show_data = st.checkbox("Tampilkan data sample?")
if show_data:
    sample_data = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie"],
            "Score": [85, 92, 78],
            "Pass": [True, False, True],
        }
    )
    st.dataframe(sample_data)

st.markdown("---")

# Radio
gender = st.radio("Pilih jenis kelamin:", ["Laki-laki", "Perempuan", "Lainnya"])
st.write(f"Jenis kelamin yang dipilih: **{gender}**")

# segmented control
option = st.segmented_control(
    "Pilih opsi:",
    options=["Option 1", "Option 2", "Option 3"],
    default="Option 2",
)
st.write(f"Opsi yang dipilih: **{option}**")


# multiselect
hobbies = st.multiselect(
    "Pilih hobi kamu:",
    options=["Membaca", "Olahraga", "Memasak", "Traveling", "Coding"],
)
if len(hobbies) > 0:
    st.write(f"Hobi yang dipilih: **{', '.join(hobbies)}**")


# example of tiered input using loop
features = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
input_values = {}
for idx, feature in enumerate(features):
    if idx > 0:
        if not input_values[features[idx - 1]]:
            st.warning(f"⚠️ Harap isi {features[idx - 1]} terlebih dahulu.")
            break

    input_values[feature] = st.slider(
        f"{feature} (cm)", min_value=0.0, max_value=10.0, value=None, step=0.1
    )
    st.write(f"{feature}: **{input_values[feature]}**")

st.markdown("---")
st.markdown("""Berdasarkan 4 fitur:
- Sepal Length & Width
- Petal Length & Width
""")
st.json(input_values)


inputs = {
    "iris": {
        "sepal_length_2": {"form_input": "slider", "min": 4.0, "max": 8.0, "step": 0.1},
        "sepal_width_2": {"form_input": "slider", "min": 2.0, "max": 4.5, "step": 0.1},
        "petal_length_2": {"form_input": "slider", "min": 1.0, "max": 7.0, "step": 0.1},
        "petal_width_2": {"form_input": "slider", "min": 0.1, "max": 2.5, "step": 0.1},
    },
    "titanic": {
        "age": {"form_input": "slider", "min": 0, "max": 100, "step": 1},
        "fare": {"form_input": "slider", "min": 0.0, "max": 500.0, "step": 0.1},
        "pclass": {"form_input": "selectbox", "options": [1, 2, 3]},
    },
    "house_price": {
        "num_rooms": {"form_input": "slider", "min": 1, "max": 10, "step": 1},
        "area": {"form_input": "slider", "min": 100.0, "max": 10000.0, "step": 10.0},
        "location": {
            "form_input": "selectbox",
            "options": ["Downtown", "Suburb", "Rural"],
        },
    },
    "air_quality": {
        "pm25": {"form_input": "slider", "min": 0.0, "max": 500.0, "step": 0.1},
        "pm10": {"form_input": "slider", "min": 0.0, "max": 500.0, "step": 0.1},
        "o3": {"form_input": "slider", "min": 0.0, "max": 300.0, "step": 0.1},
    },
}


def resolve_input(feature_name, feature_info):
    if feature_info["form_input"] == "slider":
        return st.slider(
            feature_name,
            min_value=feature_info["min"],
            max_value=feature_info["max"],
            step=feature_info["step"],
            value=None,
        )
    elif feature_info["form_input"] == "selectbox":
        return st.selectbox(feature_name, options=feature_info["options"])
    else:
        st.error(f"Unknown form input type for {feature_name}")
        return None


st.markdown("---")
st.markdown("""Pilih dataset di sidebar untuk melihat input yang relevan.
- Iris: Sepal Length & Width, Petal Length & Width
- Titanic: Age, Fare, Pclass
- House Price: Number of Rooms, Area, Location
""")

selected_dataset = st.sidebar.radio("Pilih dataset:", options=list(inputs.keys()))
st.markdown("---")
feature_inputs = inputs[selected_dataset]
input_values_2 = {}
for idx, (feature_name, feature_input) in enumerate(feature_inputs.items()):
    if idx > 0:
        if not input_values_2[list(feature_inputs.keys())[idx - 1]]:
            st.warning(
                f"⚠️ Harap isi {list(feature_inputs.keys())[idx - 1]} terlebih dahulu."
            )
            break

    input_values_2[feature_name] = resolve_input(feature_name, feature_input)


# ============================================================================
# 4) BUTTON & INTERACTION
# ============================================================================
st.header("3️⃣ Button & Interaction")

if st.button("Klik saya untuk generate random number"):
    random_num = np.random.randint(1, 100)
    # st.balloons()  # celebratory animation
    st.snow()
    st.success(f"🎲 Angka random: **{random_num}**")

st.markdown("---")

# ============================================================================
# 5) VISUALIZATION
# ============================================================================
st.header("4️⃣ Visualization")

num_points = st.slider("Jumlah data points:", 10, 200, 50)
x = np.linspace(0, 10, num_points)
y = np.sin(x) + np.random.normal(0, 0.1, num_points)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, marker="o", linestyle="-", markersize=3, alpha=0.7)
ax.set_title("Sine Wave with Noise")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True, alpha=0.3)

st.sidebar.pyplot(fig)

st.markdown("---")

# ============================================================================
# 6) COLUMNS LAYOUT
# ============================================================================
st.header("5️⃣ Layout: Columns")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "94.5%", delta="2.1%")

with col2:
    st.metric("Precision", "91.2%", delta="-0.5%")

with col3:
    st.metric("Recall", "89.8%", delta="1.3%")

st.markdown("---")

# ============================================================================
# 7) SIDEBAR
# ============================================================================
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Gunakan sidebar untuk kontrol tambahan.")

theme = st.sidebar.radio("Pilih tema:", ["Light", "Dark", "Auto"])
st.sidebar.info(f"Tema dipilih: **{theme}**")

st.sidebar.markdown("---")
st.sidebar.markdown("**Fullstack Bangalore**")
st.sidebar.markdown("📷 @fullstackbangalore")

# ============================================================================
# CLOSING
# ============================================================================
st.markdown("---")
st.success("✅ Selamat! Kamu sudah melihat komponen dasar Streamlit.")
st.write("**Next step:** Integrasikan model AI kamu ke Streamlit app.")


# after

## train
# data = load_data()

# pipeline = Pipeline([preprocess(), split(), Model.fit()])
# pipeline.fit(data)

# pipeline.save("pipeline.pkl")

# ## inference
# pipeline = Pipeline.load()

# X = input()
# prediction = pipeline.predict(X)
