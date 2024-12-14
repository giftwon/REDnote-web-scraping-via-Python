import pandas as pd
import re

# Read Excel
df = pd.read_excel('已去重hashtags待分割.xlsx')

# Define a function
def replace_chinese_with_zero(value):
    if isinstance(value, str):
        # Chinese charcters are turned to zero if there is no Likes, Collects, and Comments
        value = re.sub(r'[\u4e00-\u9fa5]', '0', value)
        value = re.sub(r'0+', '0', value)
        return value
    return value

# Apply a replacement function to specified columns
for column in ['Likes', 'Collects', 'Comments']:
    df[column] = df[column].apply(replace_chinese_with_zero)

    df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).astype(int)

# Write in a new Excel file
df.to_excel('replacechinesewithzero.xlsx', index=False)  # Save
print("Successfully saved")
