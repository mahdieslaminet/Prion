# مرحله 5: تولید داده‌های شبیه‌سازی‌شده برای نمونه‌های پوست
# داده‌های گروه TSE پوست (38 نمونه): 31 مثبت، 7 منفی/ضعیف که بعد از تکرار 3 تای آن مثبت شد
tse_skin_positive = np.random.normal(loc=120000, scale=57000, size=34)  # 31 + 3
tse_skin_weak = np.random.normal(loc=40000, scale=20000, size=4)        # 7 - 3
tse_skin_values = np.concatenate([tse_skin_positive, tse_skin_weak])
tse_skin_labels = ['TSE Skin']*38

# داده‌های گروه کنترل غیر TSE پوست (30 نمونه)
control_skin = np.random.exponential(scale=20000, size=30)  # توزیع نامتقارن برای شبیه‌سازی داده‌های واقعی
control_skin_labels = ['Control']*30

# ترکیب همه داده‌های پوست
all_skin_values = np.concatenate([tse_skin_values, control_skin])
all_skin_labels = tse_skin_labels + control_skin_labels
all_skin_groups = ['TSE']*38 + ['Control']*30

df_skin = pd.DataFrame({
    'Fluorescence_AU': all_skin_values,
    'Group': all_skin_groups
})

# محاسبه آستانه پوست
threshold_skin = control_skin.mean() + 5 * control_skin.std()

print("📈 خلاصه داده‌های شبیه‌سازی‌شده پوست (واحد فلورسانس AU):")
print(df_skin.groupby('Group')['Fluorescence_AU'].describe())
print(f"\n📏 آستانه تشخیص برای نمونه‌های پوست: {threshold_skin:,.0f} AU")
print("\n---")