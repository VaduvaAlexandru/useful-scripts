#!/usr/bin/python
import sys
from openpyxl import load_workbook

wb = load_workbook('input/CGL_5.0_Registration_Template.xlsx')
print wb.get_sheet_names()
