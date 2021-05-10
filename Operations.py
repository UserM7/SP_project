import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element


class operations():

    def Sawcut(self,referenceSide,orientation, lengthMeas):
            name = 'SawCut'
            saw = dict(ReferenceSide=str(referenceSide),
                       Orientation=str(orientation),
                       Angle="90",
                       Bevel="90",
                       LengthMeas=str(lengthMeas),
                       CrossMeas1="0",
                       CrossMeas2="0")
            return name, saw

    def Lap(self,referenceSide, lengthMeas):
        name = 'Lap'
        lap = dict(ReferenceSide=str(referenceSide),
                   LengthMeas=str(lengthMeas),
                   CrossMeas1="",
                   CrossMeas2="",
                   Length="",
                   LengthOrientation="",
                   Angle="",
                   Bevel="",
                   Rotation="",
                   SplinterFree="")
        return name, lap

    def Housing(self,referenceSide):
        name = 'Housing'
        housing = dict(ReferenceSide=str(referenceSide),
                       LengthMeas="",
                       CrossMeas1="",
                       CrossMeas2="",
                       Length="",
                       LengthOrientation="",
                       Angle="",
                       Bevel="",
                       Rotation="",
                       SplinterFree="",
                       Width="",
                       WidthOrientation="")
        return name, housing

    def SawDado(self,ReferenceSide,StartLengthMeas,EndLengthMeas,StartCrossMeas,EndCrossMeas,Depth):
        name = 'SawDado'
        sawdado = dict(ReferenceSide=str(ReferenceSide),
                       StartLengthMeas=str(StartLengthMeas),
                       EndLengthMeas=str(EndLengthMeas),
                       StartCrossMeas=str(StartCrossMeas),
                       EndCrossMeas=str(EndCrossMeas),
                       Depth=str(Depth),
                       Bevel="0",
                       Measurement="Outside",
                       SawBladeOrientation="Right",
                       Offcut="False")
        return name, sawdado