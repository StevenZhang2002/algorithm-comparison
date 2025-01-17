import cv2
import numpy as np
import time

import psutil
import rsa

class algRSA:
    def __init__(self):
        (self.private_key,self.public_key) = rsa.newkeys(256)

    """
    RSA can only encrypt messages that are smaller than the key.
    Out of 256bit it take 11bytes for PKCS padding and header data
    For our use case it given 128bit(16bytes)
    """

    def encrypt(self, img):
        chunk_size = 16
        byteImg = img.tobytes()

        ## Encrypting

        st_time = time.clock()

        encBytes = b''

        before_memory = psutil.Process().memory_info().rss

        for i in range(0,len(byteImg), chunk_size):

            if(i+chunk_size > len(byteImg)):
                encBytes = encBytes + rsa.encrypt(byteImg[i:],self.public_key)
            else:
                encBytes = encBytes + rsa.encrypt(byteImg[i:i+chunk_size],self.public_key)
        after_memory = psutil.Process().memory_info().rss
        
        enc_t = time.clock() - st_time
        
        ## Droping extra bytes, converting back to img
        
        shape = list(img.shape)
        shape[0] = -1
        encImg = np.frombuffer(encBytes, dtype=img.dtype).reshape(shape)
        

        np.savetxt("output/1024/$rsa_ciphertxt.txt",encImg)
        cv2.imwrite("output/1024/$rsa_img.jpg", encImg)

        result = list()
        result.append(enc_t)
        result.append(after_memory - before_memory)

        return result