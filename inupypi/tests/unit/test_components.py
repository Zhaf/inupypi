from fixture import TempIO
from unittest import TestCase
from inupypi.settings import PACKAGE_PATH
from inupypi.components.packages import Packages
import os

class TestComponents(TestCase):

    """Testing Components Functionality"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_package_directory(self):

        '''Verify that get_folders work correctly'''

        package_dir = PACKAGE_PATH = TempIO() + '/packages'
        os.makedirs(package_dir)
        os.makedirs(package_dir+'/package_one')
        open(package_dir+'/package_incorrect.txt','w').close()
        packages = Packages()
        packages.package_dir = package_dir
        folders = packages.get_folders()

        for folder in folders:
            assert folder.name == 'package_one'
        folders = packages.get_folders()
        assert len(folders) == 1, "package_incorrect.txt should not be listed"






