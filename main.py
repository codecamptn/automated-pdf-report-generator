import argparse
import os
import schedule
import time
from datetime import datetime

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def load_data(csv_file):
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"Data file not found: {csv_file}")

    return pd.read_csv(csv_file)


def generate_report(df, output_file):
    os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)

    total_records = len(df)
    numeric_columns = df.select_dtypes(include="number").columns

    summary_data = [
        ["Metric", "Value"],
        ["Generated At", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        ["Total Records", str(total_records)],
        ["Numeric Columns", str(len(numeric_columns))],
    ]

    for column in numeric_columns:
        summary_data.append(
            [f"Average {column}", f"{df[column].mean():.2f}"]
        )

    document = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph("Automated Data Analysis Report", styles["Title"])
    )
    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "Enterprise Python Automation Capstone Project",
            styles["Heading2"],
        )
    )
    story.append(Spacer(1, 15))

    summary_table = Table(summary_data, colWidths=[220, 250])

    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("PADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    story.append(summary_table)
    story.append(Spacer(1, 20))

    story.append(
        Paragraph("Source Data Preview", styles["Heading2"])
    )
    story.append(Spacer(1, 10))

    preview = df.head(10)

    table_data = [list(preview.columns)] + preview.astype(str).values.tolist()

    data_table = Table(table_data, repeatRows=1)

    data_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("PADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )

    story.append(data_table)

    document.build(story)

    print(f"PDF report generated successfully: {output_file}")


def run_scheduled_report():
    print("Running scheduled report...")

    try:
        df = load_data("data/sample_data.csv")
        generate_report(df, "reports/scheduled-report.pdf")
        print("Scheduled report completed.")
    except Exception as error:
        print(f"Scheduled report failed: {error}")


def run_scheduler():
    schedule.every().day.at("09:00").do(run_scheduled_report)

    print("Scheduler started.")
    print("Daily report time: 09:00")
    print("Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    parser = argparse.ArgumentParser(
        description="Enterprise Automated PDF Report Generator"
    )

    parser.add_argument(
        "--input",
        default="data/sample_data.csv",
        help="Path to input CSV file",
    )

    parser.add_argument(
        "--output",
        default="reports/report.pdf",
        help="Path for generated PDF report",
    )

    parser.add_argument(
        "--schedule",
        action="store_true",
        help="Start the daily report scheduler",
    )

    args = parser.parse_args()

    if args.schedule:
        run_scheduler()
        return

    try:
        df = load_data(args.input)
        generate_report(df, args.output)
    except Exception as error:
        print(f"Error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()