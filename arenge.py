
import os
import shutil
os.chdir(r'C:\projecttt\run')

# os.chdir('..')
if os.path.exists('ProcessedDataset') == False:
   os.mkdir('ProcessedDataset')
os.chdir('ProcessedDataset')
dest_path = os.path.abspath(os.curdir)
os.chdir('../Dataset')

for a in sorted(os.listdir()):
    os.chdir(a)
    print(a)
    for b in sorted(os.listdir()):
        os.chdir(b)
        print("\t",b)
        for c in sorted(os.listdir()):
            os.chdir(c)
            print("\t\t",c)
            for d in sorted(os.listdir()):
                os.chdir(d)
                if os.path.exists(dest_path+'/'+b+c)==False:
                    os.mkdir(dest_path+'/'+b+c)
                print("\t\t\t",d)
                print('ExtractedLips',dest_path+'/'+b+c+'/'+a+d)
                # shutil.copytree('ExtractedLips',dest_path+'/'+b+c+'/'+a+d)
                shutil.copytree('ExtractedLips',os.path.join(dest_path, b+c,a+d))

                print("\t\t\t",d, " Done")
                os.chdir('../')
            print("\t\t",c, " Done")
            os.chdir('../')
        print("\t",b, " Done")
        os.chdir('../')
    print("\t\t\t",a, " Done")
    os.chdir('../')
os.chdir('../')



