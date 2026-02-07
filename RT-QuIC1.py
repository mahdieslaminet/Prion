# مرحله 4: تولید داده‌های شبیه‌سازی‌شده برای نمونه‌های CSF
np.random.seed(42)  # برای تکرارپذیری نتایج

# داده‌های گروه TSE (38 نمونه): 30 نمونه رقیق‌نشده قوی، 8 نمونه رقیق‌شده
tse_undiluted = np.random.normal(loc=230000, scale=50000, size=30)  # میانگین 23e4
tse_diluted = np.random.normal(loc=210000, scale=60000, size=8)     # میانگین 21e4
tse_csf_values = np.concatenate([tse_undiluted, tse_diluted])
tse_csf_labels = ['TSE Undiluted']*30 + ['TSE Diluted']*8

# داده‌های گروه کنترل غیر TSE (30 نمونه)
control_undiluted = np.random.normal(loc=19000, scale=5000, size=27)   # میانگین 19e3
control_diluted_low = np.random.normal(loc=40000, scale=10000, size=3) # 3 نمونه با سیگنال بالاتر
control_csf_values = np.concatenate([control_undiluted, control_diluted_low])
control_csf_labels = ['Control']*30

# ترکیب همه داده‌های CSF
all_csf_values = np.concatenate([tse_csf_values, control_csf_values])
all_csf_labels = tse_csf_labels + ['Control']*30
all_csf_groups = ['TSE']*38 + ['Control']*30

df_csf = pd.DataFrame({
    'Fluorescence_AU': all_csf_values,
    'Subgroup': all_csf_labels,
    'Group': all_csf_groups
})

# محاسبه آستانه (Threshold) مطابق مقاله: میانگین کنترل + 5 انحراف معیار
threshold_undiluted = control_undiluted.mean() + 5 * control_undiluted.std()
threshold_diluted = control_csf_values.mean() + 5 * control_csf_values.std()

print("📈 خلاصه داده‌های شبیه‌سازی‌شده CSF (واحد فلورسانس AU):")
print(df_csf.groupby(['Group', 'Subgroup'])['Fluorescence_AU'].describe())
print(f"\n📏 آستانه تشخیص برای نمونه‌های رقیق‌نشده: {threshold_undiluted:,.0f} AU")
print(f"📏 آستانه تشخیص برای نمونه‌های رقیق‌شده: {threshold_diluted:,.0f} AU")
print("\n---")