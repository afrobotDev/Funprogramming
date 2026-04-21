def new_resizer(max_width, max_height):
    def inner_resizer(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def inner_dimensions(width, height):
            width = max(min_width, min(width, max_width))
            height = max(min_height, min(height, max_height))
            return width, height

        return inner_dimensions
    return inner_resizer

