# مرحله 1: نصب کتابخانه‌ها (اگر روی Colab هستید، اکثر آنها از قبل نصب هستند)
!pip install pandas numpy matplotlib scipy --quiet

# مرحله 2: وارد کردن کتابخانه‌ها
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("✅ همه کتابخانه‌ها با موفقیت بارگذاری شدند!")