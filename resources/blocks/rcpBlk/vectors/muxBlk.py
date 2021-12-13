from supsisim.RCPblk import RCPblk
from numpy import ones

def muxBlk(pin, pout):
    """

    Call:   muxBlk(pin, pout)

    Parameters
    ----------
       pin: connected input port
       pout: connected output port(s)

    Returns
    -------
    blk  : RCPblk

    """
    out_dim = len(pin)
    in_dim = ones(len(pin), dtype = int)

    blk = RCPblk('mux',pin,pout, in_dim, [out_dim],[0,0],1, [], [])
    return blk
