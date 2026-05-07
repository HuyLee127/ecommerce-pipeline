import pandas as pd

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Làm sạch dữ liệu đơn hàng Shopee/Tiki.
    
    Bước:
    1. Bỏ row có order_id null
    2. Bỏ row trùng lặp
    3. Convert order_date sang datetime
    4. Bỏ đơn có amount <= 0 (đơn lỗi)
    """
    # Bước 1: Bỏ null ở cột bắt buộc
    df = df.dropna(subset=['order_id'])
    
    # Bước 2: Bỏ duplicate
    df = df.drop_duplicates(subset=['order_id'], keep='first')
    
    # Bước 3: Convert datetime (errors='coerce' → giá trị lỗi thành NaT)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    
    # Bước 4: Lọc đơn hợp lệ
    df = df[df['amount'] > 0]
    
    # Reset index sau khi lọc (huynh đã hiểu sâu chỗ này ở quiz pandas!)
    df = df.reset_index(drop=True)
    
    return df


if __name__ == "__main__":
    # Test nhanh
    sample = pd.DataFrame({
        'order_id': ['SP001', 'SP002', None, 'SP001', 'SP003'],
        'order_date': ['2026-01-15', '2026-01-16', '2026-01-17', '2026-01-15', 'invalid'],
        'amount': [150000, 250000, 100000, 150000, -50000]
    })
    
    result = clean_orders(sample)
    print(result)