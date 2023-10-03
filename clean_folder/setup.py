from setuptools import setup

setup(name='clean_folder',
      version='1.0.1',
      description='Clean folder',
      url='https://github.com/lotuskolobok/HomeWork6/tree/main/clean_folder',
      author='Kolobok',
      author_email='kolobok@example.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['cleanfolder = clean_folder.clean:main']}
      )