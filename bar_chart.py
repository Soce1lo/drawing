import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def chart4():
    # 4.不同周期系数下的成功调度率与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['5', '10', '15', '20']
    phi3 = [0.93, 0.9, 0.86, 0.75]
    phi10 = [0.97, 0.96, 0.94, 0.86]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, phi3, width, label=r'$\varphi$=3')
    rects2 = ax.bar(x + width / 2, phi10, width, label=r'$\varphi$=10')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Number of Flows', font)
    ax.set_ylabel('Successful Scheduling Ratio', font)
    # ax.set_title('The results of successful scheduling ratio for different period coefficients')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.tick_params(labelsize=20)
    # 调整图例在图中的绝对位置
    # 两个参数表示比例 （1，0）右下 （0，1）左上
    # ax.legend(bbox_to_anchor=(0.83, 0.84))
    ax.legend(loc='lower right', fontsize=20)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-5.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart5():
    # 5.不同周期系数下算法运行时间与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['5', '10', '15', '20']
    phi3 = [1, 3, 3.4, 4.2]
    phi10 = [0.9, 2.8, 3, 4]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, phi3, width, label=r'$\varphi$=3')
    rects2 = ax.bar(x + width / 2, phi10, width, label=r'$\varphi$=10')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Number of Flows', font)
    ax.set_ylabel('Running Time', font)
    ax.tick_params(labelsize=20)
    # ax.set_title('The results of running time for different period coefficients')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-6.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart6():
    # 6.不同ε下算法成功调度率与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['5', '10', '15', '20']
    eps3 = [0.92, 0.87, 0.83, 0.76]
    eps7 = [1, 0.95, 0.93, 0.85]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, eps3, width, label=r'$\varepsilon$=0.3')
    rects2 = ax.bar(x + width / 2, eps7, width, label=r'$\varepsilon$=0.7')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Number of Flows', font)
    ax.set_ylabel('Successful Scheduling Ratio', font)
    ax.tick_params(labelsize=20)
    # ax.set_title('The results of successful scheduling ratio for different ' + r'$\varepsilon$')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc='lower right', fontsize=20)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-7.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart7():
    # 7.不同ε下算法运行时间与流数量柱状图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['5', '10', '15', '20']
    eps3 = [1.8, 2.7, 4.8, 5.9]
    eps7 = [1, 2.5, 4.5, 5.5]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, eps3, width, label=r'$\varepsilon$=0.3')
    rects2 = ax.bar(x + width / 2, eps7, width, label=r'$\varepsilon$=0.7')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Number of Flows', font)
    ax.set_ylabel('Running Time', font)
    # ax.set_title('The results of running time for different ' + r'$\varepsilon$')
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-8.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart11():
    # 11.截止期系数与平均延迟时间关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['4', '6', '8', '10']
    RFSU = [30, 186, 410, 634]
    TTA = [68, 169, 564, 827]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, RFSU, width, label='RFSU')
    rects2 = ax.bar(x + width / 2, TTA, width, label='TTA')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Deadline Coefficient $c$', font)
    ax.set_ylabel('Average Delay Time', font)
    # ax.set_title('The Results of Average Delay Time for Different $c$')
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-12.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart12():
    # 12.不同截止期系数与抖动关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['4', '6', '8', '10']
    RFSU = [43, 201, 427, 644]
    TTA = [49, 220, 584, 896]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, RFSU, width, label='RFSU')
    rects2 = ax.bar(x + width / 2, TTA, width, label='TTA')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Deadline Coefficient $c$', font)
    ax.set_ylabel('Jitter', font)
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-13.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart13():
    # 13.不同截止期系数与延迟流比率关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['4', '6', '8', '10']
    RFSU = [0.286, 0.349, 0.376, 0.458]
    TTA = [0.29, 0.488, 0.56, 0.654]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, RFSU, width, label='RFSU')
    rects2 = ax.bar(x + width / 2, TTA, width, label='TTA')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Deadline Coefficient $c$', font)
    ax.set_ylabel('Delay Flow Ratio', font)
    # ax.set_title('The results of delay flow ratio for different $c$')
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-14.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart14():
    # 14.不同TT流比率与平均延迟时间关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['0.3', '0.4', '0.5', '0.6']
    RFSU = [23, 64, 388, 637]
    TTA = [42, 66, 492, 828]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, RFSU, width, label='RFSU')
    rects2 = ax.bar(x + width / 2, TTA, width, label='TTA')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('TT Flow ratio ' + r'$\alpha$', font)
    ax.set_ylabel('Average Delay Time', font)
    # ax.set_title('The results of average delay time for different ' + r'$\alpha$')
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-15.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart15():
    # 15.不同TT流比率与平均延迟时间关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['0.3', '0.4', '0.5', '0.6']
    RFSU = [23, 74, 405, 647]
    TTA = [42, 76, 507, 910]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, RFSU, width, label='RFSU')
    rects2 = ax.bar(x + width / 2, TTA, width, label='TTA')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('TT flow Ratio ' + r'$\alpha$', font)
    ax.set_ylabel('Jitter', font)
    # ax.set_title('The results of jitter for different ' + r'$\alpha$')
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-16.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart16():
    # 16.不同TT流比率与延迟流比率关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    labels = ['0.3', '0.4', '0.5', '0.6']
    RFSU = [0.11, 0.349, 0.38, 0.47]
    TTA = [0.14, 0.389, 0.518, 0.67]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, RFSU, width, label='RFSU')
    rects2 = ax.bar(x + width / 2, TTA, width, label='TTA')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('TT Flow Ratio ' + r'$\alpha$', font)
    ax.set_ylabel('Delay flow Ratio', font)
    # ax.set_title('The results of delay flow ratio for different ' + r'$\alpha$')
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

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig("./figures/figure5-17.pdf", bbox_inches='tight')
    plt.show()
    plt.close()
