import unittest
import doctest

from Testing import ZopeTestCase
from Products.PloneTestCase import ptc
from collective.testcaselayer import ptc as tcl_ptc
from Products.Five import zcml

from interlude import interact

optionflags = (doctest.NORMALIZE_WHITESPACE |
               doctest.ELLIPSIS |
               doctest.REPORT_NDIFF)

ptc.setupPloneSite()


class Layer(tcl_ptc.BasePTCLayer):
    """Install collective.mediaelementjs"""
    def afterSetUp(self):
        import collective.mediaelementjs
        zcml.load_config('configure.zcml', collective.mediaelementjs)
        self.addProfile('collective.mediaelementjs:default')
        # put resource registry to debug mode to avoid cachekyes in tests
        self.portal.portal_css.setDebugMode(True)
        self.portal.portal_javascripts.setDebugMode(True)


layer = Layer([tcl_ptc.ptc_layer])


FUNCTIONALTESTFILES = [
    'README.txt',
]
TESTFILES = [
    '../metadata_extraction.txt',
]


def test_suite():
    test_class = ptc.FunctionalTestCase
    test_class.layer = layer

    return unittest.TestSuite(
        [ZopeTestCase.FunctionalDocFileSuite(
            file,
            package='collective.mediaelementjs',
            optionflags=optionflags,
            globs={'interact': interact},
            test_class=test_class
        ) for file in FUNCTIONALTESTFILES] + [doctest.DocFileSuite(
            file,
            optionflags=optionflags,
            globs={'interact': interact},
        ) for file in TESTFILES]
    )


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
