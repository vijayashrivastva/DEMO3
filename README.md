# Data Analytics with S3 and Athena for Reporting

This project demonstrates running SQL analytics queries on Amazon Athena using data stored in Amazon S3, generating reports via Python Pandas, and automating the workflow with GitHub Actions.

## Steps
1. Upload CSV files to S3 under `raw/` folder.
2. Use Athena or Glue to create a table referencing the data.
3. Run `python analytics/query_athena.py` to fetch data.
4. Run `python analytics/report_generator.py` to create CSV + visual report.
5. Reports are uploaded to `s3://<your-bucket>/reports/`.

## Automation
The GitHub Actions workflow runs daily at 3 AM UTC to refresh analytics reports automatically.

## Next Steps
- Add Athena CTAS (Create Table As Select) queries for pre-aggregated data.
- Integrate QuickSight for dashboarding.
- Parameterize queries for multi-region filtering.
```
