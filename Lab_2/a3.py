import pandas as pd
import statistics
import matplotlib.pyplot as plt

# ---------------- Functions ----------------

def load_irctc_data(filepath, sheet_name="IRCTC Stock Price"):
    """Load IRCTC stock price data from Excel."""
    return pd.read_excel(filepath, sheet_name=sheet_name)

def calculate_mean_variance(df):
    """Calculate mean and variance of Price (column D)."""
    prices = df.iloc[:, 3]  # column D
    mean_val = statistics.mean(prices)
    var_val = statistics.variance(prices)
    return mean_val, var_val

def filter_wednesdays(df):
    """Select price data for all Wednesdays."""
    df['Day'] = pd.to_datetime(df['Date']).dt.day_name()
    wed_prices = df[df['Day'] == 'Wednesday'].iloc[:, 3]
    return wed_prices

def filter_april(df):
    """Select price data for April."""
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    april_prices = df[df['Month'] == 4].iloc[:, 3]
    return april_prices

def probability_of_loss(df):
    """Find probability of making a loss from Chg% (column I)."""
    chg = df.iloc[:, 8]  # column I
    losses = chg.apply(lambda x: 1 if x < 0 else 0).sum()
    return losses / len(chg)

def probability_of_profit_on_wed(df):
    """Find probability of making a profit on Wednesdays."""
    df['Day'] = pd.to_datetime(df['Date']).dt.day_name()
    chg = df.iloc[:, 8]  # column I
    wed_chg = df[df['Day'] == 'Wednesday'].iloc[:, 8]
    profits = wed_chg[wed_chg > 0].count()
    return profits / len(wed_chg)

def conditional_probability_profit_given_wed(df):
    """P(Profit | Wednesday) = P(Profit n Wednesday) / P(Wednesday)."""
    df['Day'] = pd.to_datetime(df['Date']).dt.day_name()
    total = len(df)
    wed_df = df[df['Day'] == 'Wednesday']
    p_wed = len(wed_df) / total
    p_profit_and_wed = len(wed_df[wed_df.iloc[:, 8] > 0]) / total
    return p_profit_and_wed / p_wed

def scatter_plot_chg_vs_day(df):
    """Make scatter plot of Chg% vs Day of week."""
    df['Day'] = pd.to_datetime(df['Date']).dt.day_name()
    plt.figure(figsize=(8,5))
    plt.scatter(df['Day'], df.iloc[:, 8], alpha=0.7)
    plt.xlabel("Day of the Week")
    plt.ylabel("Chg%")
    plt.title("Scatter Plot of Chg% vs Day of Week")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

# ---------------- Main Program ----------------

if __name__ == "__main__":
    filepath = "Lab Session Data (1).xlsx"   # <---- put your file path here
    
    # Step 1: Load Data
    df = load_irctc_data(filepath)

    # Step 2: Mean & Variance
    mean_price, var_price = calculate_mean_variance(df)
    print(f"Population Mean Price: {mean_price:.2f}, Variance: {var_price:.2f}")

    # Step 3: Wednesday Mean vs Population Mean
    wed_prices = filter_wednesdays(df)
    wed_mean = statistics.mean(wed_prices)
    print(f"Wednesday Mean Price: {wed_mean:.2f}, Population Mean: {mean_price:.2f}")

    # Step 4: April Mean vs Population Mean
    april_prices = filter_april(df)
    april_mean = statistics.mean(april_prices)
    print(f"April Mean Price: {april_mean:.2f}, Population Mean: {mean_price:.2f}")

    # Step 5: Probability of Loss
    p_loss = probability_of_loss(df)
    print(f"Probability of Loss: {p_loss:.2f}")

    # Step 6: Probability of Profit on Wednesday
    p_profit_wed = probability_of_profit_on_wed(df)
    print(f"Probability of Profit on Wednesday: {p_profit_wed:.2f}")

    # Step 7: Conditional Probability P(Profit | Wednesday)
    p_profit_given_wed = conditional_probability_profit_given_wed(df)
    print(f"Conditional Probability of Profit given Wednesday: {p_profit_given_wed:.2f}")

    # Step 8: Scatter Plot
    scatter_plot_chg_vs_day(df)
