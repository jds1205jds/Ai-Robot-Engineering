from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtle_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('turtle_project/*.ui')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jungdaeseok',
    maintainer_email='jungdaeseok@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = turtle_project.main:main',
            'patrol_server = turtle_project.patrol_server:main',
        ],
    },
)
