import maya.cmds as cmds

class showUI():
    
    def Transx(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.translatex)
        cmds.setParent('..')
    
    def Transy(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.translatey)
        cmds.setParent('..')
        
    def Transz(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.translatez)
        cmds.setParent('..')
        
    def Rotx(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.rotatex)
        cmds.setParent('..')
        
    def Roty(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.rotatey)
        cmds.setParent('..')
        
    def Rotz(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.rotatez)
        cmds.setParent('..')
        
    def Scalx(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.scalex)
        cmds.setParent('..')
        
    def Scaly(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.scaley)
        cmds.setParent('..')
    
    def Scalz(self, labelText):
        cmds.rowLayout(numberOfColumns=2)
        name = cmds.text(label=labelText)
        cmds.button(label='OK', command=self.scalez)
        cmds.setParent('..')
    
    def __init__(self):
        self.win = cmds.window('Translate, Rotate, Scale', widthHeight=(300,300))
        cmds.columnLayout()
        
        Translate_x = self.Transx('Translate x:')
        Translate_y = self.Transy('Translate y:')
        Translate_z = self.Transz('Translate x:')
        Rotate_x = self.Rotx('Rotate x:')
        Rotate_y = self.Roty('Rotate y:')
        Rotate_z = self.Rotz('Rotate z:')
        Scale_x = self.Scalx('Scale x:')
        Scale_y = self.Scaly('Scale y:')
        Scale_z = self.Scalz('Scale z:')
        
        cmds.showWindow(self.win)
        
    def translatex(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.move(num, 0, 0)
        
    def translatey(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.move(0, num, 0)
        
    def translatez(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.move(0, 0, num)
        
    def rotatex(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.rotate(num, 0, 0)
        
    def rotatey(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.rotate(0, num, 0)
        
    def rotatez(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.rotate(0,0, num)
        
    def scalex(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.scale(num,0,0)
        
    def scaley(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.rotate(0,num,0)
        
    def scalez(self, *args):
        enterInput = input('Enter translation amount: ')
        num = eval(enterInput)
        cmds.rotate(0,0, num)
        
def objectSelection(obj):
    shapeType = cmds.listRelatives(obj, shapes=True)
    nodeType = cmds.nodeType(shapeType)
    
    if (nodeType == 'mesh'):
        return True
        
    return False
    
def changeSelection():
    selectedObj = cmds.ls(selection=True)
    
    if len(selectedObj) < 1:
        cmds.error('Please select an object')
    
    lastSelected = selectedObj[-1]
    isPolygon = objectSelection(lastSelected)
    
    if (isPolygon):
        showUI()
    else:
        cmds.error('Please select an object')

changeSelection()