from data.loader import generate_dummy_data
from data.validator import validate_market_data

def main():
    print("🚀 بدء تشغيل نظام التداول (V1)...")
    
    print("📊 جاري تحميل البيانات...")
    df = generate_dummy_data()
    
    print("🔍 جاري فحص وتنظيف البيانات...")
    try:
        is_valid = validate_market_data(df)
        if is_valid:
            print("✅ البيانات سليمة وجاهزة للاختبار.")
            print("📈 نظرة على حركة السعر (أول 5 أيام):")
            print(df[['Open', 'High', 'Low', 'Close']].head())
    except Exception as e:
        print(f"❌ تم رفض البيانات: {e}")

if __name__ == "__main__":
    main()
