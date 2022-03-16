from supsisim.RCPblk import RCPblk

def printvecBlk(pin, vec_dim):
    """

    Call:   printvecBlk(pin, vec_dim)

    Parameters
    ----------
       pin: connected input port(s)
       vec_dim: dimension of input vector signals

    Returns
    -------
        blk  : RCPblk

    """

    blk = RCPblk('print_vec',pin,[],vec_dim,[0],[0,0],1, [], vec_dim)
    return blk
