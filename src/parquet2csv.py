#converts parquet files from /data to csv files in /data/csv

import pyarrow.parquet as pq
import pandas as pd

table = pq.read_table('data/testing_data/test1.parquet')
df = table.to_pandas()
df.to_csv('data/csv/test1.csv', index=False)

table = pq.read_table('data/testing_data/test2.parquet')
df = table.to_pandas()
df.to_csv('data/csv/test3.csv', index=False)

table = pq.read_table('data/testing_data/test3.parquet')
df = table.to_pandas()
df.to_csv('data/csv/test2.csv', index=False)

