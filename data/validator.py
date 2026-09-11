import pandas as pd

def validate_market_data(df: pd.DataFrame) -> bool:
    if df.empty:
        raise ValueError("ملف البيانات فارغ تماماً.")

    if df[['Open', 'High', 'Low', 'Close', 'Volume']].isnull().any().any():
        raise ValueError("خطأ: وُجدت قيم مفقودة (NaN).")

    if df.index.duplicated().any():
        raise ValueError("خطأ: وُجدت تواريخ مكررة.")

    if not df.index.is_monotonic_increasing:
        raise ValueError("خطأ: السجل التاريخي غير مرتب زمنياً.")

    if (df[['Open', 'High', 'Low', 'Close']] <= 0).any().any() or (df['Volume'] < 0).any():
        raise ValueError("خطأ: وُجدت أسعار سالبة أو صفرية غير منطقية.")
    
    if not ((df['High'] >= df['Open']) & (df['High'] >= df['Close'])).all():
        raise ValueError("خطأ منطقي: قيمة High أقل من Open أو Close.")

    if not ((df['Low'] <= df['Open']) & (df['Low'] <= df['Close'])).all():
        raise ValueError("خطأ منطقي: قيمة Low أعلى من Open أو Close.")

    return True
