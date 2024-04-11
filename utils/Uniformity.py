import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import entropy, kstest
from texttable import Texttable

def calculateUniformity(encrypted_path):
    # Read image
    image = cv2.imread(encrypted_path)
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
    return entropy,ks_stat




def generateTable(Image_size):
    root_path = 'output/256/'
    aes_path = "$aes_img.jpg"
    blowfish_path = "$blowfish_img.jpg"
    des_path = "$des_img.jpg"
    des3_path = "$des3_img.jpg"
    rsa_path = "$rsa_img.jpg"
    rc4_path = "$RC4_img.jpg"

    t = Texttable()
    t.add_rows([
        ['Algorithm',"Image Size","Entropy", "Kolmogorov-Smirnov test"],
        ["Original",Image_size,calculateUniformity("input/256/4.1.03.tiff")],
        ['DES',  Image_size, calculateUniformity(root_path+des_path)],
        ['3DES',  Image_size, calculateUniformity(root_path+des3_path)],
        ['AES', Image_size, calculateUniformity(root_path+aes_path)],
        ['Blowfish',  Image_size, calculateUniformity(root_path+blowfish_path)],
        ['RC4',  Image_size, calculateUniformity(root_path+rc4_path)],
        ['RSA',  Image_size, calculateUniformity(root_path+rsa_path)]]
    )
    print(t.draw())

    f = open("output/256/Algorithm_table_uniformity.txt", "w")
    f.write(t.draw())
    f.close()
