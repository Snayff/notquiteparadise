from setuptools import setup

setup(
    name='NotQuiteParadise',
    version='0.96.0',
    packages=['scripts', 'scripts.core', 'scripts.world_objects', 'scripts.world_objects.terrain', 'scripts.entity', 'scripts.events',
        'scripts.skills', 'scripts.skills.effects', 'scripts.managers', 'scripts.managers.ui_manager',
        'scripts.managers.world_manager', 'scripts.components', 'scripts.ui_elements', 'scripts.ui_elements.templates',
        'scripts.event_handlers', 'scripts.global_singletons'],
    url='',
    license='',
    author='Snayff',
    author_email='',
    description='', install_requires=['pygame', 'esper', 'tcod', 'scipy', 'pytweening']
)
