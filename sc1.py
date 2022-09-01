
from manim import *
#导入manim命名空间
import math
import sympy


#这是一个最基本的manim结构，类名叫做BaseFrame，传入一个场景Scene，并且包含一个construct方法，传入self
class BaseFrame(Scene):
    def construct(self):
        self.wait()


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # 创建了一个Circle对象：circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class ThreePar(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED, opacity=0.6)

        star = Star()
        star.set_fill(BLUE, opacity=0.4)
        
        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        circle.next_to(star, LEFT, buff=0.5)
        square.next_to(star, RIGHT, buff=0.5)

        #占用1秒的时长，
        #如果你的Create方法是在play里面的，他就会占用一秒钟的时间去展示创建对象的过程
        self.add(star)
        self.add(circle)#无意义的，后面的Create(circle)会创建，系统会删除次代码
        self.play(Create(circle),Create(square))
        self.wait(1)
        self.remove(star)
        self.wait(1)

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

#Play_Scripts_Start
        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # 旋转图形，参数是弧度制
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
#Play_Scripts_End


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()



#默认情况下，对象会生成在屏幕中心点
class Learn01_move(Scene):
    def construct(self):
        circle = Circle()
        triangle = Triangle()

        self.add(circle,triangle)
        print ("移动")
        self.wait(1)

        circle.shift(LEFT*3 + UP*2)
            #瞬间移动,LEFT,UP是单位方向向量
            #以自身为参考
        self.wait(1)

        triangle.next_to(circle,RIGHT)
            #瞬间移动
            #以传入对象为参考
        self.wait(1)

        circle.move_to(DOWN)
            #瞬间移动
            #以屏幕中心为参考
        self.wait(1)

        triangle.align_to(circle,DOWN)
            #瞬间移动
            #以传入对象的假想边界作为调整
            #传入DOWN(0,-1)，那么物体的纵坐标就会"对其"对象的下边界
                #这个假想的边界一般以物体以中心为原点的第二象限区域
        self.wait(1)

class Learn02_beauty(Scene):
    def construct(self):

        circle = Circle().shift(LEFT*2)
        star = Star().shift(RIGHT*2)
        self.play(Create(circle), Create(star))
        self.wait(1)

        #set_fill()  改变图形的内部
        #set_stroke()改变图形的边框
        star.set_stroke(color=YELLOW, width=20)
        circle.set_stroke(color=BLUE, width=20)
        star.set_fill(YELLOW, opacity=0.7)
        circle.set_fill(YELLOW, opacity=0.7)

        
        self.wait(1)
        
class Learn03_animations(Scene):
    def construct(self):
        star = Star()
        self.play(FadeIn(star))#渐入特效
        #self.play(FadeIn(star),run_time = 5)可以设置时间
        self.wait(1)
        self.play(Rotate(star, 2*PI))#旋转特效
        self.wait(1)
        self.play(FadeOut(star))#渐出特效

#animate方法
    #这样就可以
class Learn04_animateMethod(Scene):
    def construct(self):
        star = Star()
        self.play(star.animate.set_fill(YELLOW, opacity=0.4))
        self.wait(1)
        self.play(star.animate.set_fill(WHITE))
        self.wait(1)

        #也可以同时进行animate方法
        self.play(
            star.animate
            .shift(UP+LEFT)
            .rotate(2/3*PI)
            .set_fill(RED)
        )
        self.wait(1)

        #也可以在play中添加run_time参数，修改动画持续时间
        self.play(
            star.animate
            .shift(-UP-LEFT)
            .rotate(2/3*PI)
            .set_fill(BLUE)
            ,run_time = 5
        )
        self.wait(1)


#创建自定义动画
#重写interpolate_mobject()方法
class Countqq(Animation):
    #kwargs是可变参数，此处暂时用不上
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs):
        # Pass number as the mobject of the animation
        #这个是构造方法，使用到我们这个Countqq这个类的时候就会自动把参数传入此方法中
        #self在构造的时候不需要传递
        super().__init__(number, **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float):
        # Set value of DecimalNumber according to alpha
        #这一行是增长的 这个是manim系统内部调用的，我们就不管他了。
        value = self.start + (alpha * (self.end - self.start)) 
        self.mobject.set_value(value)
class Learn05_CountingScene(Scene):
    def construct(self):
        #创建一个Decimal数字，设置颜色，缩放比
        number = DecimalNumber().set_color(BLUE).scale(5).move_to(LEFT)
        #添加一个定时更新器,ORIGIN相当于[0,0,0],移动到屏幕中心点
        #匿名函数lambda构建方法 lambda XXX:___
        number.add_updater(lambda number: number)

        self.add(number)

        self.wait(1)

        # Play the Count Animation to count from 0 to 314 in 4 seconds
        #Count传入数字范围从0到100，设置持续时间4秒，线性增长
        #play可以传递一个Animation类型的参数，用于动画的播放，参数可设置：run_time,rate_func there_and_back
        self.play(Countqq(number, 0, 100), run_time=4, rate_func=linear)
        
        self.wait(1)

class Learn06_MobjectExample(Scene):
    def construct(self):
        p1= [-1,-1,0]
        p2= [1,-1,0]
        p3= [1,1,0]
        p4= [-1,1,0]
        #append_points()方法是增加节点，连成折线。
            #方法中传入起点与终点的Line的points
        a = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        #寻找线的开头&结尾&重心 get_start get_end get_center
        point_start= a.get_start()
        point_end  = a.get_end()
        point_center = a.get_center()
        #这个self.mobjects[-1]是指上一个add的对象
        #np是numpy的意思，manim中，numpy as np，即数学库
            #UR指的是UP+RIGHT，在边界的右上角
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))
        #还可以get各种位置 get_bottom get_center point_from_proportion是线的中点
        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)

#测试，不用管这里
class Learn07_MobjectTest(Scene):
    def construct(self):
        p1=[-1,-1,0]
        p2=[1,1,0]
        p3=[-1,1,0]

        a =Line(p1,p2).append_points(Line(p2,p3).points)
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)


