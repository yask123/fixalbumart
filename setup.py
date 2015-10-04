from setuptools import setup

setup(name='fixalbumart',
      version='1.0',
      description='Automagically fix album arts of mp3 files, Even with incorrect tags!!!',
      url='https://github.com/yask123/AlbumArt-Grabber',
      author='Yask Srivastava',
      author_email='yask123@gmail.com',
      license='MIT',
      packages=['fixalbumart'],
      scripts=['bin/fixalbumart'],
      install_requires=[
          'eyed3',
      ],
      zip_safe=False)