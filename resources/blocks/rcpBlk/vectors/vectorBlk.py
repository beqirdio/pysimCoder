from supsisim.RCPblk import RCPblk

def vectorBlk(pout, vect):
    """

    Call:   vectorBlk(pout, vect)

    Parameters
    ----------
       pout: connected output port(s)
       vect : Vector in form of a list

    Returns
    -------
    blk  : RCPblk

    """
    n = len(vect)


    blk = RCPblk('vector',[],pout,[0],[n],[0,0],0, vect, [n])
    return blk
