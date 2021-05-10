import xml.etree.ElementTree as ET
from ElementTree_pretty import prettify
import ifcopenshell.util
import ifcopenshell.util.element
from xml.dom import minidom


## Access the specific IFC file; external directory: ("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")
from Operations import operations

ifc_file = ifcopenshell.open("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")
#print(ifc_file.schema)


column = ifc_file.by_type("IfcColumn")
top = ET.Element('Job', dict(BvxVersion="1.0", DeliveryDate=".." ))


"""It is possible to specify different user-defined properties using the attribute definitions. 
These user attributes can then be copied into parts as necessary.
"""
child1 = ET.SubElement(top, 'AttDefs')
#child.text = 'This child contains text.'

"""The "Parts" element contains all parts to be processed in the job. The "Parts" element has no further attributes. 
The individual parts follow the element header. The job can contain as many parts as the user desires. """

child2 = ET.SubElement(top, 'Parts')

i = 1


def OperationPart(child,name,nartId,width,hight,length,dimension):
    if str(dimension) == "RECT":
        shape = "Rectangular"
    else:
        shape = str(dimension)
    part = ET.SubElement(child, 'Part',
                          dict(Name=str(name), PartId=str(nartId), width=str(width), Hight=str(hight), Length=str(length), Dimension=shape,
                               ReqQuantity="", Comments="", JobName="", Grade=""))
    return part

for col in column:
    geo = ifcopenshell.util.element.get_psets(col)
    #print(geo)
    name = geo["Pset_Wood"]['Type']
    partID = i
    width = geo["Pset_Wood"]['Width']
    height = geo["Pset_Wood"]['Height']
    length = geo["Pset_Wood"]['Length']
    dimension = geo["Pset_Wood"]['Shape']

    part = OperationPart(child2,name,partID,width,height,length,dimension)

    oper =  operations()
    saw1 , saw1_dict = oper.Sawcut("3","Right", "0.00")
    saw2 , saw2_dict = oper.Sawcut("3","Left", length)
    lap , lap_dict = oper.Lap("4")

    node = ET.SubElement(part, saw1, saw1_dict)
    node2 = ET.SubElement(part, saw2, saw2_dict)
    node3 = ET.SubElement(part, lap, lap_dict)

    i+=1
    #node2 = ET.SubElement(child2, 'Part')


#child2.tail = 'Here comes the Part Parameters'

#node1 = ET.SubElement(child2, 'Part', geo )



"""The board descriptions are used to optimize a job. 
Parts that are entered under a board are not new parts, just references to existing parts that have been optimized and placed (fitted) together in a rough timber (board)."""
child3 = ET.SubElement(top, 'Boards')


# Converting the xml data to byte object,
# for allowing flushing data to file
# stream
xmlstr = minidom.parseString(ET.tostring(top)).toprettyxml(indent="   ")
with open("New_Database1.xml", "w") as f:
    f.write(xmlstr)