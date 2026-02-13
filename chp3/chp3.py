import numpy as np
import matplotlib.pyplot as plt

# 1. 定義參數
L = 2 * np.pi          # 範圍
n = 50                 # 點數
dx = L / (n - 1)       # 間距 h
x = np.linspace(0, L, n)
u = np.sin(x)          # 原始函數

# 2. 執行二階精確度數值微分
ux = np.zeros_like(u)

# 左邊界 (Forward)
ux[0] = (-3 * u[0] + 4 * u[1] - u[2]) / (2 * dx)

# 內部點 (Central)
ux[1:n-1] = (u[2:] - u[:n-2]) / (2 * dx)

# 右邊界 (Backward)
ux[n-1] = (3 * u[n-1] - 4 * u[n-2] + u[n-3]) / (2 * dx)

# 3. 解析解 (用於對比)
exact_ux = np.cos(x)

# 4. 計算誤差
error = np.abs(ux - exact_ux)

print(f"最大誤差: {np.max(error):.2e}")
