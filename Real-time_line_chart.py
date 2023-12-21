import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# 创建一个空的图形
fig, ax = plt.subplots()
x_data = []
y_data = []

# 初始化折线图
line, = ax.plot([], [], lw=2)

# 设置图形范围
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# 更新函数，用于实时更新折线图数据
def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 100))

    line.set_data(x_data, y_data)
    return line,

# 创建动画
ani = FuncAnimation(fig, update, frames=range(100), blit=True)

# 显示图形
plt.show()
