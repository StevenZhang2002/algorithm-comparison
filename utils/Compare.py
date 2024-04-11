import matplotlib.pyplot as plt

import numpy as np

if __name__ == "__main__":
    #KS
    # 定义标签和数值
    labels = ['DES', '3DES', 'AES', 'Blowfish', 'RC4', 'RSA']
    values = [[0.007, 0.006, 0.006, 0.005, 0.009, 0.020],
              [0.006, 0.005, 0.007, 0.006, 0.006, 0.019],
              [0.005, 0.006, 0.005, 0.006, 0.007, 0.018]]

    # 创建图形
    x = np.arange(len(labels))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width, values[0], width, label='256')
    rects2 = ax.bar(x, values[1], width, label='512')
    rects3 = ax.bar(x + width, values[2], width, label='1024')

    # 添加标签和标题
    # ax.set_ylim(0, 0.5)
    ax.set_xlabel('Algorithm')
    ax.set_ylabel('KS Value')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    plt.savefig('Com_Kolmogorov-Smirnov.png', dpi=300)
    plt.show()


    #Entropy
    # 定义标签和数值
    labels = ['Original','DES', '3DES', 'AES', 'Blowfish', 'RC4', 'RSA']
    values = [[5.594,7.997, 7.996, 7.996, 7.996 , 7.996, 7.997],
              [6.695,7.998, 7.998, 7.998, 7.998, 7.998, 7.998],
              [7.524,7.999, 7.999, 7.999, 7.999, 7.999, 7.998]]

    # 创建图形
    x = np.arange(len(labels))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width, values[0], width, label='256')
    rects2 = ax.bar(x, values[1], width, label='512')
    rects3 = ax.bar(x + width, values[2], width, label='1024')

    # 添加标签和标题
    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Entropy')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.savefig('Com_Entropy.png', dpi=300)
    plt.show()

    #Time
    # 定义标签和数值
    labels = ['DES', '3DES', 'AES', 'Blowfish', 'RC4', 'RSA']
    values = [[0.002, 0.003, 0.001, 0.001, 0.001, 0.032],
              [0.003, 0.006, 0.001, 0.002, 0.001, 0.174],
              [0.013, 0.029, 0.003, 0.009, 0.004, 13.344]]

    # 创建图形
    x = np.arange(len(labels))
    width = 0.25


    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width, values[0], width, label='256')
    rects2 = ax.bar(x, values[1], width, label='512')
    rects3 = ax.bar(x + width, values[2], width, label='1024')

    # 添加标签和标题
    ax.set_ylim(0, 0.03)
    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Time taken')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.savefig('Com_Time.png', dpi=300)
    plt.show()

    # Memory Usage
    # 定义标签和数值
    labels = ['DES', '3DES', 'AES', 'Blowfish', 'RC4', 'RSA']
    values = [[24, 24, 0, 0, 0, 296],
              [536, 24, 0, 512, 248, 292],
              [1052, 1052, 1028, 1028, 1028, 2060]]

    # 创建图形
    x = np.arange(len(labels))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width, values[0], width, label='256')
    rects2 = ax.bar(x, values[1], width, label='512')
    rects3 = ax.bar(x + width, values[2], width, label='1024')

    # 添加标签和标题

    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Memory Usage')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.savefig('Com_Memory-Usage.png', dpi=300)
    plt.show()