class Learn08_Transform(Scene):
    def construct(self):
        #设置摄像机的背景颜色，即屏幕背景
        self.camera.background_color = GREEN_A
        #创建一个正方形
        m1 = Circle().set_color(RED)
        #创建一个矩形，旋转一定角度
        m2 = Rectangle().set_color(RED).rotate(PI/6)
        #转变图形
        self.play(Transform(m1,m2))
        #会直接把m1变成m2的外观，m2不会显示


class Test_Transform(Scene):
    def construct(self):
        #渐变色
        mobj1 = Text(f"早上好，我是？", font_size=93,t2g={'[1:-1]': (RED,GREEN),}).shift(UP*2)
        self.play(FadeIn(mobj1),run_time=1)
        mobj2 = Text(f"傻逼！", font_size=256).next_to(self.mobjects[-1],DOWN).set_color(BLUE)
        self.play(Transform(mobj1,mobj2),run_time=2)

class Learn09_roll(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a= Square().set_color(BLUE).shift(RIGHT)
        m2b= Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)


#隔离分组字串
class Learn10_HelloLaTeX(Scene):
    def construct(self):

        tex = MathTex(
            r"\sum_{i=0}^{n}{\frac{x^n}{n!}}"
        )
        text = Text('指数函数的泰勒展开.',font_size=32,
            t2c={"指数函数": BLUE, "泰勒": ORANGE}).next_to(tex,UP)
        #for x in text:
            #x.set_color(random_color())
            #x.set_color(random_bright_color())
        tex2 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
            ,substrings_to_isolate="x"#隔离x作为字串，后面就可以单独渲染它的颜色了
        ).next_to(tex,DOWN)
        tex2.set_color_by_tex("x", YELLOW)
        self.add(tex,text,tex2)


#坐标轴的显示
class Learn11_Plane(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane(
        #关于直角坐标的一些相关设置
            #坐标偏移
#x_range The [x_min, x_max, x_step]-10 10 1
#y_range The [y_min, y_max, y_step]-10 10 1
            x_range=[-10,10,1],
            y_range=[-10,10,1],
            #坐标缩放边界，默认是20
            x_length=20,
            y_length=20,
            background_line_style={
                "stroke_color":RED,
                "stroke_width":4,
                "stroke_opacity":0.6
            },
            #坐标密度
            faded_line_ratio=1,

            ).add_coordinates([0,1,2,3],[-1,0,1,2,3])
            #展示部分坐标标签

        self.play(FadeIn(numberplane),run_time=2)
        self.play(FadeOut(numberplane),run_time=1.5)

        #添加默认的坐标轴标签
        numberplane = PolarPlane().add_coordinates()

        self.play(FadeIn(numberplane),run_time=2)
        self.play(FadeOut(numberplane),run_time=1.5)

        #如果要使用3维坐标，则需要使用3d scene
        ax = ThreeDAxes()
        lab = ax.get_z_axis_label(Tex("$z$-label"))
        self.set_camera_orientation(phi=2*PI/5, theta=-PI/5)
        self.add(ax, lab).wait(1)

class Learn12_indication(Scene):
    def construct(self):
        #波浪文字
        testStr = MathTex(r"WaveWavexxxxyyyyzzzz").scale(2)
        #ApplyWave
        self.play(ApplyWave(testStr))
        self.play(ApplyWave(
            testStr,
            direction=RIGHT,
            time_width=0.5,
            amplitude=0.3
        ))
        self.play(ApplyWave(
            testStr,
            rate_func=linear,
            ripples=4
        ))
        #强调，划重点
        self.play(Circumscribe(testStr))
        self.play(Circumscribe(testStr, Circle))
        self.play(Circumscribe(testStr, fade_out=True))
        self.play(Circumscribe(testStr, time_width=2))
        self.play(Circumscribe(testStr, Circle, True))
        #高亮 Indicate
        self.play(Indicate(testStr))
        self.wait()
        #放大、摇晃Wiggle
        self.play(Wiggle(testStr))
        self.wait()

class Learn13_ADD_UPDATE(Scene):
    def construct(self):
        text = Text("SomeThing")
        
        def anima(mobj):
            mobj.shift(UP*0.1)
        self.add(text)
        text.add_updater(anima)
        self.play(FadeIn(text))
        self.wait(5)


#TAU = 2 * math.pi


class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):#传进来的是label
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*2)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))



#实际例子1--Logo图案设计--#mathbb mathscr mathtt
class RemooLogo(Scene):
    def construct(self):
        self.add(NumberPlane())
        self.camera.background_color='#758a99'
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        MT_R = MathTex(r"\mathscr{R}", fill_color=logo_black)\
            .scale(7)\
            .shift(LEFT+UP)
        MT_ee = MathTex(r"\mathtt{E}", fill_color=logo_blue)\
            .scale(4)
        circle0 = Circle(color=GREEN_A, fill_opacity=0.7).shift(RIGHT)
        circle1 = Circle(color=logo_green, fill_opacity=1).shift(RIGHT*2)
        square = Square(color=YELLOW, fill_opacity=1)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(LEFT)
        logo = VGroup(triangle,square,circle0,circle1,MT_ee,MT_R)#order matters~
        logo.move_to(ORIGIN).scale(2)
        self.add(logo)

