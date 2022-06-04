import os
#change to projectfolderpath/Dataset
src_path = r"C:\Users\Aswin\Downloads\sandrabose-new\sandrabose-new\Dataset"
os.chdir(src_path)
#print(os.listdir())
for a in (os.listdir()):
    os.chdir(a)
    print("Processing", a)
    for b in (os.listdir()):
        os.chdir(b)
        #print(os.listdir())
        for c in (os.listdir()):
            os.chdir(c)
            #print(os.listdir())
            for d in (os.listdir()):
                os.chdir(d)
                #print(os.listdir())
                if os.path.exists('face') == False:
                    os.mkdir('face')
                for e in (os.listdir()):
                    if(e=="face"):
                        continue
                    filepath=src_path+'/'+a+'/'+b+'/'+c+'/'+d+'/'+e
                    newfilepath = src_path+'/'+a+'/'+b+'/'+c+'/'+d
                    os.replace(filepath,os.path.join(newfilepath,'face',e))
                print(a,"Done")
                os.chdir(src_path+'/'+a+'/'+b+'/'+c)
            os.chdir(src_path+'/'+a+'/'+b)
        os.chdir(src_path+'/'+a)
    os.chdir(src_path)