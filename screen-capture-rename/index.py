import os
import sys
import subprocess

# run capture command
fileName = input('> Please input filename: ')
if fileName:
    cmd = ['defaults', 'write', 'com.apple.screencapture', 'name', fileName]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('Rename screen capture')
else:
    print('Good bye')
    sys.exit()

# use date
useDate = input('> Using dates in filename (Y/n): ')
useDate = 'FALSE' if useDate.lower() == 'n' else 'TRUE'
if useDate:
    cmd = ['defaults', 'write', 'com.apple.screencapture', 'include-date', '-bool', useDate]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('Update useDate')

# use shadow
useShadow = input('> Using shadow window (Y/n): ')
useShadow = 'TRUE' if useShadow.lower() == 'n' else 'FALSE'
if useShadow:
    cmd = ['defaults', 'write', 'com.apple.screencapture', 'disable-shadow', '-bool', useShadow]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('Update useShadow')

# update system
os.system('killall SystemUIServer')

# end message
print('Good bye')
