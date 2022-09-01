from manim import *

class AnimationTransform(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.add(square)
        self.play(Transform(square, circle))
        square.generate_target()
        square.target.move_to(2*UP)
        self.play(MoveToTarget(square))

class CreateCircle2(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(PINK,opacity=0.5)
        circle.generate_target()
        circle.target.shift(2*UP)
        self.play(Create(circle))
        self.play(MoveToTarget(circle))
        self.wait(0.3)

class Curve3(Scene):
    def construct(self):
#initial value
        A = 1
        B = 1
        C = 0

        dn_kwargs = {"unit": r"^\circ"}
        D_A = DecimalNumber(A,**dn_kwargs)
        D_B = DecimalNumber(B,**dn_kwargs)
        D_C = DecimalNumber(C,**dn_kwargs)

        pc = self.get_param_func(A,B,C)

# updater setting
        upfunc =lambda mob: mob.become(
                self.get_param_func(
                    D_A.get_value(),
                    D_B.get_value(),
                    D_C.get_value()
                ).move_to(pc)
            )
        pc.add_updater(upfunc)

# initial position
        pc.shift(LEFT*3)
#First part
        self.add(pc)    
        self.play(
            ChangeDecimalToValue(D_B,15),
            run_time=2,
            rate_func=linear,
        )
        self.wait(0.3)


# remove updater temporary
        pc.remove_updater(upfunc)
# move the curve, without the influence from updater
        self.play(pc.animate.shift(RIGHT*6),run_time=1)
# add the updater again      
        pc.add_updater(upfunc)


# Second part        
        self.play(
            ChangeDecimalToValue(D_A,10),
            run_time=2,
            rate_func=linear,
        )


# define the curve
    def get_param_func(self, a, b, c):
        pc = ParametricFunction(
            lambda t: np.array([
                np.cos(a * t) + np.cos(b * t) / 2 + np.sin(c * t) / 3,
                np.sin(a * t) + np.sin(b * t) / 2 + np.cos(c * t) / 3,
                0
            ]),
            t_range=[0,2*PI,0.007],
            fill_opacity=0
        ).scale(2)\
        .set_color(color=[RED,YELLOW,BLUE,RED])
        return pc
        
class God_Of_Test(Scene):
    def construct(self):
        A = 1
        D_A = DecimalNumber(A)
        circle = Circle(radius=D_A.get_value())
        
        updatefunc = lambda obj : obj.become(Circle(radius=D_A.get_value()))
        circle.add_updater(updatefunc)
        self.play(ChangeDecimalToValue(D_A,1.5))


class test(Scene):
    def construct(self):
        A = 1
        D_A = DecimalNumber(A)
        square = Square(side_length=D_A.get_value())

        #upfunc = lambda obj : obj.become(Square(side_length=D_A.get_value()))
        upfunc = lambda obj : obj.become(Square(side_length=D_A.get_value())).shift(LEFT/5)

        square.add_updater(upfunc)
        self.add(square)

        self.play(square.animate.shift(LEFT))

        self.play(ChangeDecimalToValue(D_A,5))
    
tex = MathTex(r'\prod_{i=0}^{\infty}x_i=0',r'x123')

for part in tex:
    if part.get_tex_string == r'\infty':
        print("张杰是傻逼")
    if part.get_tex_string == r'\prod_{i=0}^{\infty}x_i=0':
        print("陈凯雪是脑瘫")


class TestBecome(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        #tex = MathTex(r'\sigma_{i=0}^{inf}x_i=0')

        tex = MathTex(r'\prod_{i=0}^{\infty}x_i=0',r'x123')

        
        self.add(tex[0])
        self.add(tex[1])
        
        self.add(circle)
        self.wait()
        self.play(Write(tex))
        circle.become(square).shift(LEFT)
        self.wait()







class Con(Scene):
    def construct(self):
        func = lambda x: np.sin(x[0])+np.cos(x[1])
        stream_lines = StreamLines(func)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True,flow_speed=2)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)




'''

https://docs.manim.community/en/v0.16.0.post0/reference/manim.mobject.mobject.Mobject.html?highlight=become#manim.mobject.mobject.Mobject.become

'''
       




