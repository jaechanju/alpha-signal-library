import pandas as pd

def ma_slope(df: pd.DataFrame, window: int = 20):
    ma = df['close'].rolling(window).mean()
    slope = ma.pct_change()
    return slope


def ma_slope_signal(df: pd.DataFrame, window: int = 20, threshold: float = 0.001):
    ma = df['close'].rolling(window).mean()
    slope = ma.pct_change()

    signal = slope > threshold

    return signal.astype(int)
