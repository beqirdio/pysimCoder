from supsisim.RCPblk import RCPblk


def gain_vecBlk(pin, pout, gains):
    """

    Gain of Matrix block

    Call: gain_vecBlk(pin, pout, gains)

    Parameters
    ----------
       pin: connected input port(s)
       pout: connected output port(s)
       gains : matrix or single coefficient

    Returns
    -------
        blk  : RCPblk

    """

    blk = RCPblk('gain_vec',pin,pout, [1,1], [0,0],1,[gains],[])
    return blk
