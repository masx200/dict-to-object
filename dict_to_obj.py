def mapdicttoobj(iterable):  # {
    return list(map(dicttoobj, iterable))
# end def mapdicttoobj
# }


def dicttoobj(value: dict = {}) -> object:  # {
    if type(value) == dict:  # {
        return (ObjectProxy(value))
        # }
    else:  # {

        return (value)
    # end if
# end def dicttoobj
# }
# }


class ObjectProxy():  # {

    def __delitem__(self, *args):  # {
        return object.__delattr__(self, *args)
    # end def __delitem__
    # }

    def __getitem__(self, *args):  # {
        return self.__getattr__(*args)
    # end def __getitem__
    # }

    def __setattr__(self, key, value):  # {
        if type(key) == str:
            if not (key.startswith('__') & key.endswith('__')):
                if type(value) == dict:  # {
                    obj = dicttoobj(
                        value)
                    # }
                elif type(value) == list:  # {
                    obj = mapdicttoobj(
                        value)
                    # }

                else:  # {
                    obj = value
                    # }
                # end if
                object.__setattr__(self, key, obj)
            # end if

        # end if
        # end if
    # end def __setattr__
    # }

    def __setitem__(self, *args):  # {
        return self.__setattr__(*args)
    # end def __setitem__
    # }
    def __getattr__(self, key):  # {

        return object.__getattribute__(self, key)
    # end def __getattr__
    # }

    def __init__(self, iterabledict: dict = {}):  # {
        if type(iterabledict) != dict:
            raise TypeError('dict expected')
        # end if

        items = iterabledict.items()
        for item in items:
            key = item[0]
            value = item[1]
            self.__setattr__(key, value)
        # end for
    # end def __init__
# end class ObjectProxy
# }
# }
