import boto3
import pandas as pd
import time
import os

ATHENA_DB = os.getenv("ATHENA_DB", "analytics_db")
ATHENA_OUTPUT = os.getenv("ATHENA_OUTPUT", "s3://my-analytics-bucket-demo/query-results/")
QUERY = os.getenv("ATHENA_QUERY", """
SELECT region, SUM(revenue) AS total_revenue, SUM(quantity) AS total_units
FROM sales_data
GROUP BY region
ORDER BY total_revenue DESC;
""")

client = boto3.client("athena", region_name=os.getenv("AWS_REGION", "ap-south-1"))

def run_athena_query():
    response = client.start_query_execution(
        QueryString=QUERY,
        QueryExecutionContext={"Database": ATHENA_DB},
        ResultConfiguration={"OutputLocation": ATHENA_OUTPUT},
    )

    query_id = response["QueryExecutionId"]

    while True:
        status = client.get_query_execution(QueryExecutionId=query_id)
        state = status["QueryExecution"]["Status"]["State"]
        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break
        time.sleep(2)

    if state == "SUCCEEDED":
        result_path = f"{ATHENA_OUTPUT}{query_id}.csv"
        print(f"Query succeeded. Results at: {result_path}")
        df = pd.read_csv(result_path)
        df.to_csv("region_sales_report.csv", index=False)
        print(df)
        return df
    else:
        raise RuntimeError(f"Query failed with state: {state}")

if __name__ == "__main__":
    run_athena_query()