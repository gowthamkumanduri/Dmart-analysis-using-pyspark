from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, expr

def create_spark_session():
    return SparkSession.builder.appName("Dmart Sales Analysis Pipeline").getOrCreate()

def load_data(spark):
    # Load the datasets with appropriate column names
    products_df = spark.read.csv("Product.csv", header=True, inferSchema=True)
    sales_df = spark.read.csv("Sales.csv", header=True, inferSchema=True)
    customers_df = spark.read.csv("Customer.csv", header=True, inferSchema=True)
    return products_df, sales_df, customers_df

def clean_and_transform(products_df, sales_df, customers_df):
    # Rename columns for consistency
    products_df = products_df.withColumnRenamed("Product ID", "ProductID")
    sales_df = sales_df.withColumnRenamed("Customer ID", "CustomerID").withColumnRenamed("Product ID","ProductID")
    customers_df = customers_df.withColumnRenamed("Customer ID", "CustomerID")

    # Drop missing values
    products_df = products_df.dropna()
    sales_df = sales_df.dropna()
    customers_df = customers_df.dropna()

    # Join DataFrames
    sales_product_df = sales_df.join(products_df, on="ProductID", how="inner")
    full_df = sales_product_df.join(customers_df, on="CustomerID", how="inner")
    
    # Add Profit Margin column
    full_df = full_df.withColumn("Profit_Margin", expr("Profit / Sales"))
    
    return full_df

def run_analysis(full_df):
    # Analytical Queries
    print("1. Total sales by category:")
    full_df.groupBy("Category").agg(sum("Sales").alias("Total_Sales")).show()

    print("2. Customer with highest number of purchases:")
    full_df.groupBy("CustomerID").agg(count("Sales").alias("Purchase_Count")).orderBy("Purchase_Count", ascending=False).show(1)

    print("3. Average discount across all products:")
    full_df.agg(avg("Discount").alias("Avg_Discount")).show()

    print("4. Unique products sold in each region:")
    full_df.select("Region", "ProductID").distinct().groupBy("Region").count().withColumnRenamed("count", "Unique_Products").show()

    print("5. Total profit by state:")
    full_df.groupBy("State").agg(sum("Profit").alias("Total_Profit")).show()

    print("6. Top product sub-category by sales:")
    full_df.groupBy("Sub-Category").agg(sum("Sales").alias("Total_Sales")).orderBy("Total_Sales", ascending=False).show(1)

    print("7. Average age of customers in each segment:")
    full_df.groupBy("Segment").agg(avg("Age").alias("Avg_Age")).show()

    print("8. Orders shipped by shipping mode:")
    full_df.groupBy("Ship Mode").agg(count("*").alias("Order_Count")).show()

    print("9. Total quantity sold per city:")
    full_df.groupBy("City").agg(sum("Quantity").alias("Total_Quantity")).show()

    print("10. Customer segment with highest profit margin:")
    full_df.groupBy("Segment").agg(avg("Profit_Margin").alias("Avg_Profit_Margin")).orderBy("Avg_Profit_Margin", ascending=False).show(1)

def main():
    spark = create_spark_session()
    products_df, sales_df, customers_df = load_data(spark)
    full_df = clean_and_transform(products_df, sales_df, customers_df)
    run_analysis(full_df)
    spark.stop()

if __name__ == "__main__":
    main()
