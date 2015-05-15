from distutils.core import setup

setup(name='maluku',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Data about Maluku',
      url='https://thomaslevine.com/',
      packages=['vocopvarenden'],
      entry_points = {'console_scripts': ['vocopvarenden = vocopvarenden:main']},
      version='0.1',
      license='AGPL',
)
