import xml.etree.ElementTree as ET
from ElementTree_pretty import prettify
import ifcopenshell.util
import ifcopenshell.util.element
from xml.dom import minidom


ifc_file = ifcopenshell.open("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")
print(ifc_file.schema)

column = ifc_file.by_type("IfcColumn")[0]

"""for dim in column:
    geo = ifcopenshell.util.element.get_psets(dim)
    print(geo)"""

geo = ifcopenshell.util.element.get_psets(column)


top = ET.Element('Job', dict(BvxVersion="1.0", DeliveryDate=".." ))

#comment = Comment('Generated for PyMOTW')
#top.append(comment)

"""It is possible to specify different user-defined properties using the attribute definitions. 
These user attributes can then be copied into parts as necessary.
"""
child1 = ET.SubElement(top, 'AttDefs')
#child.text = 'This child contains text.'

"""The "Parts" element contains all parts to be processed in the job. The "Parts" element has no further attributes. 
The individual parts follow the element header. The job can contain as many parts as the user desires. """
child2 = ET.SubElement(top, 'Parts')
child2.tail = 'Here comes the Part Parameters'
#node1 = SubElement(child2, 'Part', dict(Name = "", PartId = "", width = "", Hight ="" , Length = "", Dimension = "", ReqQuantity = "", Comments = "", JobName = "", Grade = "") )
node1 = ET.SubElement(child2, 'Part', geo )

node2 = ET.SubElement(child2, 'Part')



"""The board descriptions are used to optimize a job. 
Parts that are entered under a board are not new parts, just references to existing parts that have been optimized and placed (fitted) together in a rough timber (board)."""
child3 = ET.SubElement(top, 'Boards')



"""child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'
"""
#print(prettify(top))

# Converting the xml data to byte object,
# for allowing flushing data to file
# stream
xmlstr = minidom.parseString(ET.tostring(top)).toprettyxml(indent="   ")
with open("New_Database.BVX", "w") as f:
    f.write(xmlstr)