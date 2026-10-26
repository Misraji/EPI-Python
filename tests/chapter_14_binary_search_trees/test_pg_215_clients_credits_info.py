from epi_python.chapter_14_binary_search_trees.pg_215_clients_credits_info import ClientsCreditsInfo


def test_credit_ledger():
    info=ClientsCreditsInfo()
    assert info.max()=='' and info.lookup('missing')==-1
    info.insert('a',5); info.insert('b',9)
    assert info.max()=='b'
    info.add_all(4)
    assert info.lookup('a')==9 and info.lookup('b')==13
    info.insert('c',11)
    assert info.lookup('c')==11 and info.max()=='b'
    info.insert('a',20)
    assert info.max()=='a'
    assert info.remove('a') and not info.remove('a')
    assert info.max()=='b'
    assert info.remove('b') and info.remove('c') and info.max()==''
