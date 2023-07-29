import gc


def monkeypatch(type_, func):
    gc.get_referents(type_.__dict__)[0][func.__name__] = func
