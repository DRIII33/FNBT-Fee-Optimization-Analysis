#INSTALL PACKAGES
!pip install pandas

--------

# P0_Synthetic_Data_Generator.ipynb
# Description: Generates realistic synthetic transactional fee data based on the data_dictionary.csv.
# The data is structured to simulate the '24-hour cure' policy challenge and customer disputes.

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuration
NUM_RECORDS = 15000  # Generate 15,000 transactions for a robust dataset
PROJECT_START_DATE = datetime(2023, 1, 1)
PROJECT_END_DATE = datetime(2024, 6, 30)

# ----------------------------------------------------------------------------------
# 1. GENERATE BASE DATA
# ----------------------------------------------------------------------------------

# Generate random dates and times
dates = [PROJECT_START_DATE + (PROJECT_END_DATE - PROJECT_START_DATE) * np.random.rand() for _ in range(NUM_RECORDS)]

# Generate Customer IDs (Simulate a split of customer types)
customer_ids = [f'CUST_{i:05d}' for i in np.random.choice(range(1, 2000), NUM_RECORDS)]

# Transaction/Fee Types
transaction_types = np.random.choice(['ACH_DEBIT', 'POS_PURCHASE', 'ATM_WITHDRAWAL', 'BILL_PAY'], NUM_RECORDS, p=[0.4, 0.35, 0.15, 0.1])
fee_types = np.random.choice(['NSF', 'OVERDRAFT'], NUM_RECORDS, p=[0.6, 0.4])

# Simulate fee amounts (FNBT fee is $34)
fee_amounts = ['$34.00'] * NUM_RECORDS

# Policy Version - Simulate a policy change over time
POLICY_CHANGE_DATE = datetime(2023, 10, 1)
policy_versions = ['V2_24H_CURE' if d > POLICY_CHANGE_DATE else 'V1_STRICT' for d in dates]

# ----------------------------------------------------------------------------------
# 2. INTRODUCE REVERSAL LOGIC (Simulating the business problem)
# ----------------------------------------------------------------------------------

# Baseline reversal rate
is_reversed = np.random.choice([0, 1], NUM_RECORDS, p=[0.85, 0.15]) # 15% overall reversal rate

# Add noise based on transaction time (Simulate 24-hour cure window issues)
# Higher reversal rate for fees assessed in the early morning (e.g., 5 AM - 8 AM)
for i in range(NUM_RECORDS):
    hour = dates[i].hour
    if 5 <= hour <= 8:
        # Increase reversal probability for the "danger zone" hours
        if np.random.rand() < 0.25: # 25% chance of reversal in danger zone
            is_reversed[i] = 1

# Define Reversal Reasons (aligned with business context)
reasons_choices = ['CUST_DISPUTE_24H_CURE', 'FRAUD_CLAIM', 'GOODWILL_WAIVER']
reversal_reasons = np.full(NUM_RECORDS, 'NONE', dtype='<U30')

# Assign reasons only to reversed transactions
reversed_indices = np.where(is_reversed == 1)[0]
reversal_reasons[reversed_indices] = np.random.choice(reasons_choices, len(reversed_indices), p=[0.60, 0.25, 0.15])

# Generate Branch Locations (Simulate local focus)
branch_locations = np.random.choice(['KILLEEN MAIN', 'FORT HOOD GATE', 'TEMPLE HWY', 'AUSTIN DOWNTOWN', 'DALLAS NW'], NUM_RECORDS, p=[0.3, 0.25, 0.15, 0.2, 0.1])

# Calculate a random reversal date (Must be after the transaction date)
reversal_dates = []
for i in range(NUM_RECORDS):
    if is_reversed[i] == 1:
        # Reversal happens within 1 to 10 days
        reversal_delta = timedelta(days=np.random.randint(1, 11))
        reversal_dates.append((dates[i] + reversal_delta).strftime('%Y-%m-%d'))
    else:
        reversal_dates.append(None)


# ----------------------------------------------------------------------------------
# 3. CREATE FINAL DATAFRAME
# ----------------------------------------------------------------------------------
df_synth = pd.DataFrame({
    'transaction_id': [f'TRX_{i:06d}' for i in range(NUM_RECORDS)],
    'customer_id': customer_ids,
    'branch_location': branch_locations,
    'transaction_timestamp': [d.strftime('%Y-%m-%d %H:%M:%S') for d in dates],
    'transaction_type': transaction_types,
    'fee_type': fee_types,
    'fee_amount_usd_str': fee_amounts,
    'is_reversed_flag': is_reversed,
    'reversal_reason': reversal_reasons,
    'reversal_date_str': reversal_dates,
    'policy_version': policy_versions
})

# Display a quick preview and save
print(f"Generated {len(df_synth)} synthetic records.")
print("\nSynthetic Data Head:")
print(df_synth.head().to_markdown(index=False))

# Save the final CSV for BigQuery Upload (Step 1.6)
df_synth.to_csv('synthetic_fnbt_fees.csv', index=False)
print("\nFile saved: synthetic_fnbt_fees.csv (Ready for BigQuery T1 upload)")

