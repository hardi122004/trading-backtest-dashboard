import yfinance as yf

df = yf.download("RELIANCE.NS", period="2y")
df.to_csv("reliance_2y.csv")

print(df.head())
