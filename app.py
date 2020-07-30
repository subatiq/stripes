# pylint: disable=unused-wildcard-import
from sprise.wildcard import *


sprise_red = "#ed462f"
sprise_green = "#1aad84"


stacks_tests = VStack(
        Text("It's sprise")
                .foregroundColor('white')
                .font('h2')
                .upper(),
        Text("""It's a neat declarative extention 
        for Flask so you don't waste time on building 
        templates. More features are coming!""")
                .size(width=400)
                .foregroundColor(sprise_red),
        ZStack(
                Rectangle()
                        .fill("#222222")
                        .size(400, 200)
                        .Text("Under this circle")
                        .upper()
                        .foregroundColor(sprise_red)
                        .font('h1'),
                
                Rectangle()
                        .fill(sprise_red)
                        .cornersRadius(80)
                        .size(82, 82)
                        .Text("ZStack works!")
                        .foregroundColor("#333333")
                        .size(width=60)
                        .font('b')
        ),
        ZStack(
                Rectangle()
                        .fill(sprise_green)
                        .size(400, 200),
                VStack(
                        Text("VStacks working like a charm!")
                        .foregroundColor('#333333')
                        .font('h2'),
                        
                HStack(
                        Rectangle()
                        .fill("#333333")
                        .size(150, 70)
                        .Text("HStacks")
                        .font('h4')
                        .foregroundColor('white'),

                        Rectangle()
                        .fill("#333333")
                        .size(150, 70)
                        .Text("Also work")
                        .font('h4')
                        .foregroundColor('white'),
                )
                )
        ),

)


body = App(stacks_tests).fill("#111111")
