Import pandas as pd
import numpy as np

def generate_dummy_data() -> pd.DataFrame:
    dates = pd.date_range(start='2025-01-01', periods=100, freq='B')
    np.random.seed(42)
    
    close = 100 + np.cumsum(np.random.randn(100) * 0.5)
    high = close + np.random.rand(100) * 1.0
    low = close - np.random.rand(100) * 1.0
    open_p = low + (high - low) * np.random.rand(100)
    volume = np.random.randint(10000, 100000, size=100)

    df = pd.DataFrame({
        'Open': open_p,
        'High': high,
        'Low': low,
        'Close': close,
        'Volume': volume
    }, index=dates)
    
    df.index.name = 'Date'
    return df
