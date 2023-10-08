import sqlalchemy
import pandas as pd
import xlsxwriter
import asyncpg


def save_excel_to_db(
        engine: sqlalchemy.Engine,
        db_name="overdue",
        input_filename="data/med_data.xlsx",
        rows_to_skip=[0, 1, 2],
) -> None:
    workbook = pd.read_excel(
        input_filename,
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

    workbook[1:].to_sql(db_name, engine, if_exists="replace")


async def save_report_to_excel(report: list[asyncpg.Record]) -> None:
    workbook = xlsxwriter.Workbook("data/new_report.xlsx")

    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({"bold": True})
    worksheet.write(0, 0, "Субъект РФ", bold)
    worksheet.write(0, 1, "Суммарное количество доз", bold)
    worksheet.write(0, 2, "Среднее просрочено дней", bold)

    for i in range(len(report)):
        worksheet.write(i + 1, 0, report[i]["Субъект РФ"])
        worksheet.write(i + 1, 1, report[i]["Суммарное количество доз"])
        worksheet.write(i + 1, 2, report[i]["Среднее просрочено дней"])

    workbook.close()
