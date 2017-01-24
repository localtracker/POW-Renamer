#!/usr/bin/env python
from os import rename, listdir, remove
import shutil
import glob

print(' ____   __   _  _    ____  ____  __ _   __   _  _  ____  ____ ')
print('(  _ \ /  \ / )( \  (  _ \(  __)(  ( \ / _\ ( \/ )(  __)(  _  )')
print(' ) __/(  O )\ /\ /   )   / ) _) /    //    \/ \/ \ ) _)  )   /')
print('(__)   \__/ (_/\_)  (__\_)(____)\_)__)\_/\_/\_)(_/(____)(__\_)')
print(' v1.0 // Sid')


ep = input('\nWhats the Episode Number? ')

monomix = 'Mono Mix'
monomne = 'Mono M&E'
monodia = 'Mono Dia'
dolbymix = 'DMIX'
dolbymne = 'DME'

count = 0

fnames = listdir('.')

for fname in fnames:
    if fname.startswith(monomix):
        rename(fname, '01POW EP#'+str(ep)+' MONO MIX.wav')
        shutil.copy2('/Users/Sid/Desktop/Renamer/01POW EP#'+str(ep)+' MONO MIX.wav','/Users/Sid/Desktop/Renamer/enc/02POW EP#'+str(ep)+' MONO MIX.wav')
        shutil.copy2('/Users/Sid/Desktop/Renamer/enc/02POW EP#'+str(ep)+' MONO MIX.wav','/Users/Sid/Desktop/Renamer/02POW EP#'+str(ep)+' MONO MIX.wav')
        count = count + 1
        print('\nMono Mix Created....')
    elif fname.startswith(monomne):
        rename(fname, '08POW EP#'+str(ep)+' MONO M&E.wav')
        count = count + 1
        print('\nMono M&E Created....')
    elif fname.startswith(monodia):
        rename(fname, '07POW EP#'+str(ep)+' MONO DIAL.wav')
        count = count + 1
        print('\nMono Dia Created....')
    elif fname.startswith(dolbymix):
        rename(fname, '03POW EP#'+str(ep)+' DOLBY FULL MIX.wav')
        shutil.copy2('/Users/Sid/Desktop/Renamer/03POW EP#'+str(ep)+' DOLBY FULL MIX.wav','/Users/Sid/Desktop/Renamer/enc/04POW EP#'+str(ep)+' DOLBY FULL MIX.wav')
        shutil.copy2('/Users/Sid/Desktop/Renamer/enc/04POW EP#'+str(ep)+' DOLBY FULL MIX.wav','/Users/Sid/Desktop/Renamer/04POW EP#'+str(ep)+' DOLBY FULL MIX.wav')
        count = count + 1
        print('\nDolby Mix Created....')
    elif fname.startswith(dolbymne):
        rename(fname, '05POW EP#'+str(ep)+' DOLBY M&E.wav')
        shutil.copy2('/Users/Sid/Desktop/Renamer/05POW EP#'+str(ep)+' DOLBY M&E.wav','/Users/Sid/Desktop/Renamer/enc/06POW EP#'+str(ep)+' DOLBY M&E.wav')
        shutil.copy2('/Users/Sid/Desktop/Renamer/enc/06POW EP#'+str(ep)+' DOLBY M&E.wav','/Users/Sid/Desktop/Renamer/06POW EP#'+str(ep)+' DOLBY M&E.wav')
        count = count + 1
        print('\nDolby M&E Created....')
        
if count == 5:
    print('\nAll done successfully!')
    dup = glob.glob('/Users/Sid/Desktop/Renamer/enc/*.wav')
    for duplicates in dup:
        remove(duplicates)
else:
    print('\nSomething went wrong!')
        