#实际例子2--微分、斜率示意
class DyAndDx(Scene):
    def construct(self):
        dot = Dot([-2, -1,0])
        dot2 = Dot([2, 1, 0])
        dot3 = Dot([2,-1,0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)

        #线变成括号{ -- Brace
        b1 = Brace(line)
        b1text = b1.get_tex("x_0+dx")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex(r"\sqrt{(dx)^2+(dy)^2}")
        b3 = Brace(line,direction=[1,0,0])
        b3text = b3.get_tex("y_0+dy")
        #self.add(line, dot, dot2, b1, b2, b3, b1text, b2text, b3text)
        sets = VGroup( dot, dot2, b1, b2, b3, b1text, b2text, b3text)
        self.play(FadeIn(line,shift=DOWN))
        for mobj in sets:
            self.play(Write(mobj),run_time=0.2)
        self.wait(1)
        
        
#实际例子3--向量-基础
class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()
        dot = Dot([0,0,0])
        arrow = Arrow([0,0,0],[2,2,0],buff = 0)
        origin_text = Text('(0.0,0.0)').next_to(dot,DOWN+RIGHT)
        tip_text = Text(f'({np.round(arrow.get_vector()[0])},{np.round(arrow.get_vector()[1])})').next_to(arrow,UP+RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)

#实际例子4-方框文字颜色
class RectangleSelected(Scene):
    def construct(self):
        rectangle = Rectangle(color = RED)
        text=Text("你好，我是remoo\n这里是manim学习笔记",
            t2c={"我是remoo":BLUE,"manim学习笔记":GREEN,},
            line_spacing=2)
        selectText = "remoo"
        print(selectText)
        rectangle.surround(text)
        group1 = VGroup(rectangle,text)
        self.play(Write(text))
        self.play(FadeIn(rectangle))
        self.wait(0.3)
        self.play(ApplyMethod(group1.scale,2))
        self.wait(0.2)
        self.play(ApplyMethod(group1.scale,0.5))
        self.wait(1)

class BooleanDevice(Scene):
    def construct(self):
        circle1 = Circle(
            radius=2,fill_opacity=0.5,color=BLUE,stroke_width=10
        ).move_to(LEFT*2.5)
        circle2 = Circle(
            radius=2,fill_opacity=0.5,color=YELLOW,stroke_width=10
        ).move_to(LEFT*0.5)
        group1 = VGroup(circle1,circle2)
        self.play(GrowFromCenter(group1))
        self.play(group1.animate.shift(LEFT))

        #求交集
        intersection = Intersection(circle1,circle2,color=GREEN,fill_opacity=0.8)
        Text_inter = Text("交集")
        self.play(intersection.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5),
            Text_inter.animate.move_to(RIGHT * 3 + UP * 2.5))
            
        #求并集
        union = Union(circle1, circle2, color=ORANGE, fill_opacity=0.8)
        Text_uni = Text("并集")
        self.play(union.animate.scale(0.25).move_to(RIGHT * 5 + UP),
            Text_uni.animate.move_to(RIGHT * 3 + UP))

        #求容斥
        union = Exclusion(circle1, circle2, color=PINK, fill_opacity=0.8)
        Text_uni = Text("容斥")
        self.play(union.animate.scale(0.25).move_to(RIGHT * 5 - UP),
            Text_uni.animate.move_to(RIGHT * 3 - UP))

        #求异
        union = Difference(circle1, circle2, color=RED, fill_opacity=0.8)
        Text_uni = Text("求异")
        self.play(union.animate.scale(0.25).move_to(RIGHT * 5 - UP * 2.5),
            Text_uni.animate.move_to(RIGHT * 3 - UP * 2.5))

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([1, 0, 0], [7, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=there_and_back)
        self.play(MoveAlongPath(dot, circle), run_time=1, rate_func=linear)
        #根据某一点旋转
        self.play(Rotating(dot, about_point=[4, 0, 0]), run_time=1.5)
        self.wait(1)


class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()




class ArrangeSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT+UP) for i in range(0,15)])
        s.shift(UP).set_color(BLUE)
        s2= s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s,s2)



class InvertSumobjectsExample(Scene):
    def construct(self):
        s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2 = s.copy()
        s2.invert()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))



class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))

class SumFuncG_p1(Scene):
    def construct(self):
        P1Group = VGroup()
        axes = Axes(
            x_range=[-1.2, 1.2, .5],
            y_range=[-0.3, 10, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-1, 1.2, .5),
                "numbers_with_elongated_ticks": np.arange(-0.3, 3, 1),
            },
        )
        Background_Frame = SurroundingRectangle(axes,color=ORANGE)

        labels = axes.get_axis_labels(x_label="", y_label="")
        Tex01 = MathTex(
            r"\sum_{n=0}^{\infty}\frac{4n^2+4n+3}{2n+1}x^{2n}").shift(UP*1.6)
        S_Tex01 = SurroundingRectangle(Tex01,color=GREEN_A,fill_color=PINK,fill_opacity=0.3)
        self.play(Write(axes),FadeIn(labels),Write(Tex01),FadeIn(S_Tex01),GrowFromCenter(Background_Frame))
        
        #原本是x: (4*n**2+4*n+3)/(2*n+1)*x**(2*n)
        #但是指数增长过快，所以造了个假！！～～(2*n)*x**(2*n)
        def sum_func(x):
            number = lambda x: x**(2*n) 
            if math.isinf(number) and math.isnan(number):
                return 0
            return number


        for n in range(1,16):
            text = Text(f"n = {n}")
            sum_graph = axes.plot(
                sum_func,
                discontinuities=[-1.1, 1.1],
                dt=0.0001
            , color=random_bright_color())
            self.add(text)
            self.play(Write(sum_graph),run_time=0.5,rate_func=there_and_back)
            self.remove(text)

        #dot1_axes = Dot(axes.coords_to_point(1, 0))
        #dot2_axes = Dot(axes.coords_to_point(-1, 0))
        line1_graph = axes.get_lines_to_point(axes.c2p(1,10.16))
        line2_graph = axes.get_lines_to_point(axes.c2p(-1,10.17))
        Tex = MathTex(f"\\frac{{4\\cdot{n}^2+4\\cdot{n}+3}}{{2\\cdot{n}+1}}x^{{2\\cdot{n}}}")
        st = SurroundingRectangle(Tex,color=GREEN_A,fill_color=GREEN_C,fill_opacity=0.3)
        self.play(Write(line1_graph),Write(line2_graph),GrowFromCenter(st))


        for n in range(1,20):
            Tex = MathTex(f"\\frac{{4\\cdot{n}^2+4\\cdot{n}+3}}{{2\\cdot{n}+1}}x^{{2\\cdot{n}}}")

            sum_graph = axes.plot(
                sum_func,
                discontinuities=[-1.1, 1.1],
                dt=0.0001
            , color=random_bright_color())
            P1Group.add(sum_graph)
            self.add(Tex,st)
            self.play(Write(sum_graph),run_time=0.2,rate_func=linear)
            self.remove(Tex)
        P1Group.add(Background_Frame,axes,labels,Tex01,S_Tex01,line1_graph,line2_graph,Tex,st)

