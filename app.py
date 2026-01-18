import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Trading Strategy Backtesting Dashboard",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("📈 Trading Strategy Backtesting Dashboard")
st.divider()

# -------------------- DATA LOADING --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("stock_data.csv")

    # Cleaning (Yahoo-style CSV)
    df = df.iloc[2:].reset_index(drop=True)
    df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

    df['Date'] = pd.to_datetime(df['Date'])
    df[['Close','High','Low','Open','Volume']] = df[
        ['Close','High','Low','Open','Volume']
    ].apply(pd.to_numeric)

    df = df.sort_values('Date').reset_index(drop=True)

    # Indicators
    df['daily_return'] = df['Close'].pct_change()
    df['MA_20'] = df['Close'].rolling(20).mean()
    df['MA_50'] = df['Close'].rolling(50).mean()

    # Strategy logic
    df['signal'] = (df['MA_20'] > df['MA_50']).astype(int)
    df['strategy_return'] = df['daily_return'] * df['signal'].shift(1)
    df['strategy_cumulative'] = (1 + df['strategy_return']).cumprod()

    # Drawdown
    rolling_max = df['strategy_cumulative'].cummax()
    df['drawdown'] = (df['strategy_cumulative'] - rolling_max) / rolling_max

    return df

df = load_data()

# -------------------- METRICS --------------------
st.subheader("📊 Strategy Performance Overview")

sharpe = df['strategy_return'].mean() / df['strategy_return'].std()
max_dd = df['drawdown'].min()
total_return = df['strategy_cumulative'].iloc[-1] - 1

col1, col2, col3 = st.columns(3)
col1.metric("Sharpe Ratio", f"{sharpe:.2f}")
col2.metric("Max Drawdown", f"{max_dd:.2%}")
col3.metric("Total Return", f"{total_return:.2%}")

st.divider()

# -------------------- PRICE & MA CHART --------------------
st.subheader("📉 Price Action & Moving Averages")

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(df['Date'], df['Close'], label='Close Price', linewidth=1.6)
ax.plot(df['Date'], df['MA_20'], label='20-Day MA', linestyle='--')
ax.plot(df['Date'], df['MA_50'], label='50-Day MA', linestyle='--')

ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)

# -------------------- EQUITY CURVE --------------------
st.subheader("💰 Strategy Equity Curve")

fig2, ax2 = plt.subplots(figsize=(14, 4))
ax2.plot(df['Date'], df['strategy_cumulative'], linewidth=2)
ax2.set_xlabel("Date")
ax2.set_ylabel("Growth of ₹1 Invested")
ax2.grid(alpha=0.3)

st.pyplot(fig2)

# -------------------- DRAWDOWN --------------------
st.subheader("⚠️ Drawdown Analysis")

fig3, ax3 = plt.subplots(figsize=(14, 3))
ax3.fill_between(df['Date'], df['drawdown'], alpha=0.6)
ax3.set_xlabel("Date")
ax3.set_ylabel("Drawdown")
ax3.grid(alpha=0.3)

st.pyplot(fig3)

# -------------------- FOOTER --------------------
st.divider()
