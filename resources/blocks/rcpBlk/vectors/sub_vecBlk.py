from supsisim.RCPblk import RCPblk

def sub_vecBlk(pin, pout, vd):
    """

    Call:   sub_vecBlk(pin, pout, vd)

    Parameters
    ----------
       pin: connected input port
       pout: connected output port(s)
       vd (vect_dim): dimensions of vectors for subtraction

    Returns
    -------
    blk  : RCPblk

    """

    blk = RCPblk('sub_vec',pin,pout,[vd],[vd],[0,0],1,[],[vd])
    return blk
