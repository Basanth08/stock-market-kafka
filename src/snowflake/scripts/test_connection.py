#!/usr/bin/env python3
"""
Snowflake Connection Test Script
This script tests different Snowflake account identifier formats to find the correct one.
"""

import snowflake.connector
import sys

# Your credentials
USER = '[YOUR_USERNAME]'
PASSWORD = '[YOUR_PASSWORD]'
WAREHOUSE = 'COMPUTE_WH'
DATABASE = 'STOCKMARKETBATCH'
SCHEMA = 'PUBLIC'

# Different account identifier formats to try
ACCOUNT_FORMATS = [
    '[YOUR_ACCOUNT_ID]',                   # Correct format from your account
    '[YOUR_ACCOUNT_ID].snowflakecomputing.com',  # Full URL format
    '[YOUR_ACCOUNT_ID].us-east-1',         # AWS US East
    '[YOUR_ACCOUNT_ID].us-west-2',         # AWS US West
    '[YOUR_ACCOUNT_ID]',                   # Simple format (fallback)
]

def test_connection(account):
    """Test connection with a specific account format."""
    try:
        print(f"Testing account format: {account}")
        
        conn = snowflake.connector.connect(
            user=USER,
            password=PASSWORD,
            account=account,
            warehouse=WAREHOUSE,
            database=DATABASE,
            schema=SCHEMA
        )
        
        print(f"SUCCESS! Connected to Snowflake!")
        print(f"   Account: {conn.account}")
        print(f"   Database: {conn.database}")
        print(f"   Schema: {conn.schema}")
        print(f"   Warehouse: {conn.warehouse}")
        
        # Test a simple query
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION()")
        version = cursor.fetchone()[0]
        print(f"   Snowflake Version: {version}")
        
        cursor.close()
        conn.close()
        print("   Connection closed successfully!")
        
        return True
        
    except Exception as e:
        print(f"   Connection failed: {e}")
        return False

def main():
    print("Snowflake Connection Test - Finding the Right Account Format")
    print("=" * 70)
    
    success_count = 0
    
    for account_format in ACCOUNT_FORMATS:
        if test_connection(account_format):
            success_count += 1
            print(f"SUCCESS! Use this account format: {account_format}")
            break
    
    if success_count == 0:
        print("All connection attempts failed.")
        print("Please check:")
        print("1. Your Snowflake account identifier")
        print("2. Your username and password")
        print("3. Network connectivity and firewall settings")
        print("4. Snowflake account status and permissions")
    
    print(f"Test Results: {success_count}/{len(ACCOUNT_FORMATS)} successful connections")

if __name__ == "__main__":
    main() 