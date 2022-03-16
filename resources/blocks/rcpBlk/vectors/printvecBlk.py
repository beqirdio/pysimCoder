from supsisim.RCPblk import RCPblk

def printvecBlk(pin):
    """

    Call:   printvecBlk(pin)

    Parameters
    ----------
       pin: connected input port(s)

    Returns
    -------
        blk  : RCPblk

    """

    blk = RCPblk('print_vec',pin,[],[0,0],1, [], [])
    return blk
