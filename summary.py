import sqlite3

def summarize_market_data(db_name="crypto_trading.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    print("\n--- Market Database Summary ---")

    cursor.execute('SELECT * FROM price_history ORDER BY id DESC LIMIT 5')
    recent_rows = cursor.fetchall()
    print("Recent Ticks:")
    for row in recent_rows:
        print(f"ID: {row[0]} | Time: {row[1]} | Price: ${row[3]:,.2f}")

    cursor.execute('SELECT AVG(price) FROM price_history')
    avg_price = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM price_history')
    total_records = cursor.fetchone()[0]

    print(f"\nTotal Records Stored: {total_records}")
    print(f"Average BTC Price in DB: ${avg_price:,.2f}")

    conn.close()

if __name__ == "__main__":
    summarize_market_data()