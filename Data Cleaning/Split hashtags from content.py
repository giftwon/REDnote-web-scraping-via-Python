import pandas as pd
import re

# 读取 Excel 文件
df = pd.read_excel('已去重.xlsx')

# 定义提取关键词的函数
def extract_keywords(content):
    if isinstance(content, str):
        pattern = r'(#\w+)(?:[^\w\s]*)'
        hashtags = re.findall(pattern, content)
        return '; '.join(hashtags)
    return ''

# Apply the hashtags split funtion
df['hashtags'] = df['Content'].apply(extract_keywords)

# Write in a new Excel file
df.to_excel('已去重hashtags分割.xlsx', index=False)  # Save
print("Successfully saved")
