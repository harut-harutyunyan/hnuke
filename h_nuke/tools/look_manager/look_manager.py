import nuke

class LookManager(object):
    pass


class LookManagerUtil(object):

    MAX_LOOKS = 8
    LOOK_PREFIX = "__look"
    APPLY_LOOK_SCRIPT = "node = nuke.thisNode()\nnode.resetKnobsToDefault()\nfor k, v in look.items():\n    knob = node[k]\n    knob.setValue(v[\"v\"])\n    if v[\"e\"]:\n        knob.setExpression(v[\"e\"])"

    @classmethod
    def get_node_look(cls, node):
        look = {}
        for k in node.writeKnobs(nuke.WRITE_NON_DEFAULT_ONLY).split():
            knob = node[k]
            look[k] = {"v": knob.value(), "e": None}
            if knob.hasExpression():
                look[k]["e"] = knob.toScript()[1:-1]

        return look

    @classmethod
    def get_num_looks(cls, node):
        return len([int(k.replace("{}_n_".format(cls.LOOK_PREFIX), "")) for k in node.knobs() if k.startswith(cls.LOOK_PREFIX)])

    @classmethod
    def get_next_look_num(cls, node):
        current = cls.get_num_looks(node)%cls.MAX_LOOKS
        return current

    @classmethod
    def create_look_btn(cls, node, name, look, tooltip):
        command = "look={}\n{}".format(str(look), cls.APPLY_LOOK_SCRIPT)
        longname = "{}_n_{}".format(cls.LOOK_PREFIX, name)
        if longname in node.knobs():
            btn = node.knob(longname)
            btn.setCommand(command)
        else:
            btn = nuke.PyScript_Knob(longname, name, command)
            node.addKnob(btn)

        if tooltip:
            btn.setTooltip(tooltip)

    @classmethod
    def add_look(cls, node, look_n=None, tooltip=None):
        if isinstance(look_n, int):
            look_n -= 1
        else:
            look_n = cls.get_next_look_num(node)

        look = cls.get_node_look(node)
        cls.create_look_btn(node, str(look_n+1), look, tooltip)

    @classmethod
    def set_look(cls, node, look_n):
        knob = node.knob("{}_n_{}".format(cls.LOOK_PREFIX, look_n))
        if knob:
            knob.execute()
