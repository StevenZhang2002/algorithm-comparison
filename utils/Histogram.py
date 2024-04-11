import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import entropy, chisquare, kstest


def generateHistogram(path, picture_status):
    print(picture_status)
    # Read image
    image = cv2.imread(path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Generate histogram
    hist, bins, _ = plt.hist(gray_image.ravel(), bins=256)

    # Normalize histogram to obtain probabilities

    probabilities = hist / np.sum(hist)
    print(probabilities)

    # Calculate entropy
    entropy_value = entropy(probabilities, base=2)
    print("Entropy:", entropy_value)

    # Perform Kolmogorov-Smirnov test
    ks_stat, p_value = kstest(np.cumsum(probabilities), 'uniform')
    print("Kolmogorov-Smirnov statistic:", ks_stat)
    print("p-value:", p_value)

    gini_coefficient = 1 - np.sum(probabilities ** 2)
    print("Gini Coefficient:", gini_coefficient)

    # Plot histogram
    plt.title(f'{picture_status} Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.savefig(f"histogramPic/{picture_status}'s Histogram")
    plt.show()
    print("______________________________________________________________________")

def generateHistogram2(path, picture_status):
    # read pic
    image = cv2.imread(path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    # Normalize histogram to obtain probabilities
    probabilities = hist.flatten() / np.sum(hist)
    print(f"probabilities is {probabilities}")
    print(picture_status)

    # Calculate entropy
    entropy_value = entropy(probabilities, base=2)
    print("Entropy:", entropy_value)


    # Perform Kolmogorov-Smirnov test
    ks_stat, p_value = kstest(np.cumsum(probabilities), 'uniform')
    print("Kolmogorov-Smirnov statistic:", ks_stat)
    print("p-value:", p_value)
    print("--------------------------------------------------------------------")
    plt.figure()
    plt.title(f'{picture_status} Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.savefig(f"histogramPic/{picture_status}'s Histogram")
    plt.show()

def generatehistIntegrate(origin_path,encrypted_image_path,status,output_path):
    # 原始图片
    img_original = cv2.imread(origin_path)
    # 转rgb用来展示
    img_original = cv2.cvtColor(img_original,cv2.COLOR_BGR2RGB)
    # 灰度图用来生成直方图
    gray_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    hist_original = cv2.calcHist([img_original], [0], None, [256], [0, 256])
    # 读取图片
    img = cv2.imread(encrypted_image_path)
    # 将图像转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist_encrypted = cv2.calcHist([gray], [0], None, [256], [0, 256])


    # 计算灰度图的直方图
    hist = cv2.calcHist([gray_original], [0], None, [256], [0, 256])

    # 绘制直方图
    # 1. 原图
    plt.figure(figsize=(20, 6))
    plt.subplot(1,4,1)
    plt.imshow(img_original)
    plt.title('Original Image')
    plt.axis('off')

    # 原图直方图
    plt.subplot(1,4,2)
    plt.hist(gray_original.ravel(), bins=256)
    plt.title(f'Original Grayscale Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')



    plt.subplot(1, 4, 3)
    plt.imshow(img, cmap='gray')
    plt.title('Encrypted Image')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.hist(gray.ravel(), bins=256)
    plt.title(f'{status} Grayscale Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')



    plt.savefig(f'{output_path}{status} histogram.png')
    plt.show()