import pandas as pd

# Load raw data
df = pd.read_csv("stock_data.csv")

# Drop the first two rows (ticker and empty row)
df = df.iloc[2:].reset_index(drop=True)

# Rename columns properly
df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Convert price columns to numeric
price_cols = ['Close', 'High', 'Low', 'Open', 'Volume']
df[price_cols] = df[price_cols].apply(pd.to_numeric)

# Sort by date
df = df.sort_values('Date').reset_index(drop=True)

# Final checks
print(df.head())
print("\nINFO:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

# Daily returns
df['daily_return'] = df['Close'].pct_change()
print(df[['Date', 'Close', 'daily_return']].head())

# Cumulative returns
df['cumulative_return'] = (1 + df['daily_return']).cumprod()
print(df[['Date', 'cumulative_return']].tail())

# Moving averages
df['MA_20'] = df['Close'].rolling(window=20).mean()
df['MA_50'] = df['Close'].rolling(window=50).mean()

# Average volume
df['Volume_MA_20'] = df['Volume'].rolling(window=20).mean()
print("\nFINAL DATA PREVIEW:")
print(df.head(25))


# Trading signal: 1 = Buy, 0 = No position
df['signal'] = 0

df.loc[df['MA_20'] > df['MA_50'], 'signal'] = 1
# Position: identifies buy/sell points
df['position'] = df['signal'].diff()

print("\nSIGNAL CHECK:")
print(df[['Date', 'Close', 'MA_20', 'MA_50', 'signal', 'position']].tail(20))

# Strategy returns (shift signal to avoid look-ahead bias)
df['strategy_return'] = df['daily_return'] * df['signal'].shift(1)

# Strategy cumulative returns
df['strategy_cumulative'] = (1 + df['strategy_return']).cumprod()

# Drawdown calculation
rolling_max = df['strategy_cumulative'].cummax()
df['drawdown'] = (df['strategy_cumulative'] - rolling_max) / rolling_max

# Sharpe Ratio (assuming risk-free rate = 0)
sharpe_ratio = df['strategy_return'].mean() / df['strategy_return'].std()

print("\nSharpe Ratio:", sharpe_ratio)

print("\nPERFORMANCE CHECK:")
print(df[['Date', 'daily_return', 'strategy_return', 'strategy_cumulative', 'drawdown']].tail(15))

