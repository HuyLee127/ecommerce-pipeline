# E-commerce Data Pipeline

End-to-end data pipeline for analyzing e-commerce orders from Vietnamese platforms (Shopee, Tiki, Lazada). Built as portfolio project for Data Engineer track.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-3.0.2-150458.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

This project implements a data cleaning and processing pipeline for e-commerce order data. The pipeline handles common data quality issues encountered in real-world e-commerce datasets:

- Missing required fields (order IDs, timestamps)
- Duplicate transactions from retry mechanisms
- Invalid date formats from heterogeneous sources
- Negative or zero amounts indicating refunds or errors

## Features

- **Data validation**: Removes records with missing critical fields
- **Deduplication**: Eliminates duplicate orders by `order_id`
- **Date normalization**: Converts mixed date formats to standard datetime, gracefully handles invalid entries
- **Amount filtering**: Excludes orders with non-positive amounts
- **Type safety**: Uses Python type hints for better code reliability

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.11+ |
| Data Processing | pandas 3.0.2 |
| Database | PostgreSQL (planned) |
| Orchestration | Apache Airflow (planned) |
| Version Control | Git, GitHub |

## Project Structure

```
ecommerce-pipeline/
├── data/
│   ├── raw/              # Raw input data (gitignored)
│   ├── processed/        # Cleaned intermediate data
│   └── output/           # Final pipeline outputs
├── src/
│   └── clean_orders.py   # Order data cleaning logic
├── tests/                # Unit tests
├── logs/                 # Pipeline execution logs
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.11 or higher
- Git

### Installation

Clone the repository:

```bash
git clone git@github.com:HuyLee127/ecommerce-pipeline.git
cd ecommerce-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the order cleaning function with sample data:

```bash
python src/clean_orders.py
```

Expected output:

```
  order_id order_date    amount
0    SP001 2026-01-15    150000
1    SP002 2026-01-16    250000
```

## Development Workflow

This project follows industry-standard Git workflow:

- **Feature branching**: All changes go through dedicated branches (`feat/*`, `fix/*`, `refactor/*`, `chore/*`, `docs/*`)
- **Pull Requests**: Every merge to `main` requires a PR with description
- **Conventional Commits**: Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) specification
- **Squash and merge**: Branches are squashed for clean main history

## Roadmap

- [x] Phase 1: Project setup and data cleaning function
- [ ] Phase 2: SQL ingestion to PostgreSQL
- [ ] Phase 3: Unit tests with pytest
- [ ] Phase 4: Pipeline orchestration with Airflow
- [ ] Phase 5: Data quality monitoring
- [ ] Phase 6: Visualization dashboard

## Author

**Le Gia Huy**
Data Engineer Track | HCMUT
- GitHub: [@HuyLee127](https://github.com/HuyLee127)

## License

This project is licensed under the MIT License.
