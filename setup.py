from setuptools import setup

setup(name='port-scanner',
	version='1.0',
	description='Port Scanner',
	url='https://github.com/stirk1337/Port-scanner',
	author='stirk',
	author_email='stirk-delovoy@mail.ru',
	license='MIT',
	packages=['port-scanner', 'port-scanner/src'],
	install_requires=['aiohttp==3.8.1'],
	include_package_data=True,
	)