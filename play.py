import sys
sys.argv = ['drive.py', 'model-005.h5']  # argv[0] should still be the script name
exec(open('drive.py').read())