class SumFuncShow001(Scene):
    def construct(self):
        text01 = Text("今天来看一道2012年数学3的考研题\n颇有技巧～Remoo",t2c={"数学3":RED,"～Remoo":BLUE})
        self.play(Write(text01),run_time=2)
        self.play(text01.animate.shift(LEFT*2+UP*3.2))

        #题目
        Qs01_p1 = Text("求幂级数").align_to(text01,DL).shift(DOWN)
        Tex01 = MathTex(
            r"\sum_{n=0}^{\infty}\frac{4n^2+4n+3}{2n+1}x^{","2n","}").next_to(Qs01_p1,RIGHT)
        Qs01_p2 = Text("的收敛半径与和函数",t2c={"收敛半径":RED,"和函数":RED}).next_to(Tex01,RIGHT)
        group01 = VGroup (Qs01_p1,Tex01,Qs01_p2)
        self.play(GrowFromCenter(group01))
        self.wait(2)
        #此时题目已经展示出来了，需要把废话弄掉。
        text02 = Text("2012数三").scale(0.5).move_to(text01,UL)
        for letter in text02:
            letter.set_color(random_bright_color())
        self.play(Transform(text01,text02),group01.animate.move_to(text01,DL).shift(DOWN*0.4))

        text02 = Text("解:",font_size=84,t2c={"解:":PINK})
        self.play(text02.animate.move_to(group01,DL*2).shift(DOWN))

        #缺奇次幂，直接用比值审敛法

        mk_Rectangle_01 = Rectangle(color=RED, fill_opacity=0)
        mk_Rectangle_01.surround(Tex01[1])
        self.play(FadeOut(mk_Rectangle_01),run_time=0.5)
        for x in range(2):
            self.play(FadeOut(mk_Rectangle_01),run_time=0.5)
            self.play(FadeIn(mk_Rectangle_01),run_time=0.5)

        text03 = Text("由于这里是缺奇次幂，直接用比值审敛法",
            t2c={"比值审敛法":RED,"缺奇次幂":RED,}).next_to(text02,RIGHT)
        self.play(ReplacementTransform(Tex01[1].copy(),text03),FadeOut(mk_Rectangle_01),run_time=1)

        Tex02 = MathTex(
            r"\lim _{n \rightarrow \infty}\frac{\left|\frac{4(n+1)^{2}+4(n+1)+3}{2(n+1)+1} x^{2(n+1)}\right|}{\left|\frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}\right| } ",r"="
            ,font_size=64)
        self.wait(1)
        Tex02.move_to(ORIGIN)
        self.play(Write(Tex02))
        self.wait(1)

        ##代入比值审敛法公式
        #高亮题目Un部分
        Tex1_temp = Tex01[0][5:18].copy()
        self.add(Tex1_temp)
        for x in range(2):
            self.play(Tex1_temp.animate.set_fill(BLUE),run_time=0.8,rate_func=there_and_back)
        #传给分子
        self.play(ReplacementTransform(Tex1_temp,Tex02[0][6:44]))
        #高亮题目Un部分
        Tex1_temp = Tex01[0][5:18].copy()
        self.add(Tex1_temp)
        for x in range(1):
            self.play(Tex1_temp.animate.set_fill(BLUE),run_time=0.8,rate_func=there_and_back)
        #传给分母
        self.play(ReplacementTransform(Tex1_temp,Tex02[0][45:80]))
        self.wait(1)

        #self.play(Write(Tex02))

        ##式子往左边移动一点
        self.play(Tex02.animate.align_to(text02,LEFT))
        self.wait(1.5)

        ##式子化简
        #高亮化简部分
        Tex1_temp = Tex02[0][6:44].copy()
        Tex2_temp = Tex02[0][45:80].copy()
        self.add(Tex1_temp)
        for x in range(2):
            self.play(
                Tex1_temp.animate.set_fill(BLUE),
                Tex2_temp.animate.set_fill(BLUE),
                run_time=0.4,rate_func=there_and_back)

        ##化简结果展示
        #Tex03放在Tex02的右边
        Tex03 = MathTex(
            r"\lim _{n \rightarrow \infty} \frac{\left|x^{2(n+1)}\right|}{\left|x^{2 n}\right|}", r"=")\
            .next_to(Tex02,RIGHT)
        
        self.play(
            ReplacementTransform(Tex1_temp,Tex03),
            ReplacementTransform(Tex2_temp,Tex03),
            )

        ##把 解:XXX 隐去
        self.play(
            FadeOut(text02),FadeOut(text03),
            Tex02.animate.shift(UP*0.8),Tex03.animate.shift(UP*0.8))

        self.wait(2)

        ##把Tex02隐去，得出收敛半径
        self.play(FadeOut(Tex02),Tex03.animate.align_to(text02,LEFT))


        Tex04 = MathTex(
            r" =\left | x^2 \right | "
            ,font_size=64)\
            .next_to(Tex03,RIGHT).shift(LEFT*0.5)

        self.play(ReplacementTransform(Tex03[1],Tex04))

        self.wait(2)

        Tex05 = MathTex(
            r" =\left | x^2 \right |< 1 "
            ,font_size=64)\
            .next_to(Tex03,RIGHT).shift(LEFT*2)
        self.play(ReplacementTransform(Tex04,Tex05))

        self.wait(2)

        text04 = Text(",于是，收敛半径 R=1 ",t2c={"收敛半径":RED})
        text04.next_to(Tex05,RIGHT)

        self.play(Write(text04))
        
        self.wait(2)


        ##代入端点验算
        text05 = Text("当x = ±1时，",t2c={"±1":RED}).next_to(Tex03,DOWN).shift(DOWN)
        Tex06 = MathTex(r"\pm 1").next_to(Tex03,DOWN).shift(DOWN)
        Tex07 = MathTex(r"\sum_{n=1}^{\infty} \frac{4 n^{2}+4 n+3}{2 n+1}(\pm 1)^{2 n}").next_to(text05,RIGHT)
        Tex07[0][19:21].set_color(RED)


        self.play(Write(text05))
        self.wait(1)
        self.play(Transform(Tex06,Tex01))
        self.play(Transform(Tex06,Tex07))
        #化简
        Tex08 = MathTex(r"=\sum_{n=1}^{\infty} \frac{4 n^{2}+4 n+3}{2 n+1}").next_to(Tex06,RIGHT)
        self.play(Write(Tex08))

        text06 = Text("显然，该级数发散，故收敛域:(-1,1)",t2c={"收敛域:(-1,1)":PINK}).next_to(text05,DOWN).align_to(text05,LEFT).shift(DOWN*0.8)
        self.play(Write(text06))

