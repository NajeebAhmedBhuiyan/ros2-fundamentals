from setuptools import find_packages, setup

package_name = 'py_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='najeeb',
    maintainer_email='nabq2000@gmail.com',
    description='Nodes Tutorial',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'py_publisher = py_nodes.publisher:main',
            'py_subscriber = py_nodes.subscriber:main',
            'py_service_server = py_nodes.service_server:main',
            'py_service_client = py_nodes.service_client:main'
        ],
    },
)
