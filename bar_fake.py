import numpy as np
from matplotlib import pyplot as plt


def fake_chart():
    # 12.不同截止期系数与抖动关系图
    plt.rcParams['axes.unicode_minus'] = False  # 不使用中文减号
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为仿宋（FangSong）
    font = {
        'family': 'SimHei',
        'weight': 'normal',
        'size': 20,
    }
    labels = ['4', '6', '8', '10']
    RFSU = [43, 134, 276, 544]
    TTA = [79, 220, 584, 896]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, RFSU, width, label='并行训练模式')
    rects2 = ax.bar(x + width / 2, TTA, width, label='串行训练模式')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('训练任务数', font)
    ax.set_ylabel('时间', font)
    # ax.set_title('The results of jitter for different $c$')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.tick_params(labelsize=20)
    ax.legend(fontsize=20)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    # autolabel(rects1)
    # autolabel(rects2)
    fig.tight_layout()
    # plt.savefig("./figures/figure5-13.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


fake_chart()
