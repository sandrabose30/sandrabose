import os
import shutil
os.chdir(r'C:\projecttt\run')
# os.chdir('...')
if os.path.exists('SplitClusteredDataset') == False:
	os.mkdir('SplitClusteredDataset')
os.chdir('SplitClusteredDataset')
if os.path.exists('Train') == False:
	os.mkdir('Train')
if os.path.exists('Validation') == False:
	os.mkdir('Validation')
if os.path.exists('Test') == False:
	os.mkdir('Test')
dest_path = os.path.abspath(os.curdir)
os.chdir('../ClusteredDataset')

for a in sorted(os.listdir()):
	os.chdir(a)
	print(a)
	for x, i in enumerate(sorted(os.listdir())):
		if (x % 14 < 10):
			dest_folder = 'Train'
		elif (x % 14 < 12):
			dest_folder = 'Validation'
		else:
			dest_folder = 'Test'
		if os.path.exists(dest_path + '/' + dest_folder + '/' + a) == False:
			os.mkdir(dest_path + '/' + dest_folder + '/' + a)
		shutil.copy(i, dest_path + '/' + dest_folder + '/' + a + '/' + i)
		print("\t", i, " Done")
	print(a, " Done")
	os.chdir('..')