class SumFuncPart2(Scene):
    def construct(self):
        #题目
        text01 = Text("2012数三").scale(0.5).to_edge(UL)
        for letter in text01:
            letter.set_color(random_bright_color())
        Qs01_p1 = Text("求幂级数").align_to(text01,DL).shift(DOWN)
        Tex01 = MathTex(
            r"\sum_{n=0}^{\infty}\frac{4n^2+4n+3}{2n+1}x^{","2n","}").next_to(Qs01_p1,RIGHT)
        Qs01_p2 = Text("的收敛半径与和函数",t2c={"收敛半径":GREEN,"和函数":RED}).next_to(Tex01,RIGHT)

        group01 = VGroup (Qs01_p1,Tex01,Qs01_p2,text01)
        self.add(group01)

        ##开始求和函数
        Tex02 = MathTex(r"let:s(x)=\sum_{n=0}^{\infty} \frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n} \quad(|x|<1)")\
            .align_to(text01,LEFT)
        Tex03 = MathTex(r"=\sum_{n=0}^{\infty} \frac{(2 n+1)^{2}+2}{2 n+1} x^{2 n}")
        #14 21
        self.play(ReplacementTransform(Tex02[0][14:21],Tex03))  

#实际例子40--灰阶显示
class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, GREEN)
        self.add(image, image.background_rectangle)

#MathTex公式在内存中的存储方式！！
class MathTexTest(Scene):
    def construct(self):
        Tex02_p1 = MathTex(
            "\\lim _{n \\rightarrow \\infty}"
            ,font_size=64)
        Tex02_p2 = MathTex(
            r"\lim _{n \rightarrow \infty}\frac{\left|\frac{4(n+1)^{2}+4(n+1)+3}{2(n+1)+1} x^{2(n+1)}\right|}{\left|\frac{4 n^{2}+4 n+3}{2 n+1} x^{2 n}\right|}"
            ,font_size=64)
        self.play(GrowFromCenter(Tex02_p2))
        self.wait(2)
        #for x in range(60):
            #self.play(Tex02_p2[0][x].copy().animate.shift(DOWN*2))
        self.play(Tex02_p2[0][6:44].copy().animate.shift(DOWN*2))

class foo(Scene):
    def construct( self ):

        lines1 = MathTex(r'\frac{1}{2}', r'\divisionsymbol', r'\frac{2}{3}')
        lines2 = MathTex(r'2 \divisionsymbol 3')
        lines3 = MathTex(r'\frac{2}{1} \times \frac{1}{3}')

        lines2.move_to(lines1[2], RIGHT)
        lines2.shift(RIGHT)
        lines3.move_to(lines2)
        self.play(Write(lines1))
        self.play(ReplacementTransform(lines1[2], lines2))
        self.wait(1)
        self.play(ReplacementTransform(lines2, lines3))
        self.wait(3)

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    #remoo注释

    def construct(self):
        #显示坐标
        self.add(NumberPlane())
        self.show_axis()
        #画圆
        self.show_circle()
        #画曲线部分！
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        #标记x轴的左边和右边端点
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        #标记y轴的上面和下面端点
        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        #用线直接画坐标
        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        #将线Line直接添加到屏幕上
        self.add(x_axis, y_axis)
        #为俩直线添加坐标标记
        self.add_x_labels()

        #即设置这个场景的坐标原点变量
        self.origin_point = [-4,0,0]#效果等同于np.array([-4,0,0])
        #设置曲线起始点坐标
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to([-1 + 2*i, 0, 0], DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=2)
        circle.move_to(self.origin_point)
        self.add(circle)
        #将局部变量上传至self全局变量区域中
        self.circle = circle

    def move_dot_and_draw_curve(self):
        #将全局变量“下载”下来，后面调用就不用这么麻烦
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        #点绕圆形移动
        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        #返回一条圆心到动点的线段
        def get_line_to_circle():
            #
            return Line(origin_point, dot.get_center(), color=BLUE)



        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class MovingSquareWithUpdaters(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=False,#显示小数点省略号
            num_decimal_places=6,#显示的小数位数
            include_sign=True,#正负号
        )
        #先让正方形去到屏幕上边界
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.animate.to_edge(DOWN),
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

