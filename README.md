
# SmartTestFramework — Archive Installer

This is a **Streamlit-based installer UI** for downloading and exploring archived versions of the **SmartTestFramework**.
The app provides a clean, interactive interface to:

* Browse available framework versions
* Download the latest package directly from GitHub
* Quickly check usage instructions
* Access live demo & documentation

---

## Features

* **Version Selector** – Browse framework versions in a scrollable card view
* **One-Click Download** – Directly grab the latest `.zip` package from GitHub
* **Quick Usage Guide** – Inline instructions to launch and run tests
* **Demo & More Info Links** – Jump to the hosted demo app or GitHub docs

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
pip install -r requirements.txt
```

---

## ▶️ Running the App

Run locally with:

```bash
streamlit run main.py
```

The app will start on `http://localhost:8501/`.

---

## 📋 Requirements

Dependencies are listed in `requirements.txt`:

```
streamlit
requests
```
