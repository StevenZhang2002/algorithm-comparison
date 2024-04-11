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
    result = list()
    result.append(entropy_value)
    result.append(ks_stat)
    return result




def generateTable(Image_size):
    root_path = f'../output/{Image_size}/'
    aes_path = "$aes_img.jpg"
    blowfish_path = "$blowfish_img.jpg"
    des_path = "$des_img.jpg"
    des3_path = "$des3_img.jpg"
    rsa_path = "$rsa_img.jpg"
    rc4_path = "$RC4_img.jpg"

    t = Texttable()
    t.add_rows([
        ['Algorithm',"Image Size","Entropy", "Kolmogorov-Smirnov test"],
        ["Original",Image_size,calculateUniformity(f"../input/{Image_size}/5.3.01.tiff")[0],calculateUniformity(f"../input/{Image_size}/5.3.01.tiff")[1]],
        ['DES',  Image_size, calculateUniformity(root_path+des_path)[0],calculateUniformity(root_path+des_path)[1]],
        ['3DES',  Image_size, calculateUniformity(root_path+des3_path)[0],calculateUniformity(root_path+des3_path)[1]],
        ['AES', Image_size, calculateUniformity(root_path+aes_path)[0],calculateUniformity(root_path+aes_path)[1]],
        ['Blowfish',  Image_size, calculateUniformity(root_path+blowfish_path)[0],calculateUniformity(root_path+blowfish_path)[1]],
        ['RC4',  Image_size, calculateUniformity(root_path+rc4_path)[0],calculateUniformity(root_path+rc4_path)[1]],
        ['RSA',  Image_size, calculateUniformity(root_path+rsa_path)[0],calculateUniformity(root_path+rsa_path)[1]]
        ]
    )
    print(t.draw())

    f = open(f"../output/{Image_size}/Algorithm_table_uniformity.txt", "w")
    f.write(t.draw())
    f.close()

if __name__ == '__main__':
    generateTable('1024')