class PlotParametricFunction(Scene):
    tempa = 1.0
    tempb = 10.0
    tempc = 55.0
    dn_kwargs = {
        'show_ellipsis':False,
        'num_decimal_places':3,
        'include_sign':True,
        "unit": r"^\circ",}
    Da = DecimalNumber(tempa,**dn_kwargs)
    Db = DecimalNumber(tempb,**dn_kwargs)
    Dc = DecimalNumber(tempc,**dn_kwargs)
    def func(self,a,b,c):
        return ParametricFunction(
            lambda t: np.array([
                np.cos(a * t) + np.cos(b * t) / 2 + np.sin(c * t) / 3,
                np.sin(a * t) + np.sin(b * t) / 2 + np.cos(c * t) / 3,
                0
            ])
            , t_range = np.array([-3.14/2, 3.14/2])
            , fill_opacity=0)\
            .set_color(color=[RED,YELLOW,BLUE,RED])\
            .scale(1.5)

    def construct(self):
        #显示参数方程组
        e1 = MathTex("\\cos(at)+{\\cos(bt)\\over 2}+{\\sin(ct)\\over 3}")
        e2 = MathTex("\\sin(at)+{\\sin(bt)\\over 2}+{\\cos(ct)\\over 3}")
        equation = VGroup(e1,e2).scale(0.9).arrange(DOWN,aligned_edge=LEFT)

        #上色方程组
        for eq in equation:
            eq[0][4].color=RED
            eq[0][12].color=BLUE
            eq[0][22].color=YELLOW

        #将方程组放在屏幕的右上角
        equation.to_corner(UR)

        #参数方程组左边的大括号
        brace = Brace(equation,LEFT)
        C_ = brace.get_tex("C")

        #t属于[0,2pi]的范围显示，放在方程组的下面，右边对齐
        range_ = MathTex(r"t\in[0,2\pi]")
        range_.next_to(equation,DOWN).align_to(equation,RIGHT)

        #将上面的所有东西显示出来
        group = VGroup(equation,brace,C_,range_)
        self.add(group)

        ###接下来是图形渲染部分
        pfun = self.func(self.tempa,self.tempb,self.tempc)
        pfun.shift(LEFT*3)
        pfun.add_updater(
            lambda mob: mob.become(
                self.func(
                    self.Da.get_value(),
                    self.Db.get_value(),
                    self.Dc.get_value()
                )
            ).shift(LEFT*3)
        )

        self.add(pfun)

        self.play(ChangeDecimalToValue(self.Da,10),ChangeDecimalToValue(self.Db,5),run_time=20,rate_func=linear)

        self.remove(pfun)

class PlotParametricFunction1(Scene):
    tempa = 1.0
    tempb = 10.0
    tempc = 55.0
    dn_kwargs = {
        'show_ellipsis':False,
        'num_decimal_places':3,
        'include_sign':True,
        "unit": r"",}
    Da = DecimalNumber(tempa,**dn_kwargs)
    Db = DecimalNumber(tempb,**dn_kwargs)
    Dc = DecimalNumber(tempc,**dn_kwargs)
    def func(self,a,b,c):
        return ParametricFunction(
            lambda t: np.array([
                t,
                np.sqrt(np.cos(t))*np.cos(a*t)+np.sqrt(np.fabs(t)),
                0
            ])
            , t_range = np.array([-3.14/2, 3.14/2])
            , fill_opacity=0)\
            .set_color(color=[RED,PINK,RED,random_bright_color(),RED])\
            .scale(2)

    def construct(self):
        #显示参数方程组
        e1 = MathTex("x,")
        e2 = MathTex("\\sqrt{\\cos (x)} \\cos (ax)+\\sqrt{|x|}")
        equation = VGroup(e1,e2).scale(0.9).arrange(DOWN,aligned_edge=LEFT)

        #上色方程组
        e2[0][12].color=RED
        #for eq in equation:
        #    eq[0][4].color=RED
        #    eq[0][12].color=BLUE
        #    eq[0][22].color=YELLOW

        #将方程组放在屏幕的右上角
        equation.to_corner(UR)

        #显示方程参数
        para1Text = Text("a = ",t2c={"a":RED}).shift(RIGHT)
        self.Da.next_to(para1Text,RIGHT)


        #参数方程组左边的大括号
        brace = Brace(equation,LEFT)
        C_ = brace.get_tex("C")

        #t属于[0,2pi]的范围显示，放在方程组的下面，右边对齐
        range_ = MathTex(r"x\in[-\pi/2,\pi/2]")
        range_.next_to(equation,DOWN).align_to(equation,RIGHT)

        #将上面的所有东西显示出来
        group = VGroup(equation,brace,C_,range_,para1Text)
        self.add(group)

        ###接下来是图形渲染部分
        pfun = self.func(self.tempa,self.tempb,self.tempc)
        pfun.shift(LEFT*3)
        pfun.add_updater(
            lambda mob: mob.become(
                self.func(
                    self.Da.get_value(),
                    self.Db.get_value(),
                    self.Dc.get_value()
                )
            ).shift(LEFT*3)
        )

        self.add(pfun)
        self.play(ChangeDecimalToValue(self.Da,100),run_time=10,rate_func=linear)
        self.remove(pfun)
            
class FourierSeries(Scene):
    tempa = 1.0
    tempb = 10.0
    tempc = 55.0
    dn_kwargs = {
        'show_ellipsis':False,
        'num_decimal_places':0,
        'include_sign':True,
        "unit": r"",}
    Da = DecimalNumber(tempa,**dn_kwargs)
    Db = DecimalNumber(tempb,**dn_kwargs)
    Dc = DecimalNumber(tempc,**dn_kwargs)
    def fourierfunc(self,t,function_fourier,times):
        for n in range(times):
            function_fourier+=(1/(2*t+1)**2)*np.cos((2*n+1)*t)
        return function_fourier

    def func(self,a,b,c):
        sumfunc = lambda t : (1/(2*t+1)**2)*np.cos((2+1)*t)
        return ParametricFunction(
            lambda t: np.array([
                t,
                2*self.fourierfunc(t,sumfunc(t),int(self.tempa)),
                0
            ])
            , t_range = np.array([-3.14/2, 3.14/2])
            , fill_opacity=0)\
            .set_color(color=[RED,YELLOW,BLUE,random_bright_color(),RED])\
            .scale(2)

    def construct(self):
        #显示参数方程组
        e1 = MathTex("x,")
        e2 = MathTex(r"2 \sum_{n=1}^{d} \frac{(-1)^{(n+1)}}{n} \sin (n x)")
        equation = VGroup(e1,e2).scale(0.9).arrange(DOWN,aligned_edge=LEFT)

        #将方程组放在屏幕的右上角
        equation.to_corner(UR)

        #显示方程参数
        para1Text = Text("a = ",t2c={"a":RED}).shift(RIGHT)
        self.Da.next_to(para1Text,RIGHT)

        #参数方程组左边的大括号
        brace = Brace(equation,LEFT)
        C_ = brace.get_tex("Fourier\nSeries")

        #t属于[0,2pi]的范围显示，放在方程组的下面，右边对齐
        range_ = MathTex(r"x\in[-\pi/2,\pi/2]")
        range_.next_to(equation,DOWN).align_to(equation,RIGHT)

        #将上面的所有东西显示出来
        group = VGroup(equation,brace,C_,range_,para1Text)
        self.add(group)

        ###接下来是图形渲染部分
        pfun = self.func(self.tempa,self.tempb,self.tempc)
        pfun.shift(LEFT*3)
        pfun.add_updater(
            lambda mob: mob.become(
                self.func(
                    self.Da.get_value(),
                    self.Db.get_value(),
                    self.Dc.get_value()
                )
            ).shift(LEFT)
        )

        self.add(pfun)
        self.play(ChangeDecimalToValue(self.Da,10),run_time=10,rate_func=linear)
        self.remove(pfun)

