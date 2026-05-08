from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='omi',
    maintainer_email='omi@todo.todo',
    description='ROS2 action client and server package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'count_until_server = my_py_pkg.count_until_server:main',
            'count_until_client = my_py_pkg.count_until_client:main',
        ],
    },
)
