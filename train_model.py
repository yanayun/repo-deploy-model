"""
Script untuk melatih dan mengekspor model serta metadata dataset Iris.
Dibutuhkan sebelum menjalankan sesi_6_iris_app.py
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib


def main():
    print("🌸 Memuat dataset Iris...")
    iris = load_iris()

    # 1. Simpan metadata fitur dan target
    print("📝 Menyimpan metadata...")
    with open("iris_feature_names.txt", "w") as f:
        f.write("\n".join(iris.feature_names))
    print("  ✓ iris_feature_names.txt tersimpan")

    with open("iris_target_names.txt", "w") as f:
        f.write("\n".join(iris.target_names))
    print("  ✓ iris_target_names.txt tersimpan")

    # 2. Latih dan simpan model
    print("🤖 Melatih dan menyimpan model ML...")
    models = {
        "iris_logistic_model.pkl": LogisticRegression(max_iter=200),
        "iris_tree_model.pkl": DecisionTreeClassifier(),
        "iris_forest_model.pkl": RandomForestClassifier(),
        "iris_svm_model.pkl": SVC(probability=True),
    }

    for filename, model in models.items():
        model.fit(iris.data, iris.target)
        joblib.dump(model, filename)
        print(f"  ✓ {filename} berhasil disimpan")

    print("\n🎉 Selesai! Semua file siap. Jalankan aplikasi dengan:")
    print("   streamlit run sesi_6_iris_app.py")


if __name__ == "__main__":
    main()
