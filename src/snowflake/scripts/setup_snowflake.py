#!/usr/bin/env python3
"""
Snowflake Setup Script
This script creates the necessary Snowflake infrastructure for the stock market data pipeline.
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

def create_snowflake_infrastructure():
    """Create Snowflake database, warehouse, and schema."""
    try:
        # Connect to Snowflake
        logger.info("Connecting to Snowflake...")
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT
        )
        
        cursor = conn.cursor()
        logger.info("Connected to Snowflake successfully!")
        
        # Create warehouse if it doesn't exist
        logger.info(f"Creating warehouse: {SNOWFLAKE_WAREHOUSE}")
        cursor.execute(f"""
        CREATE WAREHOUSE IF NOT EXISTS {SNOWFLAKE_WAREHOUSE}
        WAREHOUSE_SIZE = 'X-SMALL'
        AUTO_SUSPEND = 300
        AUTO_RESUME = TRUE
        """)
        logger.info(f"Warehouse '{SNOWFLAKE_WAREHOUSE}' created/verified")
        
        # Use the warehouse
        cursor.execute(f"USE WAREHOUSE {SNOWFLAKE_WAREHOUSE}")
        logger.info(f"Using warehouse: {SNOWFLAKE_WAREHOUSE}")
        
        # Create database if it doesn't exist
        logger.info(f"Creating database: {SNOWFLAKE_DATABASE}")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {SNOWFLAKE_DATABASE}")
        logger.info(f"Database '{SNOWFLAKE_DATABASE}' created/verified")
        
        # Use the database
        cursor.execute(f"USE DATABASE {SNOWFLAKE_DATABASE}")
        logger.info(f"Using database: {SNOWFLAKE_DATABASE}")
        
        # Create schema if it doesn't exist
        logger.info(f"Creating schema: {SNOWFLAKE_SCHEMA}")
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {SNOWFLAKE_SCHEMA}")
        logger.info(f"Schema '{SNOWFLAKE_SCHEMA}' created/verified")
        
        # Use the schema
        cursor.execute(f"USE SCHEMA {SNOWFLAKE_SCHEMA}")
        logger.info(f"Using schema: {SNOWFLAKE_SCHEMA}")
        
        # Create the stock metrics table
        logger.info("Creating DAILY_STOCK_METRICS table...")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS DAILY_STOCK_METRICS (
            symbol VARCHAR(10) NOT NULL,
            date DATE NOT NULL,
            daily_open DECIMAL(10,2),
            daily_high DECIMAL(10,2),
            daily_low DECIMAL(10,2),
            daily_close DECIMAL(10,2),
            daily_volume BIGINT,
            daily_change DECIMAL(5,2),
            late_updated TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
            PRIMARY KEY (symbol, date)
        )
        """)
        logger.info("DAILY_STOCK_METRICS table created/verified")
        
        # Verify the setup
        logger.info("Verifying Snowflake infrastructure...")
        
        # Check warehouse
        cursor.execute(f"SHOW WAREHOUSES LIKE '{SNOWFLAKE_WAREHOUSE}'")
        warehouses = cursor.fetchall()
        logger.info(f"   Warehouse: {warehouses[0][0]} - Status: {warehouses[0][7]}")
        
        # Check database
        cursor.execute(f"SHOW DATABASES LIKE '{SNOWFLAKE_DATABASE}'")
        databases = cursor.fetchall()
        logger.info(f"   Database: {databases[0][1]} - Owner: {databases[0][2]}")
        
        # Check schema
        cursor.execute(f"SHOW SCHEMAS IN DATABASE {SNOWFLAKE_DATABASE}")
        schemas = cursor.fetchall()
        logger.info(f"   Schema: {schemas[0][1]} - Owner: {schemas[0][2]}")
        
        # Check table
        cursor.execute("SHOW TABLES IN SCHEMA PUBLIC")
        tables = cursor.fetchall()
        logger.info(f"   Tables: {len(tables)} found")
        for table in tables:
            logger.info(f"     - {table[1]} ({table[2]})")
        
        cursor.close()
        conn.close()
        logger.info("Snowflake connection closed")
        
        logger.info("SNOWFLAKE INFRASTRUCTURE SETUP COMPLETE!")
        logger.info("Your data warehouse is ready for the stock market pipeline!")
        
    except Exception as e:
        logger.error(f"Error setting up Snowflake: {e}")
        raise

if __name__ == "__main__":
    create_snowflake_infrastructure() 