# 💰 Expense Tracker

A simple and interactive **Expense Tracker** web app built with **Streamlit**, **Plotly**, and **Python**. Track your income and expenses, view your running balance, filter transaction history, and visualize spending by category — all in a clean, single-page dashboard.

---

## 📸 Screenshots

**Add a Transaction**

The main dashboard lets you log income or expenses with a category, amount, and description, and shows your running total balance.

**Transaction History & Charts**

Filter transactions by type (All / Income / Expenses) and generate category-wise bar and pie charts.

---

## ✨ Features

- ➕ **Add Transactions** — Log income or expenses with category, amount, and description
- 💵 **Running Balance** — Automatically updates total balance based on income/expenses
- 📜 **Transaction History** — View all logged transactions with timestamps
- 🔍 **Filter by Type** — Filter history to show All, Income, or Expenses only
- 📊 **Visual Insights** — Generate a category-wise bar chart and pie chart on demand
- 🗂️ **Session Details Viewer** — Expandable panel to inspect raw session state (useful for debugging)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | Web app framework / UI |
| [Plotly Express](https://plotly.com/python/plotly-express/) | Interactive bar & pie charts |
| Python `datetime` | Timestamping transactions |

---

## 📂 Project Structure

```
expense-tracker/
│
├── 1.py            # Main Streamlit application
└── README.md       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker

# Install dependencies
pip install streamlit plotly
```

### Run the App

```bash
streamlit run 1.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🖱️ How to Use

1. Select **Income** or **Expenses** from the dropdown.
2. Choose a **category** (Food, Cloth, Salary, Bill, Other).
3. Enter the **amount** and an optional **description**.
4. Click **Add Expenses** to log the transaction — your total balance updates instantly.
5. Use the **history filter** dropdown to view All / Income / Expenses transactions.
6. Click **chart generate** to view a category-wise bar chart and pie chart.
7. Expand **View All Session Details** to inspect the raw app state.

---

## 🔮 Planned / Upcoming Features

The following are written in the code but currently commented out — planned for a future update:

- 🗑️ Delete the last transaction
- ♻️ Reset all transactions

---

## 👤 Author

**Jaymin**
B.E. Information Technology | Aspiring Data Analyst

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
