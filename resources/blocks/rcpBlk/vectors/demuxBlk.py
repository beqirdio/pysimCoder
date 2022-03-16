from supsisim.RCPblk import RCPblk
from numpy import ones

def demuxBlk(pin, pout):
    """

    Call:   demuxBlk(pin, pout)

    Parameters
    ----------
       pin: connected input port
       pout: connected output port(s)

    Returns
    -------
    blk  : RCPblk

    """
    in_dim = len(pout)
    out_dim = ones(len(pout), dtype = int)

    blk = RCPblk('demux',pin,pout, [in_dim], out_dim,[0,0],1, [], [])
    return blk
