from supsisim.RCPblk import RCPblk


def gain_vecBlk(pin, pout, gains, vd):
    """

    Gain of Matrix block

    Call: gain_vecBlk(pin, pout, gains, vec_dim)

    Parameters
    ----------
       pin: connected input port(s)
       pout: connected output port(s)
       gains : matrix or single coefficient
       vd (vec_dim): dimensions of input/output vector

    Returns
    -------
        blk  : RCPblk

    """

    blk = RCPblk('gain_vec',pin,pout, vd, vd, [0,0],1,[gains],vd)
    return blk
