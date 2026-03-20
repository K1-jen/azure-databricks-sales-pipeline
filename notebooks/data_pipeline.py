# Load data
df = spark.read.csv('/Volumes/kierra_databricks/default/data-volume/sales.csv', header=True, inferSchema=True)

# Transform
df_summary = df.groupBy("region").sum("revenue")

# Save processed data
df_summary.write.mode("overwrite").csv('/Volumes/kierra_databricks/default/data-volume/processed_sales')

# Save as table
df_summary.write.mode("overwrite").saveAsTable("sales_summary")

# Display results
display(df_summary)
