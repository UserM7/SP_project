# coding: utf8
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

ifc_file = ifcopenshell.open("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")

products = ifc_file.by_type("IfcProduct")

List_coor = []
products_to_display = []

for product in products:
    if not product.is_a ( "IfcPlate" ) and not product.is_a ( "IfcSite" ) and not product.is_a (
            "IfcWall" ) and not product.is_a ( "IfcBuildingElementPart" ):
        if product.Representation is not None:
            products_to_display.append ( product )

for dim in products_to_display:
    inf = dim.Representation.Representations
    if inf [0] [2] == "Brep":
        coor = dim.Representation.Representations [0].Items [0].Outer.CfsFaces [0].Bounds [0].Bound.Polygon
        for i in coor:
            List_coor.append ( i )
    else:
        rec = dim.Representation.Representations [0].Items [0]

#print ( List_coor )

beam = ifc_file.by_type("IfcBeam")[5]
print(ifcopenshell.util.element.get_psets(beam))

"""{'Pset_Wood': {'Type': '48x248', 'Length': 3542.0, 'Width': '48', 'Height': '248', 'Use': 'SVILL', 'Material code': 'C24', 'Shape': 'RECT'}, 
'Pset_BeamCommon': {'Reference': 'S1-2', 'Span': 3542.000000000001, 'LoadBearing': False, 'Slope': 0.0}}"""