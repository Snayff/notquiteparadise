from setuptools import setup

setup(
    name='NotQuiteParadise',
    version='0.0.1',
    packages=['scripts', 'scripts.core', 'scripts.world', 'scripts.world.terrain', 'scripts.entity', 'scripts.events',
        'scripts.skills', 'scripts.skills.effects', 'scripts.managers', 'scripts.managers.ui_methods',
        'scripts.managers.world_methods', 'scripts.components', 'scripts.ui_elements', 'scripts.ui_elements.templates',
        'scripts.event_handlers', 'scripts.global_singletons'],
    url='',
    license='',
    author='Gabriel',
    author_email='',
    description='', install_requires=['pygame', 'esper', 'tcod', 'scipy']
)
