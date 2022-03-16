from supsisim.RCPblk import RCPblk

def sum_vecBlk(pin, pout):
    """

    Call:   sum_vecBlk(pin, pout)

    Parameters
    ----------
       pin: connected input port
       pout: connected output port(s)

    Returns
    -------
    blk  : RCPblk

    """

    blk = RCPblk('sum_vec',pin,pout,[1,1],[0,0],1,[],[])
    return blk
