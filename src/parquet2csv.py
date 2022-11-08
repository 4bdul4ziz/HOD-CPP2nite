#converts parquet files from /data to csv files in /data/csv

import pyarrow.parquet as pq
import pandas as pd

table = pq.read_table('data/training_data/train1.parquet')
df = table.to_pandas()
df.to_csv('data/csv/train/train1.csv', index=False)

table = pq.read_table('data/training_data/train2.parquet')
df = table.to_pandas()
df.to_csv('data/csv/train/train2.csv', index=False)

table = pq.read_table('data/training_data/train3.parquet')
df = table.to_pandas()
df.to_csv('data/csv/train/train3.csv', index=False)

