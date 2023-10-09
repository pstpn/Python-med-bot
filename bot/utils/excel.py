import sqlalchemy
import pandas as pd
import xlsxwriter


output_filename = "data/report.xlsx"


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


def save_report_to_excel(
        report: list[tuple],
        title=["Субъект РФ", "Суммарное количество доз", "Среднее просрочено дней"],
) -> None:
    workbook = xlsxwriter.Workbook(output_filename)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({"bold": True})

    for i, col_name in enumerate(title):
        worksheet.write(0, i, col_name, bold)

    for i in range(len(report)):
        for j in range(len(title)):
            worksheet.write(i + 1, j, report[i][j])

    workbook.close()
