from google.colab import files
import os

# Upload your Kaggle API key (kaggle.json)
files.upload()  # Select the kaggle.json file from your local machine

# Move the key to the correct directory
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json  # Set permissions
