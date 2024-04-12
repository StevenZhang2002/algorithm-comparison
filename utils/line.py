import matplotlib.pyplot as plt



# 定义x轴标签和数据
x_labels = ['256', '512', '1024']
x = [256, 512, 1024]

# 定义各折线的数据
aes_data = [7.996, 7.999, 7.999]
rsa_data = [7.997, 7.998, 7.998]
des3_data = [7.996, 7.997, 7.999]
rc4_data = [7.996, 7.998, 7.999]

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制折线图
ax.plot(x, aes_data, linestyle='--', label='AES', marker='o', markersize=5)
ax.plot(x, rsa_data, linestyle='--', label='RSA', marker='o', markersize=5)
ax.plot(x, des3_data, linestyle='--', label='DES3', marker='o', markersize=5)
ax.plot(x, rc4_data, linestyle='--', label='RC4', marker='o', markersize=5)


# 添加标签和标题
ax.set_xlabel('Image Size')
ax.set_ylabel('Entropy Value')
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()


# 保存图片
plt.savefig('line_chart_Entropy.png', dpi=300)
plt.show()












# 定义x轴标签和数据
x_labels = ['256', '512', '1024']
x = [256, 512, 1024]

# 定义各折线的数据
aes_data = [0.006, 0.008, 0.005]
rsa_data = [0.020, 0.019, 0.018]
des3_data = [0.006, 0.005, 0.006]
rc4_data = [0.009, 0.006, 0.006]

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制折线图
ax.plot(x, aes_data, linestyle='--', label='AES', marker='o', markersize=5)
ax.plot(x, rsa_data, linestyle='--', label='RSA', marker='o', markersize=5)
ax.plot(x, des3_data, linestyle='--', label='DES3', marker='o', markersize=5)
ax.plot(x, rc4_data, linestyle='--', label='RC4', marker='o', markersize=5)


# 添加标签和标题
ax.set_xlabel('Image Size')
ax.set_ylabel('KS Value')
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()


# 保存图片
plt.savefig('line_chart_KS.png', dpi=300)
plt.show()
















# 定义x轴标签和数据
x_labels = ['256', '512', '1024']
x = [256, 512, 1024]

# 定义各折线的数据
aes_data = [0.000, 0.000, 0.003]
rsa_data = [0.032, 0.174, 13.344]
des3_data = [0.002, 0.006, 0.029]
rc4_data = [0.000, 0.001, 0.004]

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制折线图
ax.plot(x, aes_data, linestyle='--', label='AES', marker='o', markersize=5)
ax.plot(x, rsa_data, linestyle='--', label='RSA', marker='o', markersize=5)
ax.plot(x, des3_data, linestyle='--', label='DES3', marker='o', markersize=5)
ax.plot(x, rc4_data, linestyle='--', label='RC4', marker='o', markersize=5)


# 添加标签和标题
ax.set_xlabel('Image Size')
ax.set_ylabel('Time taken(S)')
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()


# 保存图片
plt.savefig('line_chart_Time.png', dpi=300)
plt.show()














# 定义x轴标签和数据
x_labels = ['256', '512', '1024']
x = [256, 512, 1024]

# 定义各折线的数据
aes_data = [0.0, 0.0, 1028.0]
rsa_data = [296.0, 292.0, 2060.0]
des3_data = [24.0, 24.0, 1052.0]
rc4_data = [0.0, 248.0, 1028.0]

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制折线图
ax.plot(x, aes_data, linestyle='--', label='AES', marker='o', markersize=5)
ax.plot(x, rsa_data, linestyle='--', label='RSA', marker='o', markersize=5)
ax.plot(x, des3_data, linestyle='--', label='DES3', marker='o', markersize=5)
ax.plot(x, rc4_data, linestyle='--', label='RC4', marker='o', markersize=5)


# 添加标签和标题
ax.set_xlabel('Image Size')
ax.set_ylabel('Memory Usage(KB)')
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()


# 保存图片
plt.savefig('line_chart_Memory.png', dpi=300)
plt.show()


















