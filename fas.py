from tsn_predict import TSNPredictor as CelebASpoofDetector
import time
import sys
import logging
import cv2


import numpy as np

logging.basicConfig(level=logging.INFO)


def run_test(detector, image):
    """
    In this function we create the detector instance. And evaluate the wall time for performing CelebASpoofDetector.
    """

    # # initialize the detector
    # logging.info("Initializing detector.")
    # try:
    #     detector = CelebASpoofDetector()
    # except:
    #     # send errors to the eval frontend
    #     raise
    # logging.info("Detector initialized.")

    # run the images one-by-one and get runtime

    logging.info("Starting runtime evaluation")
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    prob = detector.predict(img)
    temp = float(prob[0][1])

    print("NaXXXXXXXXXXXx")
    print(temp)
    return temp

    logging.info("""
    ================================================================================
    All images finished, showing verification info below:
    ================================================================================
    """)


# if __name__ == '__main__':
#     # print(type(next(celebA_spoof_image_iter)))
#     run_test()
