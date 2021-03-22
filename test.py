import ifcopenshell

f = ifcopenshell.open("91004a.ifc")

# Accessing entity instances by type:
f.by_type("ifcwall")[:2]
[#91=IfcWallStandardCase('2O2Fr$t4X7Zf8NOew3FL9r',#1,'Basic Wall:Interior - Partition (92mm Stud):144586',$,'Basic Wall:Interior - Partition (92mm Stud):128360',#5198,#18806,'144586'), #92=IfcWallStandardCase('2O2Fr$t4X7Zf8NOew3FLIE',#1,'Basic Wall:Interior - Partition (92mm Stud):143921',$,'Basic Wall:Interior - Partition (92mm Stud):128360',#5206,#18805,'143921')]
wall = _[0]
len(wall) # number of EXPRESS attributes


# Accessing EXPRESS attributes by name:
wall.GlobalId
"2O2Fr$t4X7Zf8NOew3FL9r"
wall.Name = "My wall"
wall.NonExistingAttr
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".\ifcopenshell.py", line 14, in __getattr__
    except: raise AttributeError("entity instance of type '%s' has no attribute'%s'"%(self.wrapped_data.is_a(), name)) from None
AttributeError: entity instance of type 'IfcWallStandardCase' has no attribute 'NonExistingAttr'
wall.GlobalId = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".\ifcopenshell.py", line 26, in __setattr__
    self[self.wrapped_data.get_argument_index(key)] = value
  File ".\ifcopenshell.py", line 30, in __setitem__
    self.wrapped_data.set_argument(idx, entity_instance.map_value(value))
  File ".\ifc_wrapper.py", line 118, in <lambda>
    set_argument = lambda self,x,y: self._set_argument(x) if y is None else self
._set_argument(x,y)
  File ".\ifc_wrapper.py", line 114, in _set_argument
    def _set_argument(self, *args): return _ifc_wrapper.entity_instance__set_argument(self, *args)
RuntimeError: INT is not a valid type for 'GlobalId'
"""
 # Creating new entity instances
f.createIfcCartesianPoint(Coordinates=(1.0,1.5,2.0))
#27530=IfcCartesianPoint((1.,1.5,2.))
# Working with GlobalId attributes:
import uuid
ifcopenshell.guid.compress(uuid.uuid1().hex)
'3x4C8Q_6qHuv$P$FYkANRX'
new_guid = _
owner_hist = f.by_type("IfcOwnerHistory")[0]
new_wall = f.createIfcWallStandardCase(new_guid, owner_hist, None, None, Tag='my_tag')
new_wall.ObjectType = ''
new_wall.ObjectPlacement = new_wall.Representation = None

# Accessing entity instances by instance id or GlobalId:
f[92]
#92=IfcWallStandardCase('2O2Fr$t4X7Zf8NOew3FLIE',#1,'Basic Wall:Interior - Partition (92mm Stud):143921',$,'Basic Wall:Interior - Partition (92mm Stud):128360',#5206,#18805,'143921')
f['2O2Fr$t4X7Zf8NOew3FLIE']
#92=IfcWallStandardCase('2O2Fr$t4X7Zf8NOew3FLIE',#1,'Basic Wall:Interior - Partition (92mm Stud):143921',$,'Basic Wall:Interior - Partition (92mm Stud):128360',#5206,#18805,'143921')

# Writing IFC-SPF files to disk:
f.write("out.ifc")