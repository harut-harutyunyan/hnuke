import pymel.core as pm


RENDER_ENGINES = {
    "arnold": {
        "lights": ["aiAreaLight"],
        "attrs": {
            "intens": "intensity",
            "exp": "exposure",
            "color": "color",
        },
        "aov_attr": "aiAov"
    },
    "redshift": {
        "lights": ["RedshiftPhysicalLight"],
        "attrs": {
            "intens": "intensity",
            "exp": "exposure",
            "color": "color",
        },
        "aov_attr": "aovLightGroup"
    },
    "vray": {
        "lights": ["VRayLightRectShape"],
        "attrs": {
            "intens": "intensityMult",
            "color": "lightColor",
        }
    },
}

def create_color_attr(obj, attr_name):
    pm.addAttr(obj, longName = attr_name, usedAsColor=True, attributeType="float3")
    [pm.addAttr(obj, longName = attr_name+c, attributeType="float", parent=attr_name) for c in ["R", "G", "B"]]

def create_original_attrs(lgt, attrs, vray=False):
    if not lgt.hasAttr("oring_intens"):
        lgt.addAttr("oring_intens")
        lgt.oring_intens.set(lgt.attr(attrs["intens"]).get())

    if not vray:
        if not lgt.hasAttr("oring_exp"):
            lgt.addAttr("oring_exp")
            lgt.oring_exp.set(lgt.attr(attrs["exp"]).get())

    if not lgt.hasAttr("orig_color"):
        create_color_attr(lgt, "orig_color")
        lgt.orig_color.set(lgt.attr(attrs["color"]).get())

def update_lights(light_info=None, engine="arnold"):
    if not light_info:
        print("no light info!")
        return

    supported_lights = RENDER_ENGINES[engine]["lights"]
    lgts = pm.ls(type=supported_lights)

    for lgt in lgts:

        aov_attr = RENDER_ENGINES[engine]["aov_attr"]
        light_grp = lgt.attr(aov_attr).get()
        if not light_grp in light_info.keys():
            continue

        vray = engine=="vray"
        attrs = RENDER_ENGINES[engine]["attrs"]
        create_original_attrs(lgt, attrs, vray)
        params = light_info[light_grp]

        oring_intens = lgt.oring_intens.get()
        intens = oring_intens * params["intens"] * (1-params["mute"])
        lgt.attr(attrs["intens"]).set(intens)

        if not engine=="vray":
            orig_exp = lgt.oring_exp.get()
            exp = orig_exp + params["exp"]
            lgt.attr(attrs["exp"]).set(exp)

        orig_color = lgt.orig_color.get()
        col = (orig_color[0]*params["col"][0], orig_color[1]*params["col"][1], orig_color[2]*params["col"][2])
        lgt.attr(attrs["color"]).set(col)
