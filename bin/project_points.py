__author__ = 'Andrew A Campbell'

import ConfigParser
import os
import sys
import time

try:
    from qgis.core import QgsProject
    from qgis.gui import *
    from PyQt4.QtCore import Qt
    from PyQt4.QtCore import QFileInfo
except ImportError:
    print "Cannot find the QGIS dependencies. Make sure you are using the correct virtualenv."
    print "Also, refer to the batch script at the following link for configuring environmental variables."
    print "http://gis.stackexchange.com/questions/144908/can-we-avoid-using-sip-library-when-writing-standalone-qgis-python-script"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'erROOAAARRRR!!! need to pass the path to the config file.'
        exit()

    # Read the config file and load the project and layer variables
    config_path = sys.argv[1]
    conf = ConfigParser.ConfigParser()
    conf.read(config_path)
    project_path = conf.get('Paths', 'project')
    project = QgsProject.instance().read(QFileInfo(project_path))
    lines = conf.get('Layers', 'lines')
    start_nodes = conf.get('Layers', 'start_nodes')
    end_nodes = conf.get('Layers', 'end_nodes')