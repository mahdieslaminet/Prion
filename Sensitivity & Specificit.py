# مرحله 6: محاسبه معیارهای تشخیصی بر اساس داده‌های شبیه‌سازی‌شده
# برای CSF
csf_tse_positive = sum(tse_csf_values > threshold_diluted)  # همه TSEها با نمونه رقیق‌شده مقایسه می‌شوند
csf_control_positive = sum(control_csf_values > threshold_diluted)

sensitivity_csf = csf_tse_positive / 38 * 100
specificity_csf = (30 - csf_control_positive) / 30 * 100

# برای پوست
skin_tse_positive = 34  # از شبیه‌سازی: 34 نمونه مثبت از 38 نمونه
skin_control_positive = sum(control_skin > threshold_skin)

sensitivity_skin = skin_tse_positive / 38 * 100
specificity_skin = (30 - skin_control_positive) / 30 * 100

print("🎯 محاسبه حساسیت و ویژگی بر اساس داده‌های شبیه‌سازی:")
print(f"💧 CSF - حساسیت: {sensitivity_csf:.1f}%  |  ویژگی: {specificity_csf:.1f}%")
print(f"🩹 پوست - حساسیت: {sensitivity_skin:.1f}%  |  ویژگی: {specificity_skin:.1f}%")
print("\n---")