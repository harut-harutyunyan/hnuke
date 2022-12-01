#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle RGBA
#
#----------------------------------------------------------------------------------------------------------

m = ["rgb", "rgba", "alpha", "rgb"]
for i in nuke.selectedNodes():
    cur = i["channels"].value()
    i["channels"].setValue(m[m.index(cur)%3+1])