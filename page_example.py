# pylint: disable=unused-wildcard-import
from sprise.wildcard import *


sprise_red = "#ed462f"
sprise_green = "#1aad84"


stacks_tests = VStack(
        Text("It's sprise")
                .Color('white')
                .Font('h2')
                .Upper(),
        Text("""It's a neat declarative extention 
        for Flask so you don't waste time on building 
        templates. More features are coming!""")
                .Size(width=400)
                .Color(sprise_red),
        ZStack(
                Rectangle()
                        .Color("#222222")
                        .Size(400, 200)
                        .Text("Under this circle")
                        .Upper()
                        .Color(sprise_red)
                        .Font('h1'),
                
                Rectangle()
                        .Color(sprise_red)
                        .CornersRadius(80)
                        .Size(82, 82)
                        .Text("ZStack works!")
                        .Color("#333333")
                        .Size(width=60)
                        .Font('b')
        ),
        ZStack(
                Rectangle()
                        .Color(sprise_green)
                        .Size(400, 200),
                VStack(
                        Text("VStacks working like a charm!")
                        .Color('#333333')
                        .Font('h2'),
                        
                HStack(
                        Rectangle()
                        .Color("#333333")
                        .Size(150, 70)
                        .Text("HStacks")
                        .Font('h4')
                        .Color('white'),

                        Rectangle()
                        .Color("#333333")
                        .Size(150, 70)
                        .Text("Also work")
                        .Font('h4')
                        .Color('white'),
                )
                )
        ),

)


body = App(stacks_tests).Color("#111111")
