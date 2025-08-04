# 📝 Devanagari Language Detection using Machine Learning

This project is a simple and effective Devanagari language detection system that identifies whether a given input text (written in Devanagari script) is in **Hindi**, **Marathi**, **Sanskrit**, or **Nepali**.

It includes:
- A machine learning pipeline using `CountVectorizer` and `MultinomialNB` for training.
- A web interface built with **Streamlit** for real-time language prediction.

---

## 📁 Dataset

The dataset used is a CSV file named `devanagari_language_dataset.csv` with the following format:

```csv
text,label
नमस्ते, Hindi
तुमचं स्वागत आहे, Marathi
...


🧠 Part 1: Training the Language Detection Model
🌐 Part 2: Streamlit Web App


📌 Project Structure
.
├── app.py                      # Streamlit web app
├── train_model.py             # Model training script
├── language_model.pkl         # Saved ML model
├── devanagari_language_dataset.csv  # Dataset
├── README.md                  # You're here!


Check our app : [devanagari-language-detector](https://devanagari-language-detector.streamlit.app/)