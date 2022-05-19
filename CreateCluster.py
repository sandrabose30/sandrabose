import os
import numpy as np
import cv2
import sys
os.chdir(r'C:\projecttt\run')
if os.path.exists('ClusteredDataset') == False:
    os.mkdir('ClusteredDataset')
os.chdir('ClusteredDataset')
dest_path = os.path.abspath(os.curdir)
print(dest_path)
os.chdir(r'C:\projecttt\run\Dataset')
np.set_printoptions(threshold=sys.maxsize)


for f in sorted(os.listdir()):
    # print(os.listdir())
    os.chdir(f)
    print(f)
    for l in sorted(os.listdir()):
        os.chdir(l)
        print('\t',l)
        for w in sorted(os.listdir()):
            os.chdir(w)
            print('\t\t',w)
            for p in sorted(os.listdir()):
                # print('\t\t\t',p)
                # print(dest_path+'/'+l+w)
                if os.path.exists(dest_path+'/'+l+w)==False:
                    os.mkdir(dest_path+'/'+l+w)
                os.chdir(p)
                os.chdir('ExtractedLips')
                seq = np.zeros((224,224))
                orig = len(os.listdir())
                orig_image = []
                for i in sorted(os.listdir()):
                    
                    img = cv2.imread(i, 0)
                    img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_LINEAR)
                    orig_image.append(img)
                x_limit = 32
                y_limit = 32
                iterator_x = 0
                iterator_y = 0
                for i in range(0, 49):
                    # cv2.imshow("test", orig_image)
                    # cv2.waitKey(0)
                    # print((orig))
                    # print("value ",int((i * orig) / 49))
                    seq[iterator_y:iterator_y + y_limit, iterator_x:iterator_x + x_limit] = orig_image[int((i * orig) / 49)]  # movement along y-axis

                    iterator_x = iterator_x + x_limit
                    # print(iterator_x())
                    if iterator_x == 224:
                        iterator_x = 0
                        iterator_y = iterator_y + y_limit
                name = dest_path + '/' + l + w + '/' + f + '_' + p + '.jpg'
                print("name of.......",name)
                cv2.imwrite(name, seq)
                os.chdir('..')
                print('\t\t\t', p, ' Done')
                os.chdir('..')
            print('\t\t', w, ' Done')
            os.chdir('..')
        print('\t', l, ' Done')
        os.chdir('..')
    print(f, ' all Done.........')
    os.chdir('..')