class Test(Scene):
    def construct(self):
        degree = 1
        dn_kwargs = {
        'show_ellipsis':False,
        'num_decimal_places':0,
        'include_sign':False,
        "unit": r"",}
        D_degree = DecimalNumber(degree,**dn_kwargs)

        axes = Axes(x_range=[-TAU*5/6,TAU*5/6,TAU/4],y_range=[-2,2])
        axes_label = axes.get_axis_labels()
        def sumfun(x,count):
            n=sympy.Symbol('n')
            f=sympy.sin(n*x)*(-1)**(n+1)/n
            return sympy.summation(f,(n,1,count))

        graph = axes.plot(lambda x: sumfun(x,int(degree)))
        def update(D_degree):
            lambda mob: mob.become(
                D_degree.get_value(),
                )
            return axes.plot(lambda x: sumfun(x,int(D_degree.get_value())))
        graph.add_updater(
            lambda mob: mob.become(
                update(D_degree)
                ).shift(ORIGIN)
            )
        g1 = VGroup(axes,axes_label)
        self.play(Write(g1))
        self.add(graph)
        self.play(ChangeDecimalToValue(D_degree,40),run_time=10,rate_func=linear)
        self.remove(graph)


#画函数图像
class PlotGraph(Scene):
    def construct(self):
        axes = Axes(x_range=[-TAU,TAU,TAU/4],y_range=[-1,1])
        axes_label = axes.get_axis_labels()
        graph_sin = axes.plot(lambda x : np.sin(x))
        graph_sin_label = axes.get_graph_label(graph_sin,"sinx",direction=UP+LEFT*5)
        g1 = VGroup(axes,axes_label,graph_sin,graph_sin_label)
        self.play(Write(g1))

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-4, 4, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        tan_graph = axes.plot(lambda x: np.tan(x),
            x_range=[-3.14/2,3.14/2,0.01],
            use_smoothing=False,

            dt=0.00001,
            color=BLUE)
        tan_label = axes.get_graph_label(
            tan_graph, "\\tan(x)", x_val=-5, direction=UP / 2
        )

        plot = VGroup(axes, tan_graph)
        labels = VGroup(axes_labels, tan_label)
        self.add(plot, labels)

class polarTest(Scene):

    def construct(self):
        polarplane_pi = PolarPlane(azimuth_units="PI radians", size=6)
        polartopoint_vector = Vector(polarplane_pi.polar_to_point(3, PI/2))
        self.add(polarplane_pi)
        self.add(polartopoint_vector)

class FourierTrans_First(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-0, 2*PI, PI/4],
            y_range=[-0.1, 2.5, 1],
            x_length=14,
            y_length=2
            ).to_edge(UP)
        axes_label = axes.get_axis_labels('Time','Intensity')
        polarPlane = PolarPlane(
            radius_max=2.0,
            azimuth_units="TAU radians",
            size=4,
            azimuth_label_font_size=24,
            radius_config={"font_size": 24},
            ).add_coordinates().to_edge(DOWN+LEFT)
        #显示坐标与坐标标签
        self.add(axes,axes_label,polarPlane)

        #一些全局参数-修改这三个参数就好
        delta = 0#偏移量
        rou = 1#theta的系数
        move = 1#极坐标变换的变化程度系数
        dn_kwargs = {'num_decimal_places':3,}
        D_delta = DecimalNumber(delta,**dn_kwargs)
        D_rou = DecimalNumber(rou,**dn_kwargs)
        D_move = DecimalNumber(move,**dn_kwargs).shift(DOWN)

        #解析式-公式修改这里就好
        r = lambda t: np.sin(D_rou.get_value()*t)+1
        par = lambda t: np.array([
            (r(t))*np.cos(D_move.get_value()*t),
            (r(t))*np.sin(D_move.get_value()*t),
            0])
        #更新函数
        def Func_axes():
            return axes.plot(r,color=PINK)

        def Func_polar():
            return polarPlane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)

        def Func_para():
            para = ParametricFunction(
                par, 
                t_range = np.array([0, 3.14*2]),
                fill_opacity=0)\
                .set_color(color=[RED,YELLOW,BLUE,RED])\
                .shift(DOWN*2+RIGHT*2)
            self.add(Dot(para.get_center()))
            return para

        axes_graph = Func_axes()
        polar_graph = Func_polar()
        para_graph = Func_para()

        axes_graph.add_updater(lambda mob: mob.become(Func_axes()))
        polar_graph.add_updater(lambda mob: mob.become(Func_polar()))
        para_graph.add_updater(lambda mob:mob.become(Func_para()))

        self.add(D_rou,D_move)
        self.play(Write(axes_graph),Write(polar_graph),Write(para_graph))
        self.play(ChangeDecimalToValue(D_rou,20),run_time=20,rate_func=linear)
        self.play(ChangeDecimalToValue(D_move,20),run_time=20,rate_func=linear)
        self.wait(1)
        

class SVGTest(Scene):
    def construct1(self):
        SVGM = SVGMobject("SVGLib//woman.svg")
        circle = Circle()
        self.play(Write(SVGM),Write(Circle))
        self.wait(1)


