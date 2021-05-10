# coding: utf8
import ifcopenshell
from ifcopenshell import geom
import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

ifc_file_path = ("/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc")

def read_geom(ifc_file_path):

    ifc_file = ifcopenshell.open(ifc_file_path)
    beam = ifc_file.by_type("IfcColumn")[4]
    print(beam)
    settings = geom.settings()

    shape = geom.create_shape(settings, beam)

   # for ifc_entity in beam:
        #shape = geom.create_shape(settings, ifc_entity)

        # ios stands for IfcOpenShell
    ios_vertices = shape.geometry.verts
    ios_edges = shape.geometry.edges
    ios_faces = shape.geometry.faces

        # IfcOpenShell store vertices in a single tuple, same for edges and faces
    print(shape)
    print(ios_vertices)
    print("-------")
    print(ios_edges)
    print("-------")
    print(ios_faces)

    vertices = [
        np.array(ios_vertices[i: i + 3])
        for i in range(0, len(ios_vertices), 3)
    ]
    edges = [ios_edges[i: i + 2] for i in range(0, len(ios_edges), 2)]
    faces = [tuple(ios_faces[i: i + 3]) for i in range(0, len(ios_faces), 3)]

    print("This ", beam.is_a(), "has been defined by", len(vertices), "vertices", len(edges), "edges and",
          len(faces), "faces")

    print(vertices)
    print("--------------")
    print(edges)
    print("---------------")
    print(faces)


    #fig = plt.figure(figsize=(10, 10))
    #fig = plt.figure()

    #ax = fig.add_subplot(111, projection='3d')

    #ax.plot(vertices,faces,vertices)
    #plt.show()

read_geom(ifc_file_path)



"""
vertices = [
            FreeCAD.Vector(ios_vertices[i : i + 3])
            for i in range(0, len(ios_vertices), 3)
        ]
        edges = [ios_edges[i : i + 2] for i in range(0, len(ios_edges), 2)]
        faces = [tuple(ios_faces[i : i + 3]) for i in range(0, len(ios_faces), 3)]


        print("This ", ifc_entity.is_a(), "has been defined by", len(vertices), "vertices", len(edges), "edges and", len(faces), "faces")

        print(vertices)
        print("--------------")
        print(edges)
        print("---------------")
        print(faces)

        products = ifc_file.by_type("IfcProduct")
        product_shapes = []

        # For every product a shape is created if the shape has a Representation.
        for product in products:
            if product.is_a("IfcProductDefinitionShape") or product.is_a("IfcProductRepresentation"): continue
            if product.Representation is not None:
                shape = ifcopenshell.geom.create_shape(settings, product).geometry
                product_shapes.append((product, shape))
                
                
        
    Return a geometric representation from STEP-based IFCREPRESENTATIONSHAPE
    or
    Return an OpenCASCADE BRep if settings.USE_PYTHON_OPENCASCADE == True

    example:

    settings = ifcopenshell.geom.settings()
    settings.set(settings.USE_PYTHON_OPENCASCADE, True)

    ifc_file = ifcopenshell.open(file_path)
    products = ifc_file.by_type("IfcProduct")

    for i, product in enumerate(products):
        if product.Representation is not None:
            try:
                shape = geom.create_shape(settings, inst=product).geometry
                shape_gpXYZ = shape.Location().Transformation().TranslationPart() # These are methods of the TopoDS_Shape class from pythonOCC
                print(shape_gpXYZ.X(), shape_gpXYZ.Y(), shape_gpXYZ.Z()) # These are methods of the gpXYZ class from pythonOCC
    

"""
