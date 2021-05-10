#Imported library to parse IFC and create XML file. 
import itertools

import xml.etree.ElementTree as ET
import ifcopenshell.util
import ifcopenshell.util.element
from xml.dom import minidom

from Operations import operations

## Access the specific IFC file; external directory: ("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")
ifc_file = ifcopenshell.open("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")



# Specify the column and beam by making use of IFC entity 'IfcProduct'
products = ifc_file.by_type("IfcProduct")

products_to_display = []


for product in products:
    if (product.is_a("IfcPlate") or
         product.is_a("IfcSite") or product.is_a("IfcWall") or product.is_a("IfcBuildingElementPart")):
            continue
    if product.Representation is not None:
        products_to_display.append(product)
#print(products_to_display)

# Create the 'BVX' root by making use of ElementTree
root = ET.Element('Job', dict(BvxVersion="1.0", DeliveryDate=".."))


#Create 'Attribute Definitions' elements called 'AttDefs' and append it to the Root of the document
parent_1 = ET.SubElement(root, 'AttDefs')


# Create new variable called parent_2 that hold the 'Parts' elements called 'parts' and append it to the Root of the document
parent_2 = ET.SubElement(root, 'Parts')

#Variable for numerating the partId Attribute
i = 1

#Function that holds the 'part' SubElement of 'parts' whith the attributes as its argument
def OperationPart(parent_2, name, partId, width, hight, length, dimension):
    if str(dimension) == "RECT":
        shape = "Rectangular"
    else:
        shape = str(dimension)
    child_2 = ET.SubElement(parent_2, 'Part',
                            dict(Name=str(name), PartId=str(partId), width=str(width), Hight=str(hight),
                                 Length=str(length), Dimension=shape,
                                 ReqQuantity="", Comments="", JobName="", Grade=""))
    return child_2


for be in products_to_display:
    geo = ifcopenshell.util.element.get_psets(be)

    name = geo["Pset_Wood"]['Type']
    partID = i
    width = geo["Pset_Wood"]['Width']
    height = geo["Pset_Wood"]['Height']
    length = geo["Pset_Wood"]['Length']
    dimension = geo["Pset_Wood"]['Shape']

    part = OperationPart(parent_2, name, partID, width, height, length, dimension)

    oper = operations()
    saw1, saw1_dict = oper.Sawcut("3", "Right", "0.00")
    saw2, saw2_dict = oper.Sawcut("3", "Left", length)
    lap, lap_dict = oper.Lap("4", length)

    #nodes are the information that are shown in part
    node1 = ET.SubElement(part, saw1, saw1_dict)
    node2 = ET.SubElement(part, saw2, saw2_dict)

    node3 = ET.SubElement(part, lap, lap_dict)


    #The i increses with one for each loop
    i += 1


#The board descriptions are used to optimize a job.
#Parts that are entered under a board are not new parts, just references to existing parts.
parent_3 = ET.SubElement(root, 'Boards')

# Converting the xml data to byte object, using MiniDom
# for allowing flushing data to file
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("New_Database1-1.XML", "w") as f:
    f.write(xmlstr)
