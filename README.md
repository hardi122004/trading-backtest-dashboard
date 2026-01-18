📈 Trading Strategy Backtesting Dashboard



An interactive web-based dashboard built using Python and Streamlit to backtest trading strategies on historical stock market data.  

The application allows users to visualize price movements, moving averages, trading signals, and evaluate strategy performance.



---



🚀 Features



\- 📊 Load historical stock price data from CSV files

\- 📈 Calculate moving averages (short-term and long-term)

\- 🔁 Generate buy and sell signals using moving average crossover strategy

\- 💹 Visualize price charts, signals, and equity curve

\- 📉 Analyze performance metrics such as returns and drawdowns

\- 🖥️ Interactive dashboard using Streamlit



---



🛠️ Tech Stack



\- \*\*Python\*\*

\- \*\*Pandas\*\* – Data processing \& analysis  

\- \*\*Matplotlib\*\* – Data visualization  

\- \*\*Streamlit\*\* – Interactive web dashboard  

\- \*\*NumPy\*\*



---



📂 Project Structure



```

trading-backtest-dashboard/

│

├── app.py                 # Streamlit dashboard

├── data\_cleaning.py       # Data preprocessing logic

├── reliance.py            # Stock data handling

├── stock\_data.csv         # Sample dataset

├── requirements.txt       # Project dependencies

└── README.md              # Project documentation

```



---



▶️ How to Run Locally



1️⃣ Clone the repository



```

git clone https://github.com/hardi122004/trading-backtest-dashboard.git

cd trading-backtest-dashboard

```



2️⃣ Create virtual environment (optional but recommended)



```

python -m venv venv

venv\\Scripts\\activate

```



3️⃣ Install dependencies



```

pip install -r requirements.txt

```



4️⃣ Run the dashboard



```

streamlit run app.py

```



5️⃣ Open in browser



```

http://localhost:8501

```



---



📌 Future Enhancements



\- Add more trading strategies (RSI, MACD, Bollinger Bands)

\- Upload CSV files directly from UI

\- Export backtest reports

\- Live market data integration

\- Improved UI/UX



---



👤 Author



\*\*Hardi Mody\*\*  

GitHub: https://github.com/hardi122004



---



⭐ If you like this project, give it a star!



