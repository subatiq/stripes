# pylint: disable=unused-wildcard-import
from splice.wildcard import *

splice_red = "#ed462f"
splice_green = "#1aad84"

stacks_tests = VStack(
        Text("It's splice")
                .foregroundColor('white')
                .font('h2')
                .upper(),
        Text("""It's a neat declarative extention 
        for Flask so you don't waste time on building 
        templates. More features are coming!""")
                .size(width=400)
                .foregroundColor(splice_red),
        ZStack(
                Rectangle()
                        .fill("#222222")
                        .size(400, 200)
                        .Text("Under this circle")
                        .upper()
                        .foregroundColor(splice_red)
                        .font('h1'),
                
                Rectangle()
                        .fill(splice_red)
                        .cornersRadius(80)
                        .size(82, 82)
                        .Text("ZStack works!")
                        .foregroundColor("#333333")
                        .size(width=60)
                        .font('b')
        ),
        ZStack(
                Rectangle()
                        .fill(splice_green)
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
