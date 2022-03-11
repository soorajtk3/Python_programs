import ari
def test_ari_emptychar():
    ret = ari.ari_emptychar('')
    assert ret == 0
def test_ari_charalpha():
    ret =ari.ari_charalpha('#$!&')
    assert ret == False
def test_ari_numchar():
    ret = ari.ari_numchar('1apqhgkl54')
    assert ret ==  10   

def test_ari_emptyword():
    ret=ari.ari_emptyword("pqrst")
    assert ret == None
def test_ari_numwords():
     ret=ari.ari_numwords('i am passionate about programming')
     assert ret==4

def test_ari_emptysentence():
     ret=ari.ari_emptysentence('asdasfda pqrstuvwazjdjd')
     assert ret==None
def test_ari_sentence():
     ret=ari.ari_sentences('how are you? where are you? dont feel bad. Study well!')
     assert ret==4  


