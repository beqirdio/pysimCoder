"""
This is a procedural interface to the RCPblk library

roberto.bucher@supsi.ch

The following class is provided:

  RCPblk      - class with info for Rapid Controller Prototyping

"""
from numpy import array, ones

class RCPblk:
    def __init__(self, *args):
        if len(args) == 7:
            (fcn,pin,pout,nx,uy,realPar,intPar) = args
            dimPin = ones(len(pin), dtype = int)
            dimPout = ones(len(pout), dtype = int)
            dimRatio = []
            str=''
        elif (len(args) == 8) and (type(args[7]) is not list):
            (fcn,pin,pout,nx,uy,realPar,intPar,str) = args
            dimPin = ones(len(pin), dtype = int)
            dimPout = ones(len(pout), dtype = int)
            dimRatio = []
        elif (len(args) == 8) and (type(args[7]) is list):
            (fcn,pin,pout,dimRatio,nx,uy,realPar,intPar) = args
            dimPin = ones(len(pin), dtype = int)
            dimPout = ones(len(pout), dtype = int)
            str = ''
        elif len(args) == 9:
            (fcn,pin,pout,dimPin,dimPout,nx,uy,realPar,intPar) = args
            dimRatio = []
            str=''
        elif len(args) == 10:
            (fcn,pin,pout,dimPin,dimPout,nx,uy,realPar,intPar,str) = args
            dimRatio = []
        else:
            raise ValueError("Needs 6 to 9 arguments; received %i." % len(args))

        self.fcn = fcn
        self.pin = array(pin)
        self.pout = array(pout)
        self.dimPin = dimPin
        self.dimPout = dimPout
        self.nx = array(nx)
        self.uy = array(uy)
        self.realPar = array(realPar)
        self.intPar = array(intPar)
        self.str = str
        self.dimRatio = dimRatio

    def __str__(self):
        """String representation of the Block"""
        str =  "Function           : " + self.fcn.__str__() + "\n"
        str += "Input ports        : " + self.pin.__str__() + "\n"
        str += "Output ports      : " + self.pout.__str__() + "\n"
        str += "Input dimensions : " + self.dimPin.__str__() + "\n"
        str += "Output dimensions : " + self.dimPout.__str__() + "\n"
        str += "Nr. of states      : " + self.nx.__str__() + "\n"
        str += "Relation u->y      : " + self.uy.__str__() + "\n"
        str += "Real parameters    : " + self.realPar.__str__() + "\n"
        str += "Integer parameters : " + self.intPar.__str__() + "\n"
        str += "String Parameter   : " + self.str.__str__() + "\n"
        return str
