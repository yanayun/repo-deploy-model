# 🌸 Simple Deploy Model — Streamlit ML App

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45%2B-FF4B4B.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.6%2B-F7931E.svg)](https://scikit-learn.org/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-pompymandislian%2Fsimple--deploy--model-181717.svg?logo=github)](https://github.com/pompymandislian/simple-deploy-model)

Proyek ini mendemonstrasikan cara membuat dan mendeploy aplikasi Machine Learning interaktif berbasis web menggunakan **Streamlit**.

Repository ini memiliki 2 aplikasi:
1. **🌸 Iris Species Predictor (`sesi_6_iris_app.py`)**: Aplikasi prediksi spesies bunga Iris secara *real-time* dengan multi-model selection (Logistic Regression, Decision Tree, Random Forest, SVM), confidence score, dan chart probabilitas.
2. **🚀 Streamlit Basics (`sesi_6_streamlit_basics.py`)**: Panduan dan demo interaktif berbagai komponen UI dasar Streamlit (widget, formulir, plot, metrik, dan layout kolom).

---

## 📁 Struktur File

```text
simple-deploy-model/
├── README.md                   # Dokumentasi proyek
├── requirements.txt            # Daftar dependensi library
├── .gitignore                  # Filter file cache & lingkungan virtual
├── train_model.py              # Script otomatis latih & simpan model ML
├── sesi_6_iris_app.py          # Aplikasi web prediksi bunga Iris (Production App)
├── sesi_6_streamlit_basics.py  # Aplikasi web demo dasar-dasar Streamlit
├── iris_feature_names.txt      # Metadata nama fitur input
├── iris_target_names.txt       # Metadata nama target label
├── iris_logistic_model.pkl     # Model: Logistic Regression
├── iris_tree_model.pkl         # Model: Decision Tree
├── iris_forest_model.pkl       # Model: Random Forest
└── iris_svm_model.pkl          # Model: SVM (Support Vector Machine)
```

---

## 🚀 Panduan Inisialisasi & Upload Pertama Kali ke GitHub (Dari Nol)

Berikut adalah langkah-langkah lengkap dari awal yang digunakan untuk membuat repositori dan mengunggah proyek ini ke GitHub:

### 1. Buat Repositori Baru di GitHub
1. Masuk ke akun GitHub Anda dan buka: **[github.com/new](https://github.com/new)**.
2. Isi **Repository name**: `simple-deploy-model`.
3. Pilih opsi **Public**.
4. **PENTING:** Jangan centang *"Add a README file"*, *"Add .gitignore"*, atau lisensi (karena file-file ini sudah kita siapkan di komputer lokal).
5. Klik tombol hijau **"Create repository"**.

### 2. Jalankan Perintah Git di Terminal Komputer Lokal
Buka Terminal di dalam folder proyek Anda, lalu jalankan perintah berikut secara berurutan:

```bash
# 1. Inisialisasi git di folder lokal
git init

# 2. Masukkan semua file ke staging area
git add .

# 3. Buat commit pertama
git commit -m "Initial commit: Streamlit ML deployment and Iris app"

# 4. Pastikan branch utama bernama 'main'
git branch -M main

# 5. Hubungkan folder lokal ke repositori GitHub yang baru dibuat
git remote add origin https://github.com/pompymandislian/simple-deploy-model.git

# 6. Upload (push) seluruh file ke GitHub
git push -u origin main
```

---

## 🌐 Cara Deploy ke Streamlit Community Cloud (Gratis & Online)

Aplikasi ini dapat diakses secara publik melalui internet menggunakan layanan gratis **Streamlit Community Cloud**:

### Langkah-Langkah Deploy:
1. Kunjungi **[share.streamlit.io](https://share.streamlit.io/)** dan login menggunakan akun GitHub Anda (**@pompymandislian**).
2. Klik tombol **"Create app"** atau **"New app"**.
3. Pilih opsi **"I already have an app"**, lalu isi formulir deployment:
   - **Repository:** `pompymandislian/simple-deploy-model`
   - **Branch:** `main`
   - **Main file path:** `sesi_6_iris_app.py`
   - **App URL (Opsional):** Buat custom URL jika diinginkan (misal: `https://simple-deploy-model-pompy.streamlit.app`)
4. Klik tombol **"Deploy!"**.
5. Tunggu 1–2 menit saat Streamlit menginstall dependensi dari `requirements.txt`.
6. 🎉 **Aplikasi Anda sekarang sudah live di internet dan siap dibagikan!**

---

## ⚡ Panduan Menjalankan di Komputer Lokal

Jika ingin menjalankan aplikasi di komputer lokal:

### Step 1: Clone Repository
```bash
git clone https://github.com/pompymandislian/simple-deploy-model.git
cd simple-deploy-model
```

### Step 2: Buat & Aktifkan Virtual Environment (Disarankan)
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### Step 3: Install Dependensi
```bash
pip install -r requirements.txt
```

### Step 4: Siapkan Model ML & Metadata (Jika belum ada)
```bash
python train_model.py
```

### Step 5: Jalankan Aplikasi Streamlit

- **Menjalankan Aplikasi Prediksi Iris:**
  ```bash
  streamlit run sesi_6_iris_app.py
  ```
  Buka browser di: **`http://localhost:8501`**

- **Menjalankan Aplikasi Streamlit Basics:**
  ```bash
  streamlit run sesi_6_streamlit_basics.py
  ```
  Buka browser di: **`http://localhost:8501`**

- **Menjalankan Keduanya Bersamaan (di 2 terminal berbeda):**
  - Terminal 1: `streamlit run sesi_6_iris_app.py --server.port 8501`
  - Terminal 2: `streamlit run sesi_6_streamlit_basics.py --server.port 8502`

---

## 🔄 Cara Update & Push Perubahan Selanjutnya ke GitHub

Jika sewaktu-waktu Anda mengedit kode atau menambahkan fitur baru dan ingin memperbarui repositori GitHub:

```bash
# 1. Cek file yang berubah (opsional)
git status

# 2. Tambahkan semua file yang diedit
git add .

# 3. Buat catatan commit
git commit -m "Deskripsi perubahan yang Anda buat"

# 4. Push ke GitHub (Streamlit Cloud akan otomatis mendeteksi dan re-deploy)
git push origin main
```

---

## 🛠️ Tech Stack
- **Language:** Python
- **Web Framework:** [Streamlit](https://streamlit.io/)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/)
- **Model Storage:** [Joblib](https://joblib.readthedocs.io/)
- **Data & Visual:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/)

---

## 👤 Author
**Pompy Mandislian**
- GitHub: [@pompymandislian](https://github.com/pompymandislian)
- Repo: [simple-deploy-model](https://github.com/pompymandislian/simple-deploy-model)
