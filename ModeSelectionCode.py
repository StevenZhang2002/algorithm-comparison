import cv2
from matplotlib import pyplot as plt
from texttable import Texttable

import numpy as np

from RC4 import algRC4
from aes import algAES
from des import algDES
from des3 import algDES3
from rsa_256 import algRSA
from blowfish import algBlowfish
from utils import Histogram


class Test:

    def __init__(self, path):
        self.targetImg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        np.savetxt("output/Targettxt.txt", self.targetImg)

    def main(self):
        aes_enc = algAES()
        des_enc = algDES()
        des3_enc = algDES3()
        blowfish_enc = algBlowfish()

        ## blowfish
        blowfish_encryption_t = blowfish_enc.encrypt(self.targetImg)

        ## DES, output image in file and return encryption time.
        des_encryption_t = des_enc.encrypt(self.targetImg)

        ## DES3, output image in file and return encryption time.
        des3_encryption_t = des3_enc.encrypt(self.targetImg)

        ## AES, output image in file and return encryption time.
        aes_encryption_t = aes_enc.encrypt(self.targetImg)




def showPic(alg,rawImagePath,mode_1_hist,mode_2_hist):
    # 原始图片
    img_original = cv2.imread(rawImagePath)
    img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
    # ECB
    hist_1 = cv2.imread(mode_1_hist)
    hist_1 = cv2.cvtColor(hist_1, cv2.COLOR_BGR2RGB)
    # CBC
    hist_2 = cv2.imread(mode_2_hist)
    hist_2 = cv2.cvtColor(hist_2, cv2.COLOR_BGR2RGB)

    # 绘制直方图
    plt.figure(figsize=(20, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(img_original)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(hist_1)
    plt.title(F'{alg} ECB encrypted Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(hist_2)
    plt.title(F'{alg} CBC encrypted Image')
    plt.axis('off')


    plt.savefig(f'{alg} mode comparison.png')
    plt.show()


# running main
if __name__ == "__main__":
    test1 = Test("test3.jpeg")
    test1.main()




