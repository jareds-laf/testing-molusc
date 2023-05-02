try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup

config = {
	'description': 'MOLUSC',
	'author': 'Jared Sofair',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'sofairj@lafayette.edu',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': [find_packages()],
	'scripts': [],
	'name': 'MOLUSC'
}

setup(**config)
