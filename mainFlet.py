from flet import *
from checbox import CustomCheckBox

def main(page: Page):
    
    PV = '#02133e'
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5,0.5],
                colors=['#00000000', PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(alignment='center',
                            controls=[
                                Container(
                                    bgcolor=PV,
                                    width=90, height=90,
                                    border_radius=50,
                                    content=Container(bgcolor=FG,
                                    height=80, width=80,
                                    border_radius=40,
                                    content=CircleAvatar(opacity=0.8, foreground_image_url='https://scontent.cdninstagram.com/v/t51.2885-19/301036118_5722804267764730_1122446163817639218_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=110&_nc_ohc=vlDsmlagLg0AX9-G4AS&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfBPAnUcn0EmOA5J6WlvmuxSyuBiwqt7bSEH9OGQtLknsA&oe=645B9E4C&_nc_sid=978cb9'))
                                )
                            ])
            )
        ]
    )

    def shrink(e):
        page2.controls[0].width = 120
        page2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        page2.controls[0].border_radius=border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page2.update()

    def restore(e):
        page2.controls[0].width = 400
        page2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right)
        page2.update()

    createTaskView = Container(
        content=Container(on_click= lambda _: page.go('/'), 
                          height=40, width=40,
                        content=Text('Get back to main site '))
    )

    tasks = Column(
        height=400,
        scroll='auto',
        # controls=[
        #     Container(height=50, width=300, bgcolor='red'),
        #     Container(height=50, width=300, bgcolor='red'),
        #     Container(height=50, width=300, bgcolor='red'),
        #     Container(height=50, width=300, bgcolor='red'),
        #     ]
    )

    categoriesMk1  = ['Penkkipunnerrus', 'Flyes käsipainoilla', 'Ranskalainen punnerrus käsipainolla', 
                   'Pystypunnerrus käsipainoilla', 'Vipunosto sivulle käsipainoilla',
                   'Hauiskääntö käsipainoilla', 'Ylätalja', 'Alatalja', 'Leuanveto', 'Leaunveto kuminauhalla avustettuna']

    for i in range(10):
        tasks.controls.append(
            Container(height=70, 
                      width=400, 
                      bgcolor='yellow', 
                      border_radius= 25,
                      animate=animation.Animation(600, AnimationCurve.DECELERATE),
                      animate_scale=animation.Animation(400, curve='decelerate'),
                      padding=padding.only(left=20, top=25),
                      content=CustomCheckBox(
                        color = PINK,
                        label='Tee jotain',                        
                      )),
        )

    categoriesCard= Row(
        scroll='auto'
                        )
    
    categories  = ['4 viikon valmennus', '8 viikon valmennus', '12 viikon valmennus', '16 viikon valmennus']
    for i, category in enumerate(categories):
        categoriesCard.controls.append(
            Container(
                width=170,
                height=110,
                bgcolor='yellow',
                border_radius=20,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 tehtävää', color='black'),
                        Text(category, color= 'black'),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i*30),
                            content=Container(
                                bgcolor=PV
                            )
                        )
                    ]
                )
            )
        )

    firsPageContents= Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            on_click= lambda e: shrink(e),
                            content=Icon(
                                icons.MENU
                            )),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                Container(height=20),
                Text(
                    value= 'POLIISIKOULUVALMENNUS'
                ),
                Container(height= 20),
                Text(
                    value='Valmennukset'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categoriesCard
                ),
                Container(height=20),
                Text('Tämän valmennuksen tehtävät'),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(bottom=2, right=20,
                            icon = icons.ADD, on_click=lambda _: page.go
                            ('/createTask')
                        )
                    ]
                )
            ]
        )
    )
    page1 = Container(
        width=400,
        height=850,
        bgcolor=PV,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        
        content=Column(
            controls=[

                Row(
                    alignment='end',
                    controls=[
                    Container(
                    border_radius=25,
                    padding=padding.only(top=13, left=13),
                    height=50, 
                    width=50,
                    border= border.all(color='white', width=1),
                    on_click=lambda e: restore(e),
                    content=Text('<')
                )
                    ]
                ),
                Container(height=20),
                circle,
                Text('Poliisi\nPate', size=32, weight='bold'),
                Container(height=20),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color='white60'),
                    Text('Templates', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL, color='white60'),
                    Text('Categories', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED, color='white60'),
                    Text('Analytics', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                ]),
                    Image(src=f"/logo.jpeg",
                      width=300,
                      height=200
                      ),
            ]
        )
    )
    page2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=PV,
                border_radius=35,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='declerate'),
                padding=padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        firsPageContents
                    ]
                )
            )
        ]
    )

    container = Container(
        width=400, 
        height=850, 
        bgcolor=PV, 
        border_radius=35,
        content=Stack(
            controls=[
                page1,
                page2
            ]
        )
    )
    pages = {
        '/':View(
                '/',
                [
                    container
                ],
        ),
        '/createTask': View(
                    '/createTask',
                    [
                        createTaskView
                    ],
        )
    }
    
    def routeChange(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(container)
    page.on_route_change = routeChange
    page.go(page.route)

#path
app(target=main, assets_dir='.vscode')