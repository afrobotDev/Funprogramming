def zipmap(keys, values):

    zipped = dict()

    if len(keys) == 0 or len(values) == 0:

        return zipped
    

    zipped[keys[0]] = values[0]# Add first elements of the inputs as key and value pairs 

    zipped.update(zipmap(keys[1:], values[1:]))

    return zipped