class FunctionColor(Scene):
    def construct(self):
        a=62
        b=50
        c=22
        tol = 1e-9
        pc = ParametricFunction(
            lambda t: np.array([
                np.cos(a * t) + np.cos(b * t) / 2 + np.sin(c * t) / 3,
                np.sin(a * t) + np.sin(b * t) / 2 + np.cos(c * t) / 3,
                0
            ]),
            t_range=[0,2*PI,0.7],
            tolerance_for_point_equality=0.5,
        )
        pc.set_color(color=[RED,YELLOW,BLUE])
        pc.scale(2)
        #.set_color(color=[RED,PINK,BLUE])\
        
        self.add(pc)


class DiscontinuousExample(Scene):
    def construct(self):
        ax1 = NumberPlane((-3, 3), (-4, 4))
        ax2 = NumberPlane((-3, 3), (-4, 4))
        VGroup(ax1, ax2).arrange()
        discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
        incorrect = ax1.plot(discontinuous_function, color=RED)
        correct = ax2.plot(
            discontinuous_function,
            discontinuities=[-2, 2],  # discontinuous points
            dt=0.1,  # left and right tolerance of discontinuity
            color=GREEN,
        )
        self.add(ax1, ax2, incorrect, correct)



class Curve3(Scene):
    def construct(self):
        #initial value
        A = 1
        B = 1
        C = 0
        values = VGroup(*[
            Tex(f"{t}=",tex_to_color_map={f"{t}":color}).scale(1.3)
            for t,color in zip(["a","b","c"],[RED,BLUE,YELLOW])
        ])
        values.arrange(DOWN,aligned_edge=LEFT,buff=1.2)

        dn_kwargs = {"unit": r"^\circ"}
        D_A = DecimalNumber(A,**dn_kwargs)
        D_B = DecimalNumber(B,**dn_kwargs)
        D_C = DecimalNumber(C,**dn_kwargs)
        D_G = VGroup(D_A,D_B,D_C)
        for d,s in zip(D_G,values):
            d.next_to(s,aligned_edge=DOWN)

        pc = self.get_param_func(A,B,C)

        upfunc =lambda mob: mob.become(
                self.get_param_func(
                    D_A.get_value(),
                    D_B.get_value(),
                    D_C.get_value()
                ).move_to(pc)
            )

        pc.add_updater(upfunc)
        self.add(pc)
        pc.shift(LEFT*3)
        self.play(
            ChangeDecimalToValue(D_B,15),
            run_time=2,
            rate_func=linear,
        )
        self.wait(0.3)
        #暂时移除updater
        pc.remove_updater(upfunc)
        self.play(pc.animate.shift(RIGHT*6),run_time=1)
        #平滑移动完，再添加回来
        pc.add_updater(upfunc)
        self.play(
            ChangeDecimalToValue(D_A,10),
            run_time=2,
            rate_func=linear,
        )

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

class move(Scene):
    def construct(self):
        circle = Circle()
        self.play(circle.animate.shift(LEFT))




class Con(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0])+np.cos(pos[1])
        stream_lines = StreamLines(func)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True,flow_speed=2)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

class Camera_move(MovingCameraScene):
    def construct(self):
        #保存默认摄像机状态，方便恢复
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        #graph.t_min相当于graph.x_range[0],即定义域左边界
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)

        #摄像机放大一倍，放大中心是动点moving_dot
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        #创建更新函数
        # 作用：所有被传入的Mobject都会被移动到动点moving_dot的中心
        def update_cam_pos(mob):
            moving_dot.get_center()
            mob.move_to(moving_dot.get_center())

        #为camera添加updater更新函数
        self.camera.frame.add_updater(update_cam_pos)
        #动画函数MoveAlongPath，传入运动的物体，路径graph。
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        #self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))





'''
All sound starts with vibration
所有声音源自振动。音乐和数学密不可分。
中世纪的四学（算术、几何、天文、音乐）以不同的方式向我们展示了音乐与数学的联系。
音乐包含：rhythms,notes,chords and melodies
一根弦的振动，通过空气传到耳中，a wave of pressure travels through the air
不同的frequency代表不同的notes
不同的乐器可以表达不同的情绪，长笛双簧管巴松钢琴
和谐与不和谐，和弦(Chord)与和声(Harmony)
    不同的音程有不同的和谐度，同度和八度是最和谐的，其次是纯五度。
数学上的fractal在音乐中也有对应
'''

'''
在manim社区版本中，
一、对于一般的物体，移动的方法分为 (瞬移) 和 (带动画移动)
    1、瞬移
        #直接对物体操作即可
    obj.shift(LEFT) 
        #瞬间移动,LEFT,UP是单位方向向量
        #以自身为参考

    obj.move_to()
        #瞬间移动
        #以屏幕中心为参考

    obj.next_to(circle,RIGHT)
        #瞬间移动
        #以传入对象为参考

    obj.align_to(circle,DOWN)
        #瞬间移动
        #以传入对象的假想边界作为调整
        #传入DOWN(0,-1)，那么物体的纵坐标就会"对其"对象的下边界
            #这个假想的边界一般以物体以中心为原点的第二象限区域
        #此处可参考https://docs.manim.community/en/stable/tutorials/building_blocks.html#mobjectplacement

    2、带动画移动
        #此处需要使用animate方法
    self.play(obj.animate.shift(LEFT))
        #移动时间持续1秒
        #以自身为参考
    #。。。省略，同理

二、对于添加了 add_update()的物体obj，如果想移动实时更新的物体，则需要从更新函数中处理。
    此时，直接对obj使用移动的函数是无效的。例如 obj.shift(LEFT) 
    add_update的逻辑是帧渲染，每一帧画面都会从 add_update()中传入的 方法参数 中生成新的obj。例如         
        obj.add_updater(
            lambda mob: mob.become(Function(lambda x : x + 1 ))
        )
    manim在渲染的过程中每一帧画面的obj都会调用一次 lambda mob: mob.become(Function(lambda x : x + 1 ))，作为这一帧的画面。
    所以，如果我们要移动obj的位置，只有一种方法：
        移动 Function(lambda x : x + 1 ) 的位置。
'''
