# مرحله 3: ایجاد جدول داده‌های بیماران
data = {
    'Group': ['Sporadic TSEs', 'CJD MM1', 'CJD MM2', 'CJD VV1', 'CJD VV2', 'CJD MV1', 'CJD MV2', 'CJD MM1+2', 'CJD VPSPr', 'Genetic TSEs', 'gCJD E200K', 'GSS P102L'],
    'n': [34, 16, 2, 3, 4, 3, 3, 2, 1, 4, 2, 2],
    'Mean_Age': [69, 75, (56+59)/2, 59, 68, 70, 57, (63+70)/2, 73, 62, (65+75)/2, (38+69)/2],
    'Male_n': [18, 12, 0, 1, 2, 1, 1, 0, 1, 1, 1, 0],
    'Female_n': [16, 4, 2, 2, 2, 2, 2, 2, 0, 3, 1, 2]
}

df_patients = pd.DataFrame(data)
print("📊 جدول 1 مقاله: ویژگی‌های گروه‌های بیماران")
print(df_patients.to_string(index=False))
print("\n---")