import numpy as np
import matplotlib

import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['mathtext.default'] = 'regular'

# RFSU
y1 = [30.0, 50.0, 60.0, 120.0, 180.0, 190.0, 240.0, 304.0, 390.0, 420.0, 470.0, 510.0, 500.0, 590.0, 640.0]
# TTA
y2 = [60.0, 70.0, 70.0, 100.0, 160.0, 210.0, 430.0, 470.0, 490.0, 560.0, 630.0, 690.0, 750.0, 780.0, 820.0]

COLOR = ["blue", "cornflowerblue", "mediumturquoise", "goldenrod", "yellow"]
lambda1 = lambda2 = [10 ** x for x in range(-2, 3)]

# x, y: position
x = list(range(len(lambda1)))
y = list(range(len(lambda2)))
x_tickets = [str(_x) for _x in lambda1]
y_tickets = [str(_x) for _x in lambda2]

# acc = np.random.rand(len(x), len(y))
acc = np.arange(len(x) * len(y)).reshape(len(x), len(y)) + 1
acc = acc / acc.max()

# 注意顺序问题，见 [9]
# 2022.3.27：这里正常用，要反的**不**是这里，而是后文的 `acc.ravel()` 那里
xx, yy = np.meshgrid(x, y)  # 2022.3.27：这里正常用，要反的**不**是这里
# yy, xx = np.meshgrid(x, y)  # 2022.3.27：这里**别**反

# print(xx)
# print(yy)
color_list = []
for i in range(len(y)):
    c = COLOR[i]
    color_list.append([c] * len(x))
color_list = np.asarray(color_list)
# print(color_list)
# 2022.3.27：注意这里 `acc` 在 `ravel()` 之前要转置（`.T`）一下，见 [9]
xx_flat, yy_flat, acc_flat, color_flat = \
    xx.ravel(), yy.ravel(), acc.T.ravel(), color_list.ravel()
# print(xx_flat)
# print(yy_flat)


# fig, ax = plt.subplots(projection="3d")
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.bar3d(xx_flat - 0.35, yy_flat - 0.35, 0, 0.7, 0.7, acc_flat,
         color=color_flat,  # 颜色
         edgecolor="black",  # 黑色描边
         shade=True)  # 加阴影

# 坐标轴名
ax.set_xlabel(r"$\lambda_1$")
ax.set_ylabel(r"$\lambda_2$")
ax.set_zlabel("ACC")

# 座标轴范围
ax.set_zlim((0, 1.01))

# 座标轴刻度标签
# 似乎要 `set_*ticks` 先，再 `set_*ticklabels`
# has to call `set_*ticks` to mount `ticklabels` to corresponding `ticks` ?
ax.set_xticks(x)
ax.set_xticklabels(x_tickets)
ax.set_yticks(y)
ax.set_yticklabels(y_tickets)

# 保存
# plt.tight_layout()
# fig.savefig("bar3d.png", bbox_inches='tight', pad_inches=0)
# plt.close(fig)
plt.show()
