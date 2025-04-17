from google.colab import drive
import pandas as pd

# Mount Google Drive
drive.mount('/content/drive')

# Path to your dataset
csv_path = '/content/drive/MyDrive/colab_data/datasets/TII-SSRC-23/data.csv'

# Process in chunks (e.g., 100,000 rows at a time)
chunksize = 100_000

# Load the first chunk and assign it to df
for i, chunk in enumerate(pd.read_csv(csv_path, chunksize=chunksize, low_memory=False)):
    print(f"Chunk {i+1} shape: {chunk.shape}")
    df = chunk  # Now df is defined
    break  # Only loading the first chunk for exploration

# Preview the first few rows
df.head()
