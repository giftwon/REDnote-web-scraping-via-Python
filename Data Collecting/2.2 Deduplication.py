import pandas as pd

# Read Excel file
df = pd.read_excel('959 待清洗.xlsx')  # 替换为您的文件名

# Define a function to extract the unique ID in each URL
def extract_code(value):
    if isinstance(value, str):
        parts = value.split('/')
        if len(parts) >= 4:
            code = parts[3]
            question_mark_index = code.find('?')
            if question_mark_index != -1:
                return code[:question_mark_index]
        return None
    return None

# Apply
df['code'] = df.iloc[:, 0].apply(extract_code)

# Deduplication
unique_df = df.drop_duplicates(subset='code').reset_index(drop=True)

# Ouptput
unique_df.to_excel('原始数据已去重.xlsx', index=False)  # Save
print("去重后的数据已保存")
