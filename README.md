# 🚀 Azure Databricks Sales Data Pipeline

## 📌 Overview
This project demonstrates an end-to-end data pipeline built using Azure Databricks and PySpark to process and analyze sales data.

The pipeline ingests raw data, transforms it into meaningful insights, and stores the results for downstream analytics and visualization.

---

## ⚙️ Architecture

CSV (Unity Catalog Volume)
↓
Azure Databricks (Apache Spark)
↓
Data Transformation (PySpark)
↓
Aggregated Output (Revenue by Region)
↓
Stored Data (Volume + Table)
↓
Visualization (Databricks / Power BI)


---

## 🔄 Pipeline Workflow

### 1. Data Ingestion
- Loaded CSV data from Unity Catalog Volume  
- Used Spark DataFrame API for scalable processing  

### 2. Data Transformation
- Grouped data by region  
- Aggregated total revenue  

### 3. Data Storage
- Saved processed data back to Volume  
- Stored results as a queryable table (`sales_summary`)  

### 4. Data Validation
- Reloaded saved data  
- Verified row counts and outputs  

### 5. Visualization
- Created bar chart showing revenue by region  

---

## 📊 Results

| Region | Total Revenue |
|--------|-------------|
| East   | 2500        |
| West   | 2000        |
| South  | 1200        |

---

## 📸 Project Screenshots

### 📊 Dashboard
![Dashboard](images/Dashboard.png)

### 📈 Processed Output
![Output](images/Chart1.png)

### 💻 Pipeline Code
![Code](images/Datapipline_databricks.png)

---

## 🧰 Technologies Used
- Azure Databricks  
- Apache Spark (PySpark)  
- Unity Catalog (Volumes)  
- Power BI (for visualization)

---

## 💡 Key Learnings
- Built a scalable data pipeline using distributed processing  
- Implemented data validation for pipeline reliability  
- Transformed raw data into business insights  
- Structured data for downstream analytics and BI tools  

---

## 💼 Resume Highlight
Built an end-to-end data pipeline in Azure Databricks using PySpark to ingest, transform, and aggregate sales data, producing regional revenue insights and persisting results in Unity Catalog.

---

## 🚀 Future Improvements
- Integrate with Azure AI Search for intelligent querying  
- Build a Power BI dashboard for real-time reporting  
- Expand pipeline to handle larger datasets  

---
