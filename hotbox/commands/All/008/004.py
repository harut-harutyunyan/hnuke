#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: SHOT_SETUP
#
#----------------------------------------------------------------------------------------------------------




if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets

script = r'''set cut_paste_input [stack 0]
version 13.2 v5
BackdropNode {
inputs 0
name BackdropNode3
tile_color 0x9e9e9eff
label "<font color=white>EDIT"
note_font Arial
note_font_size 100
selected true
xpos -2074
ypos -6312
appearance Border
border_width 10
bdwidth 408
bdheight 707
z_order -2
}
BackdropNode {
inputs 0
name BackdropNode4
tile_color 0x9e9e9eff
label "<font color=white><h1><center>SHOT_SETUP"
note_font Arial
note_font_size 100
selected true
xpos -2200
ypos -7030
appearance Border
border_width 10
bdwidth 8249
bdheight 1975
}
BackdropNode {
inputs 0
name BackdropNode5
tile_color 0x9e9e9eff
label "<font color=white>PLATE"
note_font Arial
note_font_size 100
selected true
xpos -1609
ypos -6312
appearance Border
border_width 10
bdwidth 2886
bdheight 923
}
BackdropNode {
inputs 0
name BackdropNode6
tile_color 0x9e9e9eff
label "<font color=white>LGT"
note_font Arial
note_font_size 100
selected true
xpos 1392
ypos -6315
appearance Border
border_width 10
bdwidth 845
bdheight 690
}
BackdropNode {
inputs 0
name BackdropNode7
tile_color 0x9e9e9eff
label "<font color=white>ROTO"
note_font Arial
note_font_size 100
selected true
xpos 2382
ypos -6315
appearance Border
border_width 10
bdwidth 845
bdheight 690
}
BackdropNode {
inputs 0
name BackdropNode8
tile_color 0x9e9e9eff
label "<font color=white>3D"
note_font Arial
note_font_size 100
selected true
xpos 3379
ypos -6310
appearance Border
border_width 10
bdwidth 845
bdheight 690
}
BackdropNode {
inputs 0
name BackdropNode9
tile_color 0xaaffbfff
label "<font color=white>UTILITY"
note_font Arial
note_font_size 100
selected true
xpos 4900
ypos -6308
appearance Border
border_width 10
bdwidth 868
bdheight 868
}
push $cut_paste_input
NoOp {
name Anchor_2047d7a6bc
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos 2730
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title roto_002
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T roto_002}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_2047d7a6bc}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags roto
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
PostageStamp {
name Stamp4
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos 2730
ypos -5794
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title roto_002
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T roto_002}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>roto</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T <i>shot_setup</i>}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_2047d7a6bc
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
NoOp {
inputs 0
name Anchor_2047d7a6bc1
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos 2950
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title roto_003
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T roto_002}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_2047d7a6bc1}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags roto
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
PostageStamp {
name Stamp6
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos 2950
ypos -5794
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title roto_003
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T roto_003}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>roto</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T <i>shot_setup</i>}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_2047d7a6bc1
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
TimeOffset {
inputs 0
time_offset 1005
time ""
name TimeOffset1
label "(\[value time_offset] frames)"
selected true
xpos -1916
ypos -5915
}
NoOp {
name Anchor_1068d0e7d6
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font_size 20
selected true
xpos -1916
ypos -5788
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title edit_ref
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T edit_ref}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_1068d0e7d6}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags 2D,
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
NoOp {
name Stamp9
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font "Bitstream Vera Sans"
note_font_size 20
selected true
xpos -1916
ypos -5701
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title edit_ref
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T edit_ref}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>2D</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T "<i><font color=white><h1><center>SHOT_SETUP,<font color=white>EDIT</i>"}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +HIDDEN +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_1068d0e7d6
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
StickyNote {
inputs 0
name StickyNote11
tile_color 0x990000
label "VIEWER INPUT"
note_font_size 51
selected true
xpos 5205
ypos -5637
}
NoOp {
inputs 0
name Anchor_d522ed3
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos 724
ypos -5759
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title VZERO
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T GOR_101_010_050}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_d522ed3}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags 2D
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
PostageStamp {
name Stamp16
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos 724
ypos -5701
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title VZERO
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T VZERO}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>2D</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T "<i><font color=white>PLATE,<font color=white><h1><center>SHOT_SETUP</i>"}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_d522ed3
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
NoOp {
inputs 0
name Anchor_333d0e58fa
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos 2510
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title roto_001
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T roto_001}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_333d0e58fa}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags roto
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
PostageStamp {
name Stamp8
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos 2510
ypos -5794
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title roto_001
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T roto_001}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>roto</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." +HIDDEN T " "}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_333d0e58fa
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
NoOp {
inputs 0
name Anchor_111cc114ad
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font_size 20
selected true
xpos 3972
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title GEO
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T GEO}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_111cc114ad}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags 3D,
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
NoOp {
name Stamp11
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font "Bitstream Vera Sans"
note_font_size 20
selected true
xpos 3972
ypos -5794
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title GEO
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T GEO}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>3D</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T "<i><font color=white>3D,<font color=white><h1><center>SHOT_SETUP</i>"}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +HIDDEN +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_111cc114ad
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
NoOp {
inputs 0
name Anchor_d37efaf9f
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos 3503
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title CAM_MASTER
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T CAM_MAIN}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_d37efaf9f}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags Camera,
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
Camera {
projection_mode {{"\[expression \[value the_cam]projection_mode(\[value the_frame])]"}}
focal {{"\[expression \[value the_cam]focal(\[value the_frame])]"}}
haperture {{"\[expression \[value the_cam]haperture(\[value the_frame])]"}}
vaperture {{"\[expression \[value the_cam]vaperture(\[value the_frame])]"}}
near {{"\[expression \[value the_cam]near(\[value the_frame])]"}}
far {{"\[expression \[value the_cam]far(\[value the_frame])]"}}
win_translate {{"\[expression \[value the_cam]win_translate.u(\[value the_frame])]"} {"\[expression \[value the_cam]win_translate.v(\[value the_frame])]"}}
win_scale {{"\[expression \[value the_cam]win_scale.u(\[value the_frame])]"} {"\[expression \[value the_cam]win_scale.v(\[value the_frame])]"}}
winroll {{"\[expression \[value the_cam]winroll(\[value the_frame])]"}}
focal_point {{"\[expression \[value the_cam]focal_point(\[value the_frame])]"}}
fstop {{"\[expression \[value the_cam]fstop(\[value the_frame])]"}}
name Stamp17
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x33000001
note_font Arial
note_font_size 20
selected true
xpos 3519
ypos -5810
hide_input true
addUserKnob {20 DummyCam l Defaults +INVISIBLE}
addUserKnob {43 the_cam +INVISIBLE}
the_cam "\[\n#DummyCam v1.2 - Updated 5 May 2021.\nset starting_point \"this.input0\"\nset default \"this.d_\"\n\n# If cam has no inputs, return the default.\nif \{\[exists \$starting_point]\} \{\n    set x \[node \$starting_point]\n\} \{ \n    return \$default\n\}\n\nset finished 0\nwhile \{\$finished != 1\} \{\n\n    # First look for a Cam or Input or topnode.\n    while \{\[class \$x] != \"Camera3\" && \[class \$x] != \"Camera2\" && \[class \$x] != \"Camera\" && \[class \$x] != \"Input\" && \$x != \[topnode \$x]\} \{\n        set x \[node \$x.input0]\n    \}\n\n    # Then, check if node is a cam (and return), and otherwise, if it's an input, see if the parent exists and move to it.\n    if \{\[class \$x]==\"Camera3\"||\[class \$x]==\"Camera2\"||\[class \$x]==\"Camera\"\} \{\n        set x \[append x \".\"]\n        return \$x\n    \} \{ \n        if \{ \[class \$x]==\"Input\" \} \{ \n            set inp \"\$x.parent.input\"\n            set inputNum \[value \$x.number]\n            set inp \[append inp \$inputNum]\n            if \{ \[exists \$inp] \} \{\n                set x \[node \$inp]\n            \} \{ \n                set finished 1\n            \}\n        \} \{ \n            set finished 1\n        \}\n    \}\n\}\nreturn \$default\n]"
addUserKnob {43 the_frame +INVISIBLE}
the_frame "\[\nset the_camera \[string trimright \[value the_cam] .]\nif \{\[exists \$the_camera]\} \{\n    return \[value \$the_camera.frame]\n\} \{ \n    return \[frame]\n\}\n]"
addUserKnob {4 d_projection_mode l projection +INVISIBLE M {perspective orthographic uv spherical ""}}
addUserKnob {7 d_focal l "focal length" +INVISIBLE R 0 100}
d_focal 50
addUserKnob {7 d_haperture l "horiz aperture" +INVISIBLE R 0 50}
d_haperture 24.576
addUserKnob {7 d_vaperture l "vert aperture" +INVISIBLE R 0 50}
d_vaperture 18.672
addUserKnob {7 d_near l near +INVISIBLE R 0 10}
d_near 0.1
addUserKnob {7 d_far l far +INVISIBLE R 0 10000}
d_far 10000
addUserKnob {30 d_win_translate l "window translate" +INVISIBLE}
addUserKnob {30 d_win_scale l "window scale" +INVISIBLE}
d_win_scale {1 1}
addUserKnob {7 d_winroll l "window roll" +INVISIBLE R 0 45}
addUserKnob {7 d_focal_point l "focal distance" +INVISIBLE R 0 10}
d_focal_point 2
addUserKnob {7 d_fstop l fstop +INVISIBLE R 0 30}
d_fstop 16
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE +INVISIBLE T "<span style=\"color:#666\"><br/><b>DummyCam v1.2</b> - <a href=\"http://www.adrianpueyo.com\" style=\"color:#666;text-decoration: none;\">adrianpueyo.com</a>, 2019-2021</span>"}
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title CAM_MASTER
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T CAM_MASTER}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>Camera</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T <i>shot_setup</i>}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_d37efaf9f
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
}
Constant {
inputs 0
channels rgb
name Constant1
tile_color 0xff
selected true
xpos -1527
ypos -5988
postage_stamp false
}
Dot {
name Dot17
selected true
xpos -1493
ypos -5938
}
NoOp {
inputs 0
name Anchor_109506a8ef
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font_size 20
selected true
xpos -1326
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title RAW
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T RAW_DPX}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_109506a8ef}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags scan
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
set Nf1317000 [stack 0]
Dot {
name Dot14
selected true
xpos -1169
ypos -5938
}
NoOp {
inputs 0
name Anchor_d522ed448
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos -967
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title SCAN
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T GOR_101_010_050}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_d522ed448}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags scan
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
set Nf048d400 [stack 0]
Dot {
name Dot15
selected true
xpos -827
ypos -5938
}
NoOp {
inputs 0
name Anchor_d522ed1
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos -594
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title SCAN_DENOISE
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T GOR_101_010_050}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_d522ed1}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags "scan, 2D"
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
set N6f106800 [stack 0]
Dot {
name Dot16
selected true
xpos -416
ypos -5938
}
NoOp {
inputs 0
name Anchor_d522ed2
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos -161
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title SCAN_PAINT
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T GOR_101_010_050}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_d522ed2}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags 2D
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
set Ncc9ba800 [stack 0]
Dot {
name Dot13
selected true
xpos -8
ypos -5938
}
Switch {
inputs 5
which {{"\[exists input0.input0.input0]?0:\[exists input1.input0.input0]?1:\[exists input2.input0.input0]?2:\[exists input3.input0.input0]?3:4"}}
name Switch1
selected true
xpos 244
ypos -5942
}
NoOp {
name Anchor_d522ed4
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos 244
ypos -5609
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title WORK_PLATE
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T GOR_101_010_050}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_d522ed4}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags 2D
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
PostageStamp {
name Stamp13
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos 244
ypos -5551
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title WORK_PLATE
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T WORK_PLATE}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>2D</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T "<i><font color=white>PLATE,<font color=white><h1><center>SHOT_SETUP</i>"}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_d522ed4
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
Group {
inputs 0
name DeliveryConform1
tile_color 0x89afdff
label "global 2.0"
selected true
xpos 5338
ypos -5790
addUserKnob {20 DeliveryConform}
addUserKnob {26 description l "" +STARTLINE T "Conforms the image to delivery specs. \nMust be attached before final write node in each 'comp' shot."}
}
Input {
inputs 0
name metadata
xpos -805
ypos -715
number 1
}
Dot {
name Dot1
xpos -771
ypos -438
}
Input {
inputs 0
name comp
xpos -597
ypos -715
}
Crop {
box {0 0 {input.width} {input.height}}
crop false
name Crop1
label "\[value box.r] x \[value box.t]"
xpos -597
ypos -610
}
Remove {
operation keep
channels rgb
name Remove2
label "\[value channels]"
xpos -597
ypos -550
}
CopyMetaData {
inputs 2
name CopyMetaData1
xpos -597
ypos -442
disable {{"!\[exists parent.input1]"}}
}
Group {
name TechCheck
tile_color 0xff0000ff
selected true
xpos -597
ypos -399
}
Input {
inputs 0
name Input1
xpos -429
ypos 526
}
Dot {
name Dot2
xpos -395
ypos 581
}
set Nf89a7000 [stack 0]
Expression {
channel0 {rgba.red -rgba.green -rgba.blue none}
expr0 isinf(r)?1000:0
channel1 {-rgba.red rgba.green -rgba.blue none}
expr1 isinf(g)?1000:0
channel2 {-rgba.red -rgba.green rgba.blue none}
expr2 isinf(b)?1000:0
name Expression1
label INF
xpos -702
ypos 586
}
Expression {
temp_expr2 0
expr3 r+g+b
name Expression2
xpos -702
ypos 637
}
FilterErode {
channels alpha
size -250
name FilterErode1
xpos -702
ypos 727
}
push $Nf89a7000
Expression {
channel0 {rgba.red -rgba.green -rgba.blue none}
expr0 isnan(r)?1000:0
channel1 {-rgba.red rgba.green -rgba.blue none}
expr1 isnan(g)?1000:0
channel2 {-rgba.red -rgba.green rgba.blue none}
expr2 isnan(b)?1000:0
expr3 isnan(a)?1000:0
name Expression16
label NAN
xpos -531
ypos 626
}
FilterErode {
channels alpha
size -250
name FilterErode2
xpos -617
ypos 680
}
push $Nf89a7000
Grade {
inputs 1+1
multiply 0
add {1 0 0 0}
name Grade2
xpos -429
ypos 744
}
Grade {
inputs 1+1
multiply 0
add {1 0 0 0}
name Grade1
xpos -429
ypos 800
}
Output {
name Output1
selected true
xpos -429
ypos 1000
}
end_group
ModifyMetaData {
metadata {
 {set exr/pyshot/delivery_conform 1}
}
name ModifyMetaData1
xpos -597
ypos -373
}
Output {
name Output1
xpos -597
ypos -241
}
end_group
push $Nf1317000
NoOp {
name Stamp10
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font "Bitstream Vera Sans"
note_font_size 20
selected true
xpos -1326
ypos -5701
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title RAW
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T RAW}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>scan</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T "<i><font color=white>PLATE,<font color=white><h1><center>SHOT_SETUP</i>"}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +HIDDEN +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_109506a8ef
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
push $Nf048d400
PostageStamp {
name Stamp12
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos -967
ypos -5701
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title SCAN
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T SCAN}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>scan</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T <i>shot_setup</i>}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_d522ed448
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
push $N6f106800
PostageStamp {
name Stamp35
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos -594
ypos -5701
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title SCAN_DENOISE
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T SCAN_DENOISE}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T "<i>scan, 2D</i>"}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T "<i><font color=white>PLATE,<font color=white><h1><center>SHOT_SETUP</i>"}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_d522ed1
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
push $Ncc9ba800
PostageStamp {
name Stamp7
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos -161
ypos -5701
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title SCAN_PAINT
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T SCAN_PAINT}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>2D</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T "<i><font color=white>PLATE,<font color=white><h1><center>SHOT_SETUP</i>"}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_d522ed2
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
NoOp {
inputs 0
name Anchor_2797dea36a
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.anchorOnCreate()\n    except:\n        pass"
knobChanged stamps.anchorKnobChanged()
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0xffffff01
note_font Arial
note_font_size 20
selected true
xpos 1686
ypos -5946
addUserKnob {20 anchor_tab l "Anchor Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T anchor}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title lgt
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T lgt_BG}
addUserKnob {26 prev_name l "" +STARTLINE +HIDDEN T Anchor_2797dea36a}
addUserKnob {3 showing l "" +STARTLINE +HIDDEN}
addUserKnob {1 tags l Tags t "Comma-separated tags you can define for each Anchor, that will help you find it when invoking the Stamp Selector by pressing the Stamps shortkey with nothing selected."}
tags lgt
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 createStamp l new t "Create a new Stamp for this Anchor." -STARTLINE T stamps.stampCreateWired(nuke.thisNode())}
addUserKnob {22 selectStamps l select t "Reconnect all of this Anchor's Stamps." -STARTLINE T stamps.wiredSelectSimilar(nuke.thisNode().name())}
addUserKnob {22 reconnectStamps l reconnect -STARTLINE T stamps.anchorReconnectWired()}
addUserKnob {22 zoomNext l "zoom next" t "Navigate to this Anchor's next Stamp on the Node Graph." -STARTLINE T stamps.wiredZoomNext(nuke.thisNode().name())}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
PostageStamp {
name Stamp5
help "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021"
onCreate "if nuke.GUI:\n    try:\n        import stamps; stamps.wiredOnCreate()\n    except:\n        pass\n"
knobChanged "import stamps; stamps.wiredKnobChanged()"
autolabel "nuke.thisNode().knob(\"title\").value()"
tile_color 0x1000001
note_font Arial
note_font_size 20
selected true
xpos 1686
ypos -5794
hide_input true
addUserKnob {20 wired_tab l "Wired Stamp"}
addUserKnob {26 identifier -STARTLINE +HIDDEN T wired}
addUserKnob {3 lockCallbacks l "" +STARTLINE +HIDDEN}
addUserKnob {6 toReconnect -STARTLINE +HIDDEN}
addUserKnob {1 title l Title: t "Displayed name on the Node Graph for this Stamp and its Anchor.\nIMPORTANT: This is only for display purposes, and is different from the real/internal name of the Stamps."}
title lgt
addUserKnob {26 prev_title l "" +STARTLINE +HIDDEN T lgt}
addUserKnob {26 tags l Tags: t "Tags of this stamp's Anchor, for information purpose only.\nClick \"show anchor\" to change them." T <i>lgt</i>}
addUserKnob {26 backdrops l Backdrops: t "Labels of backdrop nodes which contain this stamp's Anchor." T <i>shot_setup</i>}
addUserKnob {26 line1 l "" +STARTLINE}
addUserKnob {6 postageStamp_show l "postage stamp" t "Enable the postage stamp thumbnail in this node.\nYou're seeing this because the class of this node includes the postage_stamp knob." +STARTLINE}
addUserKnob {26 anchor_label l Anchor: T " "}
addUserKnob {22 show_anchor l " show anchor " t "Show the properties panel for this Stamp's Anchor." -STARTLINE T stamps.wiredShowAnchor()}
addUserKnob {22 zoom_anchor l "zoom anchor" t "Navigate to this Stamp's Anchor on the Node Graph." -STARTLINE T stamps.wiredZoomAnchor()}
addUserKnob {26 stamps_label l Stamps: T " "}
addUserKnob {22 zoomNext l " zoom next " t "Navigate to this Stamp's next sibling on the Node Graph." -STARTLINE T stamps.wiredZoomNext()}
addUserKnob {22 selectSimilar l " select similar " t "Select all similar Stamps to this one on the Node Graph." -STARTLINE T stamps.wiredSelectSimilar()}
addUserKnob {26 space_1 l "" +STARTLINE T " "}
addUserKnob {26 reconnect_label l Reconnect: t "Reconnect by the stored Anchor name." T " "}
addUserKnob {22 reconnect_this l this t "Reconnect this Stamp to its Anchor, by its stored Anchor name." -STARTLINE T "n = nuke.thisNode()\ntry:\n    n.setInput(0,nuke.toNode(n.knob(\"anchor\").value()))\nexcept:\n    nuke.message(\"Unable to reconnect.\")\ntry:\n    import stamps\n    stamps.wiredGetStyle(n)\nexcept:\n    pass\n"}
addUserKnob {22 reconnect_similar l similar t "Reconnect this Stamp and similar ones to their Anchor, by their stored anchor name." -STARTLINE T stamps.wiredReconnectSimilar()}
addUserKnob {22 reconnect_all l all t "Reconnect all the Stamps to their Anchors, by their stored anchor names." -STARTLINE T stamps.wiredReconnectAll()}
addUserKnob {26 space_2 l "" +STARTLINE T " "}
addUserKnob {20 advanced_reconnection l "Advanced Reconnection" n 2}
addUserKnob {26 reconnect_by_title_label l "<font color=gold>By Title:" t "Reconnect by searching for a matching title." T " "}
addUserKnob {22 reconnect_by_title_this l this t "Look for an Anchor that shares this Stamp's title, and connect this Stamp to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitle()}
addUserKnob {22 reconnect_by_title_similar l similar t "Look for an Anchor that shares this Stamp's title, and connect this Stamp and similar ones to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSimilar()}
addUserKnob {22 reconnect_by_title_selected l selected t "For each Stamp selected, look for an Anchor that shares its title, and connect to it.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectByTitleSelected()}
addUserKnob {26 reconnect_by_selection_label l "<font color=orangered>By Selection:" t "Force reconnect to a selected Anchor." T " "}
addUserKnob {22 reconnect_by_selection_this l this t "Force reconnect this Stamp to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelection()}
addUserKnob {22 reconnect_by_selection_similar l similar t "Force reconnect this Stamp and similar ones to a selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSimilar()}
addUserKnob {22 reconnect_by_selection_selected l selected t "Force reconnect all selected Stamps to an also selected Anchor, whatever its name or title.\nIMPORTANT: Use this carefully, and only when the normal reconnection doesn't work." -STARTLINE T stamps.wiredReconnectBySelectionSelected()}
addUserKnob {1 anchor l Anchor}
anchor Anchor_2797dea36a
addUserKnob {6 auto_reconnect_by_title l "<font color=#ED9977>&nbsp; auto-reconnect by title" t "When creating this stamp again (like on copy-paste), auto-reconnect it by title instead of doing it by the saved anchor's name, and auto-turn this off immediately.\nIMPORTANT: Should be off by default. Only use this for setting up templates." +STARTLINE}
addUserKnob {26 line2 l "" +STARTLINE}
addUserKnob {22 buttonHelp l Help -STARTLINE T stamps.showHelp()}
addUserKnob {26 version l " " t "Stamps by Adrian Pueyo and Alexey Kuchinski.\nUpdated May 18 2021." -STARTLINE T "<a href=\"http://www.nukepedia.com/gizmos/other/stamps\" style=\"color:#666;text-decoration: none;\"><span style=\"color:#666\"> <big>Stamps v1.1</big></b></a>"}
}
'''


clipboard = QtWidgets.QApplication.clipboard()
clipboard.setText(script)
nuke.nodePaste('%clipboard%')
        