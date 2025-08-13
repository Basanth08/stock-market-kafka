# Stock Market Kafka Project

## Overview
I'm building a comprehensive real-time stock market data processing system using Apache Kafka for streaming data ingestion and processing. This project demonstrates how to handle high-throughput financial data streams efficiently with a complete data pipeline from source to analytics.

## 🎯 **My Execution Plan & Data Flow Architecture**

![Execution Plan](images/plan.jpg)

### **Complete Data Pipeline Flow:**

#### **1. Data Ingestion Layer**
- **Yahoo! Finance**: Batch ingestion for historical stock data
- **Alpha Vantage**: Stream ingestion for real-time market feeds
- **Apache Kafka**: Central message broker handling both batch and stream data
- **Apache ZooKeeper**: Managing Kafka cluster coordination

#### **2. Data Processing Layer**
- **Apache Spark**: Distributed processing engine with multiple worker nodes
- **Spark Streaming**: Real-time data processing from Kafka streams
- **Batch Processing**: Historical data transformation and analysis

#### **3. Orchestration & Management**
- **Apache Airflow**: Pipeline orchestration and scheduling
- **PostgreSQL**: Metadata database for Airflow workflows
- **Docker**: Complete containerization of the infrastructure

#### **4. Storage Strategy**
- **MinIO (S3-compatible)**: Flexible object storage with three data categories:
  - **Raw Data Dump CSV**: Unprocessed ingested data
  - **RealTime Data Parquet**: Processed streaming data
  - **Processed Data Parquet**: Transformed batch data

#### **5. Data Warehousing**
- **Snowflake**: Final destination for analytical querying and reporting
- **Data Loading**: Automated ingestion from MinIO storage

### **Execution Strategy:**
This architecture demonstrates a **production-ready, enterprise-grade data pipeline** that handles:
- **Real-time streaming** from Alpha Vantage
- **Batch processing** from Yahoo! Finance
- **Distributed computing** with Spark workers
- **Flexible storage** with MinIO
- **Professional orchestration** with Airflow
- **Scalable analytics** with Snowflake

## My Current Implementation
I've successfully implemented a sophisticated data pipeline that goes beyond the original plan. Here's what I've built so far:

### 🚀 Core Infrastructure (Docker Compose)
- **Apache Kafka & Zookeeper**: I'm running Kafka 7.6.0 with proper configuration for local development
- **Apache Airflow**: I've set up Airflow 2.8.1 for orchestrating my data workflows
- **PostgreSQL**: I'm using PostgreSQL 13 as the Airflow metadata database
- **MinIO**: I've implemented MinIO as my S3-compatible object storage solution
- **Apache Spark**: I'm running Spark 3.4.2 for distributed data processing with master, worker, and client nodes

### 📊 Data Pipeline Components

#### 1. Kafka Producers (`src/kafka/producer/`)
- **`stream_data_producer.py`**: I've built a real-time stock data simulator that generates live stock prices for major companies (AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA, INTC)
- **`batch_data_producer.py`**: I've implemented batch data ingestion for historical stock data

#### 2. Kafka Consumers (`src/kafka/consumer/`)
- **`realtime_data_consumer.py`**: I've created a real-time consumer that processes streaming data and stores it in MinIO
- **`batch_data_consumer.py`**: I've built a batch consumer for processing historical data

#### 3. Data Processing (`src/spark/jobs/`)
- **`spark_batch_processor.py`**: I've implemented Spark batch processing for large-scale data transformation
- **`spark_stream_processor.py`**: I've created Spark streaming jobs for real-time data processing

#### 4. Data Orchestration (`src/airflow/dags/`)
- **`stock_market_batch_dag.py`**: I've designed an Airflow DAG that orchestrates the entire batch pipeline from data ingestion to Snowflake loading
- **`check_minio_file.py`**: I've implemented data validation to check if data exists in MinIO for given execution dates

#### 5. Data Warehouse (`src/snowflake/scripts/`)
- **`load_to_snowflake.py`**: I've implemented data loading into Snowflake for analytics and reporting

### 🔧 Technology Stack
- **Streaming**: Apache Kafka 7.6.0, Confluent Kafka Python client
- **Orchestration**: Apache Airflow 2.8.1
- **Processing**: Apache Spark 3.4.2 with AWS SDK integration
- **Storage**: MinIO (S3-compatible), PostgreSQL
- **Data Warehouse**: Snowflake
- **Languages**: Python, SQL
- **Data Formats**: JSON, CSV, Parquet

