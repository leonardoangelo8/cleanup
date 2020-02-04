from cleanup.clean import (median, adaptative, otsu, edges)
import os
import glob
import cv2 as cv

in_dir = '/home/leo/Downloads/candidate-data/01-DocumentCleanup/noisy_data'


def process_imgs():
    '''
    This function applies the selected filter
    '''
    imgs = glob.glob(os.path.join(in_dir, '*.png'))
    processed = median(imgs)

    for img1, img2 in zip(imgs, processed):
        cv.imwrite(img1.replace('/noisy_data', '/processed'), img2)


def main():
    process_imgs()


if __name__ == "__main__":
    main()
