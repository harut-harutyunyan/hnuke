#dDot v1.2

import nuke

FONT_SIZE = 42
DISTANCE_FROM_NODE = 150
UPDATE_UI = "node = nuke.toNode(nuke.thisNode().knob('label').getValue())\nif node:\n    nuke.thisNode().setInput(0, node)"

def dDotParent():

    selected = nuke.Root().selectedNode()

    if selected == None:
        nuke.message('Error:Nothing is selected.')

    elif len(nuke.Root().selectedNodes()) > 1:
        nuke.message('Error:Multiple nodes selected')

    if len([n for n in selected.dependent() if n.Class() == 'Dot' and n.knob('parent')])!=0:
        nuke.message('{} is already a parent'.format(selected.name()))
        return

    if selected.knob('parent'):
        nuke.message('This is already a parent')
        return

    # p = nuke.Panel('Create Parent')
    # line_name = 'ParentName for: {}'.format(selected.name())
    # p.addSingleLineInput(line_name,'')
    # p.addRGBColorChip('Color', 0)
    # ret = p.show()

    # parentName = p.value(line_name)
    # colorVal = p.value('Color')
    parentName = nuke.getInput('ParentName for: {}'.format(selected.name()),'')
    parentKnob = nuke.Text_Knob('parent', 'parent')

    if parentName == None:
        return False

    if parentName == '':
        nuke.message('No parent name given.')
        return False

    elif selected.Class() == 'Dot':
        if selected.knob('child'):
            nuke.message("Error:It's a child.")
        else:
            nuke.selectedNode().knob('label').setValue('[value name]')
            nuke.selectedNode().knob('name').setValue(parentName)
            nuke.selectedNode().knob('tile_color').setValue(0)
            nuke.selectedNode().knob('note_font_size').setValue(FONT_SIZE)
            if nuke.selectedNode().knob('parent'):
                pass
            else:
                nuke.selectedNode().addKnob(parentKnob)

    else:
        newDot = nuke.createNode('Dot', inpanel=False)
        newDot.setXpos(selected.xpos()+int(selected.screenWidth()/2-5))
        newDot.setYpos(selected.ypos()+DISTANCE_FROM_NODE)
        newDot.knob('label').setValue('[value name]')
        newDot.knob('name').setValue(parentName)
        newDot.knob('tile_color').setValue(0)
        newDot.knob('note_font_size').setValue(FONT_SIZE)
        newDot.addKnob(parentKnob)

def dDotConnect():
    dotList = []
    for node in nuke.allNodes('Dot'):
        if node.knob('parent'):
            dotList.append(node.name())

    dotList.sort()
    p = nuke.Panel('Parent Dot List')
    p.addEnumerationPulldown('Parent',' '.join(dotList))
    ret = p.show()
    if p.value('Parent') != None:
        selectedParent = p.value('Parent')
    else:
        return False
    parent = nuke.toNode(selectedParent)
    selectedNodes = nuke.selectedNodes()
    childKnob = nuke.Text_Knob('child', 'child')

    if len( selectedNodes ) !=0:
        for n in selectedNodes:
            if  n.knob('parent'):
                pass
            elif n.Class() != 'Dot':
                pass
            else:
                n.connectInput(0, parent)
                n.knob('label').setValue(selectedParent)
                n.knob('tile_color').setValue(0)
                n.knob('hide_input').setValue(True)
                n.knob('note_font').setValue('italic')
                n.knob('updateUI').setValue(UPDATE_UI)
                n.knob('note_font_size').setValue(FONT_SIZE-10)
                parentColor = n.input(0).knob('note_font_color').getValue()
                parentColor = int(parentColor)
                n.knob('note_font_color').setValue(parentColor)
                childKnob = nuke.Text_Knob('child', 'child')
                if n.knob('child'):
                    pass
                elif n.knob('parent'):
                    pass
                elif n.Class() != 'Dot':
                    pass
                else:
                    n.addKnob(childKnob)
    else:
        nuke.createNode("Dot", inpanel=False).connectInput(0, parent)
        nuke.selectedNode().knob('label').setValue(selectedParent)
        nuke.selectedNode().knob('tile_color').setValue(0)
        nuke.selectedNode().knob('hide_input').setValue(True)
        nuke.selectedNode().knob('note_font').setValue('italic')
        nuke.selectedNode().knob('note_font_size').setValue(FONT_SIZE-10)
        nuke.selectedNode().knob('updateUI').setValue(UPDATE_UI)
        nuke.selectedNode().addKnob(childKnob)
        parentColor = nuke.selectedNode().input(0).knob('note_font_color').getValue()
        parentColor = int(parentColor)
        nuke.selectedNode().knob('note_font_color').setValue(parentColor)

def dDotConnectSelected():
    selectedNodes = nuke.selectedNodes()
    parent = selectedNodes[0]
    children = selectedNodes[1:]
    parentName = selectedNodes[0]['name'].getValue()

    for n in children:
        if  n.knob('parent'):
            pass
        elif n.Class() != 'Dot':
            pass
        else:
            n.connectInput(0, parent)
            n.knob('label').setValue(parentName)
            n.knob('tile_color').setValue(0)
            n.knob('hide_input').setValue(True)
            n.knob('note_font').setValue('italic')
            n.knob('note_font_size').setValue(FONT_SIZE-10)
            parentColor = n.input(0).knob('note_font_color').getValue()
            parentColor = int(parentColor)
            n.knob('note_font_color').setValue(parentColor)
        if n.knob('child'):
            pass
        elif n.knob('parent'):
            pass
        elif n.Class() != 'Dot':
            pass
        else:
            childKnob = nuke.Text_Knob('child', 'child')
            n.addKnob(childKnob)

