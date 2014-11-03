from setuptools import setup, find_packages
import os

version = '0.4.2'

tests_require = [
    'collective.testcaselayer',
    'interlude',
    'Products.PloneTestCase',
]

setup(name='collective.mediaelementjs',
      version=version,
      description="A simple integration of the MediaElementJS video player for Plone.",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Framework :: Zope2",
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Multimedia :: Video :: Display",
          "Topic :: Multimedia :: Sound/Audio :: Players",
          "Topic :: Multimedia :: Sound/Audio :: Players :: MP3",
      ],
      keywords='plone html5 audio video mp3 wma mp4 webm ogg flv wmv mpeg quicktime',
      author='Tom Lazar, Unweb.me',
      author_email='tom@tomster.org, we@unweb.me',
      maintainer='Servilio Afre Puentes',
      maintainer_email='afrepues@mcmaster.ca',
      url='https://github.com/collective/collective.mediaelementjs',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'hachoir_core',
          'hachoir_metadata',
          'hachoir_parser',
          'Acquisition',
          'Products.Archetypes',
          'Products.ATContentTypes',
          'Products.CMFCore',
          'Products.GenericSetup >=1.6',
          'ZODB3',
          'Zope2',
          'plone.app.jquery',
          'plone.rfc822',
          'zope.annotation',
          'zope.cachedescriptors',
          'zope.component',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
