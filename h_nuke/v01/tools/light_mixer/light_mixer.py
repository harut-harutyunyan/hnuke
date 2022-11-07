import os
import socket
import nuke

class LightMixerUtil(object):
    LGT_PREFIX = "lgt_"
    RENDER_ENGINES = {
    0: "arnold",
    1: "redshift",
    2: "vray",
    }
    MAYA_HANDLER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "maya"))
    HOST = "localhost"
    PORT = 20181

    @classmethod
    def this_node(cls):
        return nuke.thisNode()

    @classmethod
    def clear_knobs(cls):
        this_node = cls.this_node()
        for k, i in this_node.knobs().items():
            if k.startswith("lgt"):
                this_node.removeKnob(i)

    @classmethod
    def clear_grp_contents(cls):
        this_node = cls.this_node()
        this_node.begin()

        [nuke.delete(n) for n in nuke.allNodes() if not n.name() in ["In", "Out"]]

        nuke.toNode("Out").setInput(0, nuke.toNode("In"))

        this_node.end()

    @classmethod
    def clear(cls):
        cls.clear_knobs()
        cls.clear_grp_contents()

    @classmethod
    def get_render_engine(cls):
        return cls.RENDER_ENGINES[cls.this_node()["render_engine"].getValue()]

    @classmethod
    def get_input_node(cls):
        read = cls.this_node().dependencies()

        if len(read)<1:
            raise ValueError("not connected to a read")
        else:
            return read[0]

    @classmethod
    def get_lgt_aovs(cls):
        return list(set([c.split(".")[0] for c in cls.get_input_node().channels() if c.startswith(cls.LGT_PREFIX)]))

    @classmethod
    def build(cls):
        render_engine = cls.get_render_engine()
        layers = cls.get_lgt_aovs()
        this_node = cls.this_node()

        cls.clear()
        this_node.begin()

        last_node = nuke.toNode("In")
        for layer in layers:
            shuffle = nuke.nodes.Shuffle()
            shuffle.setName(layer)
            shuffle["in"].setValue(layer)
            shuffle.setInput(0, last_node)

            merge_f = nuke.nodes.Merge2()
            merge_f["operation"].setValue(10)
            merge_f.setInput(0, last_node)
            merge_f.setInput(1, shuffle)

            color = nuke.nodes.Multiply()
            color["value"].setSingleValue(False)
            color.setName(layer+"_color")
            color.setInput(0, shuffle)

            intens = nuke.nodes.Multiply()
            intens.setName(layer+"_intensity")
            intens.setInput(0, color)

            if not render_engine == "vray":
                exposure = nuke.nodes.EXPTool()
                exposure.setName(layer+"_exposure")
                exposure["mode"].setValue(0)
                exposure.setInput(0, intens)
            else:
                exposure = intens

            merge = nuke.nodes.Merge2()
            merge["operation"].setValue(24)
            merge.setInput(0, merge_f)
            merge.setInput(1, exposure)
            last_node = merge

            aov_name = layer.replace(cls.LGT_PREFIX, "")
            aov_name = aov_name.replace("_", " ")
            this_node.addKnob(nuke.Text_Knob(layer+"_tex", "",  '<font size=4 color="orange">{}</font>'.format(aov_name)))

            link = nuke.Link_Knob(layer + "_mute", "[M]")
            link.setLink("{}.disable".format(merge.name()))
            this_node.addKnob(link)
            link.clearFlag(nuke.STARTLINE)

            name = layer + "_col"
            link = nuke.Color_Knob(name, "Color")
            link.setValue(1)
            link.setSingleValue(False)
            color["value"].setExpression(expression="parent.{}.r".format(name), channel=0)
            color["value"].setExpression(expression="parent.{}.g".format(name), channel=1)
            color["value"].setExpression(expression="parent.{}.b".format(name), channel=2)
            this_node.addKnob(link)

            name = layer + "_intens"
            link = nuke.Double_Knob(name, "Intensity")
            link.setValue(1)
            link.setRange(0, 5)
            intens["value"].setExpression("parent.{}".format(name))
            this_node.addKnob(link)

            if not render_engine == "vray":
                link = nuke.Link_Knob(layer + "_exp", "Exposure")
                link.setLink("{}.red".format(exposure.name()))
                this_node.addKnob(link)

            this_node.addKnob(nuke.Text_Knob(layer+"_div", ""))

        nuke.toNode('Out').setInput(0, last_node)

        this_node.end()

    @classmethod
    def collect_light_info(cls):
        this_node = cls.this_node()

        vals = ["mute", "intens", "exp", "col"]

        knobs = [i for i, n in this_node.knobs().items() if i.startswith("lgt_") and i.rsplit("_", 1)[1] in vals]
        light_info = {l.replace("lgt_", "").rsplit("_", 1)[0]:{} for l in knobs}
        for k in knobs:
            lgt_name = k.replace("lgt_", "")
            lgt_name, val = lgt_name.rsplit("_", 1)
            light_info[lgt_name][val] = this_node[k].getValue()

        return light_info


    @classmethod
    def send_to_maya(cls):
        light_info = cls.collect_light_info()
        maya_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        maya_socket.connect((cls.HOST, cls.PORT))

        command = "import sys\nsys.path.append(r\"{}\")\nimport mixer_maya_handler\n".format(cls.MAYA_HANDLER_PATH)
        command += "light_info={}".format(str(light_info))
        command += "\nmixer_maya_handler.update_lights(light_info, \"{}\")".format(cls.get_render_engine())
        maya_socket.sendall(command.encode())
        data = maya_socket.recv(4096)
        # print(command)
        # print(data)

        maya_socket.close()

    @classmethod
    def test_this(cls):
        cls.send_to_maya()
