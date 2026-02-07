# مرحله 8: رسم نمودارها
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# نمودار 1: نقطه‌ای (Dot Plot) برای CSF (شبیه شکل 1A)
ax1 = axes[0, 0]
# داده‌های TSE
for i, (val, lbl) in enumerate(zip(tse_csf_values, tse_csf_labels)):
    color = 'red' if 'Undiluted' in lbl else 'limegreen'
    ax1.plot(i, val, 'o', color=color, alpha=0.6)
# داده‌های کنترل
for i, val in enumerate(control_csf_values, start=38):
    ax1.plot(i, val, '^', color='black', alpha=0.6)

ax1.axhline(y=threshold_undiluted, color='black', linestyle=':', label='آستانه رقیق‌نشده')
ax1.axhline(y=threshold_diluted, color='blue', linestyle='-.', label='آستانه رقیق‌شده')
ax1.set_ylim(0, 350000)
ax1.set_title('(A) شبیه‌سازی شکل 1 مقاله: نمونه‌های CSF', fontweight='bold')
ax1.set_ylabel('فلورسانس ThT (AU)')
ax1.set_xlabel('نمونه‌ها')
ax1.legend()
ax1.grid(True, alpha=0.3)

# نمودار 2: نقطه‌ای برای پوست (شبیه شکل 2A)
ax2 = axes[0, 1]
# داده‌های TSE پوست
for i, val in enumerate(tse_skin_values):
    ax2.plot(i, val, 'o', color='red', alpha=0.6)
# داده‌های کنترل پوست
for i, val in enumerate(control_skin, start=38):
    ax2.plot(i, val, '^', color='black', alpha=0.6)

ax2.axhline(y=threshold_skin, color='black', linestyle=':', label='آستانه')
ax2.set_ylim(0, 250000)
ax2.set_title('(B) شبیه‌سازی شکل 2 مقاله: نمونه‌های پوست', fontweight='bold')
ax2.set_ylabel('فلورسانس ThT (AU)')
ax2.set_xlabel('نمونه‌ها')
ax2.legend()
ax2.grid(True, alpha=0.3)

# نمودار 3: منحنی زمانی برای CSF (شبیه شکل 1B)
ax3 = axes[1, 0]
# شبیه‌سازی منحنی رشد
time_points = np.linspace(0, 60, 100)  # 60 ساعت
# تابع سیگموئید برای شبیه‌سازی رشد
def sigmoid(t, t50, k):
    return 1 / (1 + np.exp(-k * (t - t50)))

# تولید منحنی‌های میانگین
curve_undiluted = 230000 * sigmoid(time_points, t50=15, k=0.3) + np.random.normal(0, 10000, len(time_points))
curve_diluted = 210000 * sigmoid(time_points, t50=10, k=0.4) + np.random.normal(0, 10000, len(time_points))
curve_control = 19000 * sigmoid(time_points, t50=30, k=0.1) + np.random.normal(0, 5000, len(time_points))

ax3.plot(time_points, curve_undiluted, color='red', label='TSE رقیق‌نشده')
ax3.plot(time_points, curve_diluted, color='limegreen', label='TSE رقیق‌شده')
ax3.plot(time_points, curve_control, color='black', label='کنترل')
ax3.set_title('(C) شبیه‌سازی منحنی‌های زمانی CSF', fontweight='bold')
ax3.set_xlabel('زمان (ساعت)')
ax3.set_ylabel('فلورسانس ThT (AU)')
ax3.legend()
ax3.grid(True, alpha=0.3)

# نمودار 4: منحنی زمانی برای پوست (شبیه شکل 2B)
ax4 = axes[1, 1]
curve_skin_tse = 120000 * sigmoid(time_points, t50=12, k=0.35) + np.random.normal(0, 15000, len(time_points))
curve_skin_control = 20000 * sigmoid(time_points, t50=35, k=0.15) + np.random.normal(0, 8000, len(time_points))

ax4.plot(time_points, curve_skin_tse, color='red', label='TSE پوست')
ax4.plot(time_points, curve_skin_control, color='black', label='کنترل پوست')
ax4.set_title('(D) شبیه‌سازی منحنی‌های زمانی پوست', fontweight='bold')
ax4.set_xlabel('زمان (ساعت)')
ax4.set_ylabel('فلورسانس ThT (AU)')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()