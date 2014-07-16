#!/usr/bin/python
import sys
import xlrd

# Parse the command line arguments.
if len(sys.argv) != 2:
    helpText = "Usage: " + str(sys.argv[0]) + " <filename>"
    print helpText
    sys.exit()

# Open the XLS file as a "workbook", I will get tag names from the sheet's first row contents.
filename = str(sys.argv[1]) + ".xls"
wb = xlrd.open_workbook(filename)
for i in range(wb.nsheets):
    name = str(sys.argv[1]) + "-sheetNo-" + str(i) + ".xml"
    sh = wb.sheet_by_index(i)
    tags = [n.replace(" ", "").lower() for n in sh.row_values(0)]

    # This is going to come out as a string, which will write to a file in the end.
    result = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<myItems>\n"

    # Now, I'll create an XML node for each row in the sheet.
    PYTHONIOENCODING='utf-8'
    reload(sys);
    sys.setdefaultencoding("utf8")
    for row in range(1, sh.nrows):
        result += "  <item>\n"
        for i in range(len(tags)):
            tag = tags[i].encode("utf-8")
            val = str(sh.row_values(row)[i]).encode("utf-8")
            result += "    <%s>%s</%s>\n" % (tag, val, tag)
        result += "  </item>\n"

    # Close our pseudo-XML string.
    result += "</myItems>"

    # Write the result string to a file using the standard I/O.
    f = open(name, "w")
    f.write(result)
    f.close()
