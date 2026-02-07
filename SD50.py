# مرحله 7: ایجاد جدول SD50 (جدول 2 مقاله)
sd50_data = {
    'sCID type': ['MM1', 'VV2', 'MV1', 'MV2', 'VPSPr'],
    'n': [16, 4, 3, 3, 1],
    'log10 SD50/ml CSF': [6.6, 7.1, 5.8, 5.6, 5.8],
    'log10 SD50/g skin': [7.7, 7.4, 6.9, 7.4, 7.7]
}

df_sd50 = pd.DataFrame(sd50_data)
print("📊 جدول 2 مقاله: دوز متوسط سیدینگ (SD50) در CSF و پوست")
print(df_sd50.to_string(index=False))
print("\n---")