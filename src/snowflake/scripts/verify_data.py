#!/usr/bin/env python3
"""
Snowflake Data Verification Script
This script verifies that data was successfully loaded into Snowflake.
"""

import snowflake.connector
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Snowflake Configuration
SNOWFLAKE_ACCOUNT = '[YOUR_ACCOUNT_ID]'
SNOWFLAKE_USER = '[YOUR_USERNAME]'
SNOWFLAKE_PASSWORD = '[YOUR_PASSWORD]'
SNOWFLAKE_DATABASE = "STOCKMARKETBATCH"
SNOWFLAKE_SCHEMA = "PUBLIC"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_TABLE = "DAILY_STOCK_METRICS"

def verify_snowflake_data():
    """Verify data loaded into Snowflake."""
    try:
        # Connect to Snowflake
        logger.info("Connecting to Snowflake...")
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        
        cursor = conn.cursor()
        logger.info("Connected to Snowflake successfully!")
        
        # Check total record count
        cursor.execute(f"SELECT COUNT(*) FROM {SNOWFLAKE_TABLE}")
        total_count = cursor.fetchone()[0]
        logger.info(f"Total records in {SNOWFLAKE_TABLE}: {total_count}")
        
        # Check unique symbols
        cursor.execute(f"SELECT COUNT(DISTINCT symbol) FROM {SNOWFLAKE_TABLE}")
        unique_symbols = cursor.fetchone()[0]
        logger.info(f"Unique stock symbols: {unique_symbols}")
        
        # Check date range
        cursor.execute(f"SELECT MIN(date), MAX(date) FROM {SNOWFLAKE_TABLE}")
        date_range = cursor.fetchone()
        logger.info(f"Date range: {date_range[0]} to {date_range[1]}")
        
        # Show sample data
        logger.info("Sample Data (Latest 5 records):")
        cursor.execute(f"""
        SELECT symbol, date, daily_open, daily_high, daily_low, daily_close, daily_volume, daily_change
        FROM {SNOWFLAKE_TABLE}
        ORDER BY date DESC, symbol
        LIMIT 5
        """)
        
        sample_data = cursor.fetchall()
        for row in sample_data:
            logger.info(f"   {row[0]:<6} | {row[1]} | Open: ${row[2]:<8.2f} | Close: ${row[5]:<8.2f} | Vol: {row[6]:<10} | Change: {row[7]:<6.2f}%")
        
        # Check data by symbol
        logger.info("Data Summary by Symbol:")
        cursor.execute(f"""
        SELECT symbol, COUNT(*) as record_count, 
               AVG(daily_change) as avg_change,
               AVG(daily_volume) as avg_volume
        FROM {SNOWFLAKE_TABLE}
        GROUP BY symbol
        ORDER BY symbol
        """)
        
        symbol_summary = cursor.fetchall()
        for row in symbol_summary:
            logger.info(f"   {row[0]:<6} | Records: {row[1]:<3} | Avg Change: {row[2]:<6.2f}% | Avg Volume: {row[3]:<12,.0f}")
        
        cursor.close()
        conn.close()
        logger.info("Snowflake connection closed")
        
        logger.info("DATA VERIFICATION COMPLETE!")
        logger.info("Your stock market data is successfully loaded in Snowflake!")
        
    except Exception as e:
        logger.error(f"Error verifying data: {e}")
        raise

if __name__ == "__main__":
    verify_snowflake_data() 