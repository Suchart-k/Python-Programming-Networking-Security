import os

if not os.path.exists('my_dir'):
    try:
        os.makedirs('my_dir')
    except OSError as e:
        print(e)


