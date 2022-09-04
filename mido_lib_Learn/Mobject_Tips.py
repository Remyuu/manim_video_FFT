'''
2022-7-26 
Learn <manim.mobject.geometry.tips>
'''
from manim import *

#0 Arrow
class ArrowSetTest(Scene):
    def construct(self):
        arrow01 = Arrow(start=[-2,3,0],end=[2,3,0],color = BLUE)
        arrow02 = Arrow(start=[-2,2,0],end=[2,2,0],tip_shape=ArrowSquareTip)
        arrow03 = Arrow(start=[-2,1,0],end=[2,1,0],tip_shape=ArrowTip)
        arrow04 = Arrow(start=[-2,0,0],end=[2,0,0],tip_shape=ArrowCircleFilledTip)
        arrow05 = Arrow(start=[-2,-1,0],end=[2,-1,0],tip_shape=ArrowCircleTip)
        self.add(arrow01,arrow02,arrow03,arrow04,arrow05)

#1 ArrowTip
class MT(Scene):
    def construct(self):
        AT = ArrowTip().move_to(UL)
        AST = ArrowSquareTip().next_to(AT,RIGHT)
    

        self.add(AT,AST)








#3





#