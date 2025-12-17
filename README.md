# FNBT-Fee-Optimization-Analysis

## Project Title: FNBT Operational Efficiency & Fee Revenue Stream Optimization

### Project Summary

This end-to-end data analysis portfolio project addresses a critical business problem for a financial institution: **reducing operational costs and increasing net fee revenue by analyzing and optimizing the customer fee reversal process, specifically for Non-Sufficient Funds (NSF) and Overdraft fees.**

Research into First National Bank Texas (FNBT) and industry challenges highlighted customer service issues related to fee disputes, which directly impact the bank's operational efficiency and bottom line due to fee reversals. This project implements a full Data Analysis life cycle—from ETL/ELT in SQL to advanced driver analysis in Python—to deliver actionable insights to stakeholders.

The entire project is structured to directly map to the **Data Analyst Job Description at First National Bank Texas in Killeen, TX**, demonstrating proficiency in key required skills: SQL data maintenance, ETL/ELT automation, and robust reporting.

---

## Business Problem & Goal

Based on research and typical banking pain points (e.g., high volumes of customer service complaints related to fees), the scenario is as follows:

1. **Business Problem:** FNBT's Net Fee Revenue is being significantly eroded by a high rate of fee reversals (waived fees), particularly those related to customers successfully curing an overdraft within a 24-hour grace period (a common bank policy). This high reversal volume indicates customer confusion, inefficient policy execution, or systemic issues in the transaction posting process.
2. **Project Goal:** Identify the key drivers of fee reversals, measure the variance in net fee revenue, and recommend operational or policy adjustments to increase the *valid* fee collection rate by **15%** without compromising customer goodwill.

---

## Project Architecture & Tool Stack

| Phase | Tool(s) Used | Deliverable(s) & Skills Demonstrated |
| --- | --- | --- |
| **Data Storage** | Google BigQuery (`driiiportfolio` Project ID) | Created tables (`T1`, `T2`, `T3`) and maintained relational data schema. |
| **ETL/ELT & Data Maintenance** | SQL (`S1_FNBT_Fee_ETL_Load_and_Clean.sql`) | Data type casting, exception handling, data reconciliation, and data cleaning. **Directly addresses: *Maintain datasets using Oracle / SQL* and *Integrate automation, ETL / ELT of data***. |
| **Core Analysis** | Python (`P1_FNBT_Advanced_Fee_Driver_Analysis.ipynb`), SQL (`Q2_Fee_Variance_Analysis.sql`) | Advanced time-series analysis (hourly reversal rates), customer segmentation (High-Risk), and aggregation for reporting. **Directly addresses: *Perform research and analysis on assigned areas***. |
| **Reporting & Visualization** | Looker Studio (Conceptual), Python CSV Output | Automated generation of the final dashboard source (`D1_FNBT_Fee_Optimization_Report.csv`). Creation of a dashboard for distribution. **Directly addresses: *Create, maintain, and distribute assigned department reporting***. |

---

## Repository Structure & Deliverables

| File/Folder Name | Description | Key Skill Alignment |
| --- | --- | --- |
| **`README.md`** | **This document.** Project summary, business context, architecture, and job requirement mapping. | Stakeholder Communication |
| **`data_dictionary.csv`** | **Data Governance Document.** Defines the schema for the synthetic `transactional_fees` dataset used in BigQuery. | Data Documentation/Data Quality |
| **`SQL/`** | **BigQuery Scripts (Optimized)** |  |
|     `S1_FNBT_Fee_ETL_Load_and_Clean.sql` | **Data Transformation.** Full-length SQL for loading raw data into `T1` and transforming it into the clean `T2` fact table, including data quality checks and reconciliation. | ETL/ELT, Data Reconciliation, SQL Optimization |
|     `Q2_Fee_Variance_Analysis.sql` | **Reporting Aggregation.** Full-length SQL to create the `T3` aggregated performance table for monthly/quarterly variance analysis of net fee revenue and reversal rates. | Reporting, Data Modeling |
| **`Notebooks/`** | **Google Colab Python Analysis** |  |
|     `P1_FNBT_Advanced_Fee_Driver_Analysis.ipynb` | **Driver Analysis & Automation.** Python notebook for connecting to BigQuery, performing time-based analysis (e.g., 24-hour policy analysis), and generating the final dashboard report (`D1`). | Python, BigQuery Integration, Advanced Analysis, Automation |
| **`Data/`** | **Final Project Assets** |  |
|     `D1_FNBT_Fee_Optimization_Report.csv` | **Final Dashboard Source.** The aggregated data export from the Python script, ready for immediate upload/connection to a visualization tool. | Data Distribution, Reporting |

---

## Key Insight Example (from `P1_FNBT_Advanced_Fee_Driver_Analysis.ipynb`)

A critical analysis performed was examining fee reversal rates by the **hour of the transaction**. The goal was to test the effectiveness of the bank's 24-hour grace period ("No Harm No Foul" policy, as mentioned in the research).

**Hypothesis:** If the policy is working efficiently, the reversal rate should be relatively consistent. If the reversal rate spikes in the hours *immediately following* the fee assessment, it suggests customers are struggling to cure the overdraft in time, leading to higher customer service disputes and eventual reversals.

| Metric | Recommendation for Stakeholders | Job Alignment |
| --- | --- | --- |
| **High Reversal Rate at 10:00 AM** | Investigate why transactions at this time have the highest likelihood of reversal. Could the daily ACH cutoff time conflict with the 24-hour cure window, causing legitimate deposits to post too late? | **Research and Analysis** |
| **High-Risk Customer Segment** | **Operational Recommendation:** Flag high-risk customers (`is_high_risk_customer = TRUE`) for targeted financial literacy outreach or automatically extend their cure window to 36 hours to reduce dispute volume. | **Integrate Automation** (of customer flagging), **Reporting** |