### ⚙️ Configuration & Environment
- **`.env`**: I've configured environment variables for Kafka topics, MinIO settings, and API keys
- **Kafka Topics**: 
  - `stock-market-realtime` for streaming data
  - `stock_market_batch` for batch processing
- **MinIO**: Configured with `stock-market-data` bucket and proper access credentials

### 📁 Project Structure
```
stock-market-kafka/
├── src/
│   ├── kafka/
│   │   ├── producer/
│   │   │   ├── stream_data_producer.py      # Real-time stock data simulator
│   │   │   └── batch_data_producer.py      # Batch data ingestion
│   │   └── consumer/
│   │       ├── realtime_data_consumer.py   # Real-time data processing
│   │       └── batch_data_consumer.py      # Batch data processing
│   ├── spark/
│   │   └── jobs/
│   │       ├── spark_batch_processor.py    # Spark batch processing
│   │       └── spark_stream_processor.py   # Spark streaming
│   ├── airflow/
│   │   ├── dags/
│   │   │   └── stock_market_batch_dag.py   # Data pipeline orchestration
│   │   └── scripts/
│   │       ├── batch_data_producer.py      # Airflow-integrated producer
│   │       ├── batch_data_consumer.py      # Airflow-integrated consumer
│   │       ├── check_minio_file.py         # Data validation script
│   │       └── load_to_snowflake.py       # Data warehouse loading
│   └── snowflake/
│       └── scripts/
│           └── load_to_snowflake.py        # Data warehouse loading
├── docker-compose.yaml                     # Complete infrastructure setup
├── requirements.txt                        # Python dependencies
├── commands.sh                            # Useful commands and setup
├── .env                                   # Environment configuration
└── README.md                              # This documentation
```

## What I've Accomplished
✅ **Real-time Data Generation**: I've created a sophisticated stock market simulator that generates realistic price movements  
✅ **Streaming Pipeline**: I've implemented end-to-end Kafka streaming from producer to consumer  
✅ **Data Storage**: I've set up MinIO for S3-compatible object storage  
✅ **Batch Processing**: I've built Spark jobs for large-scale data transformation  
✅ **Workflow Orchestration**: I've created Airflow DAGs to coordinate the entire pipeline  
✅ **Data Warehouse Integration**: I've implemented Snowflake loading for analytics  
✅ **Containerized Infrastructure**: I've containerized everything with Docker Compose  
✅ **Data Validation**: I've implemented MinIO data checks for pipeline reliability  
✅ **Environment Configuration**: I've set up proper environment variables for all services  
✅ **Batch Data Pipeline Success**: I've successfully executed the complete batch data ingestion pipeline, fetching 1 year of historical data for 10 major stocks (AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA, INTC, JPM, V) and producing 2,500 records to Kafka with 100% success rate  

## 🎯 My Next Challenges (From challenge.txt)
Based on my current implementation, I'm planning to tackle these next steps:

1. **Integrate MinioCheck in Airflow**: I'll remove the standalone Producer and Consumer tasks and integrate the MinIO validation directly into my Airflow pipeline
2. **Build Hourly Airflow Pipeline**: I'll create a pipeline that runs every hour to process yesterday's data and update stream data
3. **Real-time Data Loading**: I'll implement hourly updates to load streaming data into Snowflake
4. **Stock Visualization**: I'll create dashboards and visualizations for different stocks to monitor performance

## Current Status
🚀 **Major Milestone Achieved** - I've successfully built a production-ready data pipeline that exceeds my original plan!

### 🎉 **Latest Achievement: Batch Data Pipeline Successfully Executed!**

On **August 12, 2025**, I achieved a major breakthrough in my data pipeline:

#### **What I Accomplished:**
- **Successfully executed** the complete batch data ingestion pipeline
- **Fetched historical data** for 10 major stocks using Yahoo! Finance API
- **Produced 2,500 records** to Kafka with **100% success rate**
- **Zero failures** in data fetching or message production

#### **Technical Details:**
- **Stocks Processed**: AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA, INTC, JPM, V
- **Data Volume**: 250 historical records per stock (1 year of daily data)
- **Kafka Topic**: `stock_market_batch`
- **Data Format**: JSON with OHLC (Open, High, Low, Close) + Volume data
- **Processing Time**: ~30 seconds for complete pipeline execution

