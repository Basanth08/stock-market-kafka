#!/usr/bin/env python3
"""
Snowflake Configuration Example
Copy this file to config.py and fill in your actual credentials
Never commit config.py files to version control
"""

# Snowflake Configuration Example
SNOWFLAKE_ACCOUNT = 'YOUR_ACCOUNT_ID'  # e.g., 'XASHRVU-AC03776'
SNOWFLAKE_USER = 'YOUR_USERNAME'        # e.g., 'BBBBBBBOSSS'
SNOWFLAKE_PASSWORD = 'YOUR_PASSWORD'    # Your actual password
SNOWFLAKE_DATABASE = "STOCKMARKETBATCH"
SNOWFLAKE_SCHEMA = "PUBLIC"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_TABLE = "DAILY_STOCK_METRICS"

# MinIO Configuration (if needed)
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
MINIO_ENDPOINT = "http://localhost:9000"
MINIO_BUCKET = "stock-market-data"

# Usage Instructions:
# 1. Copy this file to config.py
# 2. Fill in your actual Snowflake credentials
# 3. Import config.py in your scripts
# 4. Never commit config.py to version control
# 5. Consider using environment variables for production 