def dDotCheckInput():
    brokenConnections = []
    for d in nuke.allNodes('Dot'):
        if d.input(0) == None:
            d['tile_color'].setValue(4278190335)
            brokenConnections.append(d.knob('name').getValue())
        else:
            if d.knob('child'):
                childLabel = d.knob('label').getValue()
                parentName = d.input(0).knob('name').getValue()
                if childLabel == parentName:
                    d['tile_color'].setValue(0)
                else:
                    d['tile_color'].setValue(4278190335)
                    brokenConnections.append(d.knob('name').getValue())
            else:
                d['tile_color'].setValue(0)
    if len(brokenConnections) > 0:
        brokenConnections.sort()
        nuke.message('%s connection(s) broken: \n %s' % (len(brokenConnections), brokenConnections))

def dDotAutoConnect():

    for d in nuke.selectedNodes('Dot'):
        if d.knob('child'):
            childLabel = d.knob('label').getValue()
            parent = nuke.toNode(childLabel)
            try:
                parentColor = parent.knob('note_font_color').getValue()
                parentColor = int(parentColor)
            except:
                parentColor = 4278190335
            if d.input(0) == None:
                d.connectInput(0, parent)
                d['tile_color'].setValue(0)
                d.knob('note_font_size').setValue(FONT_SIZE-10)
                d.knob('note_font_color').setValue(parentColor)
            else:
                parentName = d.input(0).knob('name').getValue()
                if childLabel != parentName:
                    d.connectInput(0, parent)
                    d['tile_color'].setValue(0)
                    d.knob('note_font_size').setValue(FONT_SIZE-10)
                    d.knob('note_font_color').setValue(parentColor)
    dDotCheckInput()

def dDotShowChildren():

    selectedNode = nuke.selectedNode()
    dependentNodes = selectedNode.dependent()
    selectedNode.setSelected(False)
    for depnd in dependentNodes:
        depnd.setSelected(True)

def dDotToggleConnectionsVisibility():
    selectedNode = nuke.selectedNode()
    dependentNodes = selectedNode.dependent()
    for depnd in dependentNodes:
        currentState = depnd.knob('hide_input').getValue()
        depnd.knob('hide_input').setValue(not currentState)

def dDotRollDownNameChange():
     selectedNode = nuke.selectedNode()
     selectedNodeName = selectedNode.knob('name').getValue()
     parentColor = selectedNode.knob('note_font_color').getValue()
     parentColor = int(parentColor)
     if selectedNode.Class() == 'Dot':
        if selectedNode.knob('parent'):
            dependentNodes = selectedNode.dependent()
            for depnd in dependentNodes:
                if depnd.knob('child'):
                    depnd.knob('label').setValue(selectedNodeName)
                    depnd.knob('note_font_color').setValue(parentColor)
            dDotCheckInput()

def dDotGrabParentName():
    for n in nuke.selectedNodes('Dot'):
        if n.knob('child'):
            parentName = n.input(0).knob('name').getValue()
            parentNameNoNumbers = filter(lambda x: x.isalpha(), parentName)
            parentColor = n.input(0).knob('note_font_color').getValue()
            parentColor = int(parentColor)
            childName = n.knob('label').getValue()
            childNameNoNumbers = filter(lambda x: x.isalpha(), childName)
            if childNameNoNumbers.startswith(parentNameNoNumbers):
                n.knob('label').setValue(parentName)
                n.knob('note_font_color').setValue(parentColor)

    dDotCheckInput()

def dDotSelectChildren():
    childName = nuke.getInput('select child nodes labeled:','')
    for n in nuke.allNodes('Dot'):
        if n.knob('child') and n.knob('label'). getValue() == childName:
            n.setSelected(True)

def unselect_all():
    for node in nuke.selectedNodes():
        node.setSelected(False)

def dDotStart():
    sel_list = nuke.selectedNodes()
    if len(sel_list) == 0:
        dDotConnect()
    elif sel_list[0].knob('child'):
        dDotAutoConnect()
    else:
        for node in sel_list:
            unselect_all()
            node.setSelected(True)
            dDotParent()




# Add backpack
toolbar = nuke.menu('Nodes')
backpackToolbar = toolbar.addMenu('dDot')

#dDotStart
backpackToolbar.addCommand("dDot", "dDot.dDotStart()", "shift+D")

#dDotConnectSelected
backpackToolbar.addCommand("dDotConnectSelected", "dDot.dDotConnectSelected()", "ctrl+,")

#dDotCheckInput
backpackToolbar.addCommand("dDotCheckInput", "dDot.dDotCheckInput()", "ctrl+shift+,")

#dDotAutoConnect
backpackToolbar.addCommand("dDotAutoConnect", "dDot.dDotAutoConnect()", "ctrl+shift+.")

#dDotShowChildren
backpackToolbar.addCommand("dDotShowChildren", "dDot.dDotShowChildren()", "alt+,")

#dDotToggleConnectionsVisibility
backpackToolbar.addCommand("dDotToggleConnectionsVisibility", "dDot.dDotToggleConnectionsVisibility()", "alt+.")

#dDotRollDownNameChange
backpackToolbar.addCommand("dDotRollDownNameChange", "dDot.dDotRollDownNameChange()","alt+shift+,")

#dDotGrabParentName
backpackToolbar.addCommand("dDotGrabParentName", "dDot.dDotGrabParentName()","alt+shift+.")

#dDotSelectChildren
backpackToolbar.addCommand("dDotSelectChildren", "dDot.dDotSelectChildren()")
