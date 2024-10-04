import functools

class HTMLNode:
    def __init__(self, 
                tag = None, 
                value = None,
                children = None,
                props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def aprops_to_html(self):
        lst_props = list(self.props.items())
        lst_props_str = map(lambda t: self.convert_prop(t), lst_props)
        return " " + (" ").join(lst_props_str)

    def __repr__(self):
        return f"- HTMLNode: \n--tag: {self.tag} \n--value: {self.value} \n--children: {self.children} \n--props: {self.props}"

    def convert_prop(self, prop_item):
        prop_attr = prop_item[0]
        prop_val = prop_item[1]
        return prop_attr + f"=\"{prop_val}\""

    def get_attr_tag(self):
        if self.props != None:
            attr = self.aprops_to_html()
            return attr
        else:
            return ""

    def get_html_open_tag(self):
        return f"<{self.tag}{self.get_attr_tag()}>"

    def get_html_close_tag(self):
        return f"</{self.tag}>"

    def get_html_value_tag(self):
        if self.value != None:
            return self.value
        else:
            return ""

    def to_html_default(self):
        open_tag = self.get_html_open_tag()
        value_tag = self.get_html_value_tag()
        close_tag = self.get_html_close_tag()
        return f"{open_tag}{value_tag}{close_tag}"
