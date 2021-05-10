import ifcopenshell.geom


from OCC.Core.BRepTools import BRepTools_WireExplorer
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopoDS import topods_Face, topods_Edge, topods_Wire, topods_Vertex
from OCC.Core.TopAbs import TopAbs_FACE, TopAbs_WIRE, TopAbs_EDGE, TopAbs_VERTEX



# Access the specific IFC file; external directory: (r"C:/Users/s136146/Desktop/StoreysWindowsMaterialsFacade.ifc")

ifc_file = ifcopenshell.open(r'/Users/abubakrazizi/PycharmProjects/SP_project/91004a.ifc')




# Use IfcOpenShell and OPENCASCADE to convert implicit geometry into explicit geometry
# Each Face consists of Wires, which consists of Edges, which has Vertices
FACE, WIRE, EDGE, VERTEX = TopAbs_FACE, TopAbs_WIRE, TopAbs_EDGE, \
                           TopAbs_VERTEX

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_PYTHON_OPENCASCADE, True)

#occ_display = ifcopenshell.geom.utils.initialize_display()



def sub(shape, ty):
    F = {
        TopAbs_FACE: topods_Face,
        TopAbs_WIRE: topods_Wire,
        TopAbs_EDGE: topods_Edge,
        TopAbs_VERTEX: topods_Vertex,
    }[ty]
    exp = TopExp_Explorer(shape, ty)
    while exp.More():
        face = F(exp.Current())
        yield face
        exp.Next()


def ring(wire, face):
    def vertices():
        exp = BRepTools_WireExplorer(wire, face)
        while exp.More():
            yield exp.CurrentVertex()
            exp.Next()

    return list(map(lambda p: (p.X(), p.Y(), p.Z()), map(BRep_Tool.Pnt, vertices())))


# Face to vertices
def get_vertices(shape):
    for face in sub(shape, FACE):
        for idx, wire in enumerate(sub(face, WIRE)):
            vertices = ring(wire, face)

            if idx > 0:
                vertices.reverse()
            return vertices



beam = ifc_file.by_type("IfcBeam")
be = beam[5]
#For sweotSolid 'Depth', 'ExtrudedDirection', 'LayerAssignments', 'Position', 'StyledByItem', 'SweptArea'
#For FacedBrep 'LayerAssignments', 'Outer', 'StyledByItem', --- 'CfsFaces', 'LayerAssignments', 'StyledByItem'


for element in beam:
    print(element.Representation.Representations.Outer)

shape = be.Representation.Representations

shape_1 = shape[0].Items
for z in shape_1:
    face = z.Outer.CfsFaces
    for y in face:
        outer = y.Bounds
        for i in outer:
            print(i.Bound)

    print(dir(i))

#space_boundary_shape = ifcopenshell.geom.create_shape(settings, i.Bound)



"""
for element in beam:
    space_boundary_shape = ifcopenshell.geom.create_shape(settings, beam)
    new_z = element.RelatingSpace.ObjectPlacement.PlacementRelTo.RelativePlacement.Location.Coordinates[2]
    new_z = new_z / 1000


    for v in get_vertices(space_boundary_shape):
        x,y,z = v
        z = z+new_z
        print(x,y,z)

"""