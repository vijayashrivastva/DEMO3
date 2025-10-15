import pandas as pd
import matplotlib.pyplot as plt
import boto3
import os

BUCKET = os.getenv("REPORT_BUCKET", "my-analytics-bucket-demo")

def generate_report():
    df = pd.read_csv("region_sales_report.csv")
    plt.figure(figsize=(8, 4))
    df.plot(kind="bar", x="region", y="total_revenue", legend=False)
    plt.title("Revenue by Region")
    plt.tight_layout()
    plt.savefig("region_revenue_report.png")

    s3 = boto3.client("s3")
    s3.upload_file("region_sales_report.csv", BUCKET, "reports/region_sales_report.csv")
    s3.upload_file("region_revenue_report.png", BUCKET, "reports/region_revenue_report.png")
    print(f"Reports uploaded to s3://{BUCKET}/reports/")

if __name__ == "__main__":
    generate_report()