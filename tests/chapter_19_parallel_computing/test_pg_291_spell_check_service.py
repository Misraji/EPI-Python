# pytest documentation: https://docs.pytest.org/en/stable/
from concurrent.futures import ThreadPoolExecutor

from epi_python.chapter_19_parallel_computing.pg_291_spell_check_service import SpellCheckService


def test_cache():
    calls=[]
    service=SpellCheckService(lambda word: calls.append(word) or [word])
    assert service.service('a')==['a']
    assert service.service('a')==['a']
    assert calls==['a']
    with ThreadPoolExecutor(max_workers=4) as executor:
        assert list(executor.map(service.service, ['b']*8))==[['b']]*8
