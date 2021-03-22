


import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from xml.dom import minidom
import xml.etree.ElementTree as xe

ifc_file = ifcopenshell.open("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")
print(ifc_file.schema)

column = ifc_file.by_type("IfcColumn")[0]

"""for dim in column:
    geo = ifcopenshell.util.element.get_psets(dim)
    print(geo)"""

geo = ifcopenshell.util.element.get_psets(column)
print(geo)