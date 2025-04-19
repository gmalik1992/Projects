
# 🧾 Finance Data Extractor

A simple Streamlit-based UI application that extracts structured financial data from raw news articles using OpenAI's GPT API.

---

## 🚀 Features

- Accepts unstructured finance-related news articles as input
- Uses OpenAI's `gpt-4o` model to extract:
  - Company Name
  - Stock Symbol (with intelligent guesswork)
  - Revenue
  - Net Income
  - Earnings Per Share (EPS)
- Displays extracted data in a clean tabular format using Streamlit

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🖼️
- OpenAI API 🤖
- Pandas 📊

---

## 📸 Sample UI

![Finance Data Extractor UI]![](<Screenshot 2025-04-20 at 4.12.15 AM.png>)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gmalik1992/Projects.git
   cd Projects/finance-data-extractor
   ```

2. **Create a Conda environment (recommended)**
   ```bash
   conda create -n finance-extractor python=3.10
   conda activate finance-extractor
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**
   - Make sure you have an OpenAI API key from [platform.openai.com](https://platform.openai.com)
   - Add the following to your shell config or `.env`:
     ```bash
     export OPENAI_API_KEY=your_key_here
     ```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

This will open the app in your browser at `http://localhost:8501/`.

---

## 📁 Project Structure

```
finance-data-extractor/
│
├── main.py                   # Streamlit app
├── finance_data_extractor.py # Core logic for data extraction using OpenAI
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ✅ Example Input

```
The company reported a 10% increase in revenue for the quarter,
driven by strong sales of its flagship product, the iPhone.
The company also announced a new product, the iPhone 15.
```

## 🧠 Example Output

| Measure       | Values        |
|---------------|---------------|
| Company Name  | Apple         |
| Stock Symbol  | AAPL          |
| Revenue       | ...           |
| Net Income    | ...           |
| EPS           | ...           |

---

## 📬 Feedback

Feel free to open issues or pull requests to improve this tool!  
Made with ❤️ by [@gmalik1992](https://github.com/gmalik1992)
