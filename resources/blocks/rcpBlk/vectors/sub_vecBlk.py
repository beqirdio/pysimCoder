from supsisim.RCPblk import RCPblk

def sub_vecBlk(pin, pout):
    """

    Call:   sub_vecBlk(pin, pout)

    Parameters
    ----------
       pin: connected input port
       pout: connected output port(s)

    Returns
    -------
    blk  : RCPblk

    """

    blk = RCPblk('sub_vec',pin,pout,[1,1],[0,0],1,[],[])
    return blk
