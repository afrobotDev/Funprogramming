from copy import deepcopy

def css_styles(initial_styles):
    new_styles = deepcopy(initial_styles)
    def add_style(selector, proprty, value):
        if selector not in initial_styles:
            new_dict = {}
            new_styles[selector] = new_dict
            new_dict[proprty] = value 

        new_styles[selector][proprty] = value
        return new_styles

    return add_style


