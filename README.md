\# Automated PDF Report Generator



An enterprise-style Python automation application that processes CSV data, generates professional PDF reports, and supports scheduled report generation through a command-line interface.



\## Features



\* CSV data processing using Pandas

\* Automated PDF report generation

\* Summary statistics and data preview

\* CLI interface using `argparse`

\* Daily automated scheduling using `schedule`

\* Python package configuration using `pyproject.toml`

\* Editable package installation

\* Configurable input and output file paths

\* Structured project architecture

\* Execution-ready CLI command



\## Technologies



\* Python 3.10+

\* Pandas

\* ReportLab

\* Schedule

\* Argparse

\* Setuptools



\## Project Structure



```text

automated-pdf-report-generator/

│

├── data/

│   └── sample\_data.csv

│

├── docs/

│   └── architecture-diagram.png

│

├── reports/

│   ├── report.pdf

│   └── monthly-report.pdf

│

├── src/

│

├── main.py

├── pyproject.toml

├── requirements.txt

├── README.md

└── .gitignore

```



\## Installation



Create and activate a virtual environment:



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



Install the project as an editable package:



```powershell

pip install -e .

```



\## Usage



\### Generate a PDF report



```powershell

python main.py

```



\### Generate a report with custom input and output



```powershell

python main.py --input data/sample\_data.csv --output reports/monthly-report.pdf

```



\### Run using the installed CLI



```powershell

pdf-report

```



\### Start the automated scheduler



```powershell

python main.py --schedule

```



The scheduler is configured to generate the report daily at 09:00.



Press `Ctrl+C` to stop the scheduler.



\## Input Data



The application accepts CSV files containing structured data.



Example:



```csv

Date,Department,Sales,Expenses,Employees

2026-09-01,Electronics,125000,75000,12

2026-09-02,Software,150000,82000,18

2026-09-03,IoT,98000,55000,10

```



\## Report Output



The generated PDF contains:



\* Report generation timestamp

\* Total record count

\* Number of numeric columns

\* Average values for numeric columns

\* Source data preview



Generated reports are stored inside the `reports/` directory.



\## Architecture



```text

CSV Input

&#x20;  ↓

Pandas Data Processing

&#x20;  ↓

Data Analysis

&#x20;  ↓

ReportLab PDF Generator

&#x20;  ↓

PDF Report

&#x20;  ↓

reports/

```



For automation:



```text

CLI / Scheduler

&#x20;     ↓

Data Loader

&#x20;     ↓

Pandas Processing

&#x20;     ↓

PDF Generator

&#x20;     ↓

Automated Report

```



\## Validation



The application was tested for:



\* PDF generation

\* Custom CLI arguments

\* Scheduler startup

\* Package installation

\* Installed CLI command

\* CSV data processing



Example successful output:



```text

PDF report generated successfully: reports/report.pdf

```



\## Project Purpose



This project demonstrates practical Python automation skills including data processing, document generation, command-line application development, package configuration, and automated scheduling.



\## License



This project is created for educational and portfolio purposes.



