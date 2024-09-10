from matplotlib import pyplot as plt
import pandas as pd

from financier import PROJECT_ROOT

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Date", "Balance"]
df = pd.read_csv(
    PROJECT_ROOT / "data/account_data.csv", usecols=columns, parse_dates=["Date"]
)

df["Balance"] = df["Balance"].replace({"£": "", r"\+": ""}, regex=True).astype(float)

plt.plot(df.Date, df.Balance)
plt.savefig(PROJECT_ROOT / "output/balance_plot.png")
