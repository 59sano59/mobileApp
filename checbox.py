from flet import *


class CustomCheckBox(UserControl):

    def __init__(self, color, label='', selection_fill='#183588', size=25, stroke_width=2, animation=None, checked=False, font_size=17, pressed=None):
        super().__init__()
        self.selectionFill = selection_fill
        self.color = color
        self.label = label
        self.size = size
        self.strokeWidth = stroke_width
        self.animation = animation
        self.checked = checked
        self.fontSize = font_size
        self.pressed = pressed

    def _checked(self):
        self.checkBox = Container(
            animate=self.animation,
            width = self.size, height=self.size,
            border_radius=(self.size/2) + 5,
            bgcolor=self.CHECKED,
            content= Icon(icons.CHECK_ROUNDED, size=15,),)
        return self.checkBox
    
    def _unchecked(self):
        self.checkBox = Container(
            animate=self.animation,
            width=self.size,height=self.size,
            border_radius=(self.size/2)+5,
            bgcolor=None,
            border = border.all(color=self.color,width=self.strokeWidth),
            content=Container(),)   
        return self.checkBox

    def build(self):
        self.PV = '02133e'
        self.BG = '#041955'
        self.FG = '#3450a1'
        self.PINK = '#eb06ff'
        self.CHECKED = '#183588'

        if self.checked == True:  
            return Column(controls=[
                Container(
                on_click = lambda e: self.checkedCheck(e),
                content=Row(
                    controls=[
                self._checked(),
                Text(self.label,
                        font_family='poppins',
                        size=self.fontSize,
                        weight=FontWeight.W_300,),
            ]))
        ])
        
        else:  
            return Column(
            controls=[
            Container(on_click = lambda e: self.checkedCheck(e),
            content=Row(
                controls=[
            self._unchecked(),
            Text(self.label,
                    font_family='poppins',
                    size=self.fontSize,
                    weight=FontWeight.W_300,
                    color='Black'),
            ]))
        ])

    def checkedCheck(self,e):
        print(self.checked)
        if self.checked == False:
            self.checked = True
            self.checkBox.border = None
            self.checkBox.bgcolor = self.CHECKED
            self.checkBox.content = Icon(icons.CHECK_ROUNDED,size=15,)
            self.update()

            
        elif self.checked == True:
            self.checked = False
            self.checkBox.bgcolor = None
            self.checkBox.border = border.all(color=self.color,width=self.strokeWidth)
            self.checkBox.content.visible = False
            self.update()
            

        if self.pressed:
            self.run()       
    def isChecked(self):
        return self.checked

    def run(self,*args):
        self.pressed(args)