#### **Pipeline Components Working:**
✅ **Data Source**: Yahoo! Finance API integration  
✅ **Data Fetching**: Historical stock data retrieval (1 year)  
✅ **Data Transformation**: OHLC data cleaning and formatting  
✅ **Kafka Producer**: Message production with proper serialization  
✅ **Error Handling**: Robust error handling with detailed logging  
✅ **Environment**: Virtual environment with all dependencies resolved  

#### **What This Means:**
My **batch data pipeline is now fully operational** and ready for:
- **Production deployment**
- **Integration with Spark processing**
- **Airflow orchestration**
- **Data warehouse loading**
- **Real-time analytics**

This represents a **critical milestone** in building a complete, enterprise-grade stock market data platform!

## Getting Started
1. **Clone and Setup**: I've provided a complete `docker-compose.yaml` for easy setup
2. **Environment**: All dependencies are in `requirements.txt` and environment variables in `.env`
3. **Commands**: I've documented useful commands in `commands.sh`
4. **Run**: Use `docker-compose up` to start the entire infrastructure

## 🐍 Python Virtual Environment Setup

### **What is a Virtual Environment (venv)?**

A **virtual environment** is a **separate, isolated container** for Python packages and dependencies. Think of it as a "clean room" where you can install specific versions of libraries without affecting your system's global Python installation.

### **Why Virtual Environments Are Essential:**

#### **🔒 Isolation & Dependency Management**
- **Without venv**: All Python packages go to your system Python (can cause conflicts)
- **With venv**: Packages are isolated to just this project
- **Your project needs specific versions**:
  - `confluent-kafka==2.3.0` for Kafka integration
  - `yfinance` for stock market data
  - `minio` for S3-compatible storage
  - `fastparquet` and `pyarrow` for data processing

#### **📦 Reproducibility & Consistency**
- Anyone can recreate **exactly the same environment**
- **No "it works on my machine" problems**
- **Consistent development environment** across team members
- **Professional practice** - Industry standard for Python projects

### **How to Set Up Your Virtual Environment:**

#### **1. Create the Virtual Environment**
```bash
# Using your specific Python version
python3.11.5 -m venv venv

# Or simply (if python points to 3.11.5)
python -m venv venv
```

#### **2. Activate the Virtual Environment**
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

#### **3. Install Dependencies**
```bash
# Install all required packages
pip install -r requirements.txt
```

#### **4. Verify Installation**
```bash
# Check what's installed
pip list

# Verify Python path points to venv
which python
# Should show: /path/to/stock-market-kafka/venv/bin/python
```

### **How It Works:**

When activated, your terminal prompt changes to show `(venv)`:
```bash
(venv) (base) varagantibasanthkumar@VARAGANTIs-MacBook-Pro stock-market-kafka %
```

**What Happens:**
- **Python path** points to `venv/bin/python`
- **pip install** goes to `venv/lib/python3.11/site-packages/`
- **Your system Python** remains completely untouched

### **Managing Your Virtual Environment:**

#### **Activate (when starting work):**
```bash
source venv/bin/activate
```

#### **Deactivate (when done):**
```bash
deactivate
```

#### **Update Dependencies:**
```bash
# After modifying requirements.txt
pip install -r requirements.txt --upgrade
```

#### **Clean Reinstall:**
```bash
# If you encounter dependency issues
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **Benefits for Your Stock Market Data Pipeline:**

1. **Clean Kafka Setup** - No conflicts with other Python projects
2. **Specific Library Versions** - Ensures compatibility across environments
3. **Easy Sharing** - Others can recreate your exact environment
4. **Professional Development** - Industry best practice for Python projects
5. **Dependency Isolation** - Your project won't interfere with system Python

### **Troubleshooting Virtual Environment Issues:**

#### **Common Problems:**
- **"Command not found: python3.10"** → Use `python3.11.5` or `python`
- **Packages not found** → Ensure venv is activated (`source venv/bin/activate`)
- **Permission errors** → Check if you have write access to the directory

#### **Verification Commands:**
```bash
# Check if venv is active
echo $VIRTUAL_ENV

# Check Python location
which python

