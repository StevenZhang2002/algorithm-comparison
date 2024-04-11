
import cv2
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
        self.MB_CONVERT = 1048576
        self.KB_CONVERT = 1024
        self.targetImg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        np.savetxt("output/Targettxt.txt",self.targetImg)

    def main(self):

        
        aes_enc = algAES()
        des_enc = algDES()
        des3_enc = algDES3()
        rsa_enc = algRSA()
        blowfish_enc = algBlowfish()
        rc4_enc = algRC4()

        ## blowfish
        blowfish_encryption_t = blowfish_enc.encrypt(self.targetImg)

        ## DES, output image in file and return encryption time.
        des_encryption_t = des_enc.encrypt(self.targetImg)

        ## DES3, output image in file and return encryption time.
        des3_encryption_t = des3_enc.encrypt(self.targetImg)


        ## AES, output image in file and return encryption time.
        aes_encryption_t = aes_enc.encrypt(self.targetImg)
        
        ## RSA, output image in file and return encryption time.
        rsa_encryption_t = rsa_enc.encrypt(self.targetImg)
        RC4_encryption_t = rc4_enc.encrypt(self.targetImg)





        #  TargetText Table

        t = Texttable()
        t.add_rows([
            ['Algorithm', "Key Size(bits)", "Time taken in nanosecs","Memory Usage(MB)"],
            ['DES', 56,des_encryption_t[0],str(des_encryption_t[1]/self.MB_CONVERT)+"MB"],
            ['3DES', 168,des3_encryption_t[0],str(des3_encryption_t[1]/self.MB_CONVERT)+"MB"],
            ['AES', 256,aes_encryption_t[0],str(aes_encryption_t[1]/self.MB_CONVERT)+"MB"],
            ['Blowfish',56, blowfish_encryption_t[0],str(blowfish_encryption_t[1]/self.MB_CONVERT)+"MB"],
            ['RC4', 256, RC4_encryption_t[0], str(RC4_encryption_t[1] / self.MB_CONVERT) + "MB"],
            ['RSA', 128,rsa_encryption_t[0],str(rsa_encryption_t[1] / self.KB_CONVERT) + "MB"]]
        )
        print(t.draw())

        f = open("output/Algorithm_table.txt","w")
        f.write(t.draw())
        f.close()

# running main
if __name__ == "__main__":
    test1 = Test("input/256/4.1.03.tiff")
    test1.main()
    Histogram.generateHistogram("test3.jpeg","Original")
    Histogram.generateHistogram("output/$aes_img.jpg","AES CBC MODE")
    Histogram.generateHistogram("output/$DES_img.jpg", "DES CBC MODE")
    Histogram.generateHistogram("output/$des3_img.jpg", "DES3 CBC MODE")
    Histogram.generateHistogram("output/$blowfish_img.jpg", "Blowfish CBC MODE")
    Histogram.generatehistIntegrate("input/usc.tiff","output/$RC4_img.jpg","RC4","output/1024")


    
