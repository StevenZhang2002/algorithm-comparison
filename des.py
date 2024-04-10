import cv2
import numpy as np
import time

import psutil
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import Blowfish
from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes




class algDES:

    def __init__(self,MODE=2):
        ## Key from random bytes
        key  = get_random_bytes(8)
        if MODE==1:
            self.cipher = DES.new(key, DES.MODE_ECB)
        else:
            self.cipher = DES.new(key, DES.MODE_CBC)

    def encrypt(self, img):
        """
         encrypt img, save encrypted image as aes_img.jpg
         returns encryption_time 
        """

        byteImg = img.tobytes()
        ## Padding
        PadbyteImg = pad(byteImg, 8)

        ## Encrypting bytes

        st_time = time.time_ns()
        before_memory = psutil.Process().memory_info().rss
        encBytes = self.cipher.encrypt(PadbyteImg)
        after_memory = psutil.Process().memory_info().rss
        enc_time = time.time_ns() - st_time

        # Convert ciphertext bytes to encrypted image data
        encBytes = encBytes[:len(byteImg)]
        encImg = np.frombuffer(encBytes, dtype=img.dtype).reshape(img.shape)

        np.savetxt("output/$des_ciphertxt.txt", encImg)
        cv2.imwrite("output/ModeSelection/$des_img.jpg", encImg)

        result = list()
        result.append(enc_time)
        result.append(after_memory - before_memory)

        return result


