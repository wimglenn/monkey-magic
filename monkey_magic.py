import gc
import types


def _wrap_builtin_function(f):
    def f_py(*args, **kwargs):
        return f(*args, **kwargs)
    f_py.__name__ = f.__name__
    return f_py


def monkeypatch(type_, obj, name=None):
    if isinstance(type_, tuple):
        for t in type_:
            monkeypatch(t, obj, name)
        return
    if name is None:
        if isinstance(obj, property):
            name = obj.fget.__name__
        else:
            name = obj.__name__
    if isinstance(obj, types.BuiltinFunctionType):
        obj = _wrap_builtin_function(obj)
    gc.get_referents(type_.__dict__)[0][name] = obj
