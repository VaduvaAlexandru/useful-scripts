#!/usr/bin/python
import sys
from simpleodspy.sodsspreadsheet import SodsSpreadSheet
from simpleodspy.sodsxml import SodsXml
from simpleodspy.sodsods import SodsOds

# Parse the command line arguments.
if len(sys.argv) != 2:
    helpText = "Usage: " + str(sys.argv[0]) + " <filename>"
    print helpText
    sys.exit()

# Open the XLS file as a "workbook", I will get tag names from the sheet's first row contents.
filename = str(sys.argv[1]) + ".ods"

t = SodsSpreadSheet()
tw = SodsOds(t)
tw.load(filename)
tw = SodsXml(t)
tw.save("test.xml")
