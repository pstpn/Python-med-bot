import pandas as pd
from sqlalchemy import create_engine


conn_string = "postgresql://postgres:admin@localhost/meddata"
rows_to_skip = [0, 1, 2]

workbook = pd.read_excel(
    "data/med_data.xlsx",
    skiprows=rows_to_skip,
    index_col=0,
    names=[
        "subject",
        "mo",
        "tax_id",
        "status",
        "withdrawal_type",
        "gtin",
        "batch",
        "doses_in_package",
        "packages_count",
        "doses_count",
        "ex_date",
        "ex_days",
    ],
)

workbook[1:].to_sql("overdue", create_engine(conn_string), if_exists="replace")
