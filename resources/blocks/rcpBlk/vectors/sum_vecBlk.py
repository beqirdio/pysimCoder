from supsisim.RCPblk import RCPblk

def sum_vecBlk(pin, pout, vd):
    """

    Call:   sum_vecBlk(pin, pout, vd)

    Parameters
    ----------
       pin: connected input port
       pout: connected output port(s)
       vd (vect_dim): dimensions of vectors for addition

    Returns
    -------
    blk  : RCPblk

    """

    blk = RCPblk('sum_vec',pin,pout,[vd],[vd],[0,0],1,[],[vd])
    return blk