# Check installed packages
pip list
```

---

*Virtual environments are crucial for maintaining clean, reproducible Python development environments. This setup ensures your stock market data pipeline will work consistently across different machines and team members.*

## 🔧 Troubleshooting Common Issues

### Port Conflicts When Starting Docker Infrastructure

When starting the Docker infrastructure, you may encounter port conflicts. Here's how I resolved them:

#### **Port 8080 Conflict (Spark Master)**
**Problem**: Port 8080 was occupied by conflicting services
```bash
Error: Bind for 0.0.0.0:8080 failed: port is already allocated
```

**Root Causes Found**:
1. **Java WAR Application**: A standalone Java web application was running on port 8080
2. **Kafka UI Container**: A `kafka-ui` container was using port 8080

**Solutions**:
```bash
# Check what's using port 8080
lsof -i :8080

# Stop conflicting Java application
kill <PID>

# Stop conflicting Docker containers
docker stop kafka-ui

# Verify port is free
lsof -i :8080
```

#### **Port 8081 Conflict (Airflow Webserver)**
**Problem**: Port 8081 was occupied by another service
```bash
Error: Bind for 0.0.0.0:8081 failed: port is already allocated
```

**Root Cause**: **Confluent Schema Registry** container was running on port 8081

**Solution**:
```bash
# Check what's using port 8081
lsof -i :8081
docker ps -a | grep 8081

# Stop conflicting container
docker stop schema-registry

# Verify port is free
lsof -i :8081
```

#### **General Port Conflict Resolution Steps**
1. **Identify conflicting processes**:
   ```bash
   lsof -i :<PORT_NUMBER>
   docker ps -a | grep <PORT_NUMBER>
   ```

2. **Stop conflicting services**:
   ```bash
   # For system processes
   kill <PID>
   
   # For Docker containers
   docker stop <CONTAINER_NAME>
   ```

3. **Clean up Docker state**:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

4. **Verify all services are running**:
   ```bash
   docker-compose ps
   ```

### **Common Docker Issues**

#### **Container Name Conflicts**
**Problem**: Container names already in use
```bash
Error: Conflict. The container name "/zookeeper" is already in use
```

**Solution**: Remove conflicting containers
```bash
docker rm -f zookeeper
docker rm -f kafka
```

#### **Network Binding Issues**
**Problem**: Docker networking conflicts during startup
```bash
Error: failed to set up container networking: driver failed programming external connectivity
```

**Solution**: Ensure ports are free and restart cleanly
```bash
docker-compose down
# Free up ports (see above)
docker-compose up -d
```

### **Verification Commands**

After resolving conflicts, verify your infrastructure is healthy:

```bash
# Check all container statuses
docker-compose ps

# Check specific service logs
docker-compose logs kafka
docker-compose logs spark-master
docker-compose logs airflow-webserver

# Verify ports are accessible
curl http://localhost:8080  # Spark Master UI
curl http://localhost:8081  # Airflow UI
curl http://localhost:9001  # MinIO Console
```

### **Prevention Tips**

1. **Check ports before starting**: Always verify no conflicting services are running
2. **Use unique port mappings**: Consider changing default ports in `docker-compose.yaml` if conflicts persist
3. **Clean shutdown**: Always use `docker-compose down` before stopping services
4. **Monitor running containers**: Regularly check `docker ps` to see what's currently active

### **MinIO Bucket Creation Issues**

#### **Problem**: MinIO bucket not being created automatically
**Symptoms**: 
- MinIO MC service shows errors about unrecognized commands
- Bucket `stock-market-data` doesn't exist after startup
- Errors like `mc: <ERROR> 'config' is not a recognized command`

**Root Cause**: 
The MinIO MC (MinIO Client) version has changed its command syntax:
- Old: `mc config host add` → New: `mc alias set`
- Old: `mc policy set public` → New: `mc anonymous set public`

**Manual Solution**:
```bash
# Access MinIO container and set up manually
docker exec minio mc alias set myminio http://localhost:9000 minioadmin minioadmin
docker exec minio mc mb myminio/stock-market-data
docker exec minio mc anonymous set public myminio/stock-market-data

# Verify bucket creation
docker exec minio mc ls myminio
```

**Prevention**: 
The `docker-compose.yaml` has been updated with the correct MinIO MC commands for future deployments.

---

*This README documents my journey building a comprehensive stock market data pipeline. I've evolved from a simple Kafka setup to a full-featured data engineering platform with real-time streaming, batch processing, orchestration, and analytics capabilities.*