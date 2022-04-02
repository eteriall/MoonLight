"""UI Conversion"""
import glob
import os

os.chdir(os.environ.get('UI_PATH'))
filenames = glob.glob('*.ui', recursive=True)

for f in filenames:
    os.system(f'pyuic5 {f} > ../_py/{f[:-3]}.py ')
os.chdir(os.environ.get('PWD'))
