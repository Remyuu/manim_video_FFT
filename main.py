from manim import *
import numpy as np
import scipy

class formula_set(MathTex):
    formula_01s=[
        MathTex(r"F\left(\omega_{k}\right) \equiv \int_{-\infty}^{\infty} f(t) e^{-2 \pi i k t} \mathrm{~d} t, \quad k \in(-\infty, \infty)"),
        MathTex(r"f(t) e^{-2 \pi i k t}"),
        MathTex(r"F\left(\omega_{k}\right) = \int_{0}^{1} f(t) e^{-2 \pi i k t} \mathrm{~d} t, \\ k \in(-\infty, \infty)"),
        ]

    formula_01=[
        MathTex(r"F\left(\omega_{k}\right) \equiv \int_{-\infty}^{\infty}",r"f(t) e^{-2 \pi i k t}",r"\mathrm{~d} t, \quad k \in(-\infty, \infty)"),
        MathTex(r"f(t) e^{-2 \pi i k t}"),
        MathTex(r"F\left(\omega_{k}\right) = \int_{0}^{1} f(t) e^{-2 \pi i k t} \mathrm{~d} t, \\ k \in(-\infty, \infty)"),
        ]

    formula_02 = [MathTex(
            r"\hat{f}_{k}=\sum_{j=0}^{n-1} f_{j} e^{-i 2 \pi k j / n}"
        ),
            MathTex(
            r"k=0,1,2,...,n-1"
        )  ]

    formula_003 = MathTex()

    formula_004 = MathTex(
            r"\left[\begin{array}{l}\
            f_{0} \\\
            f_{1} \\\
            f_{2} \\\
            f_{3} \\\
            f_{4} \\\
            f_{5} \\\
            f_{6} \\\
            f_{7} \\\
            f_{8} \\\
            f_{9} \\\
            \end{array}\right]"
        )

    formula_005 = MathTex()

    formula_006 = [
        MathTex(
            r"\left[\begin{array}{l}\
            e^{-i 2 \pi(2(0)) / 9  }\\\
            e^{-i 2 \pi(2(1)) / 9  }\\\
            e^{-i 2 \pi(2(2)) / 9  }\\\
            e^{-i 2 \pi(2(3)) / 9  }\\\
            e^{-i 2 \pi(2(4)) / 9  }\\\
            e^{-i 2 \pi(2(5)) / 9  }\\\
            e^{-i 2 \pi(2(6)) / 9  }\\\
            e^{-i 2 \pi(2(7)) / 9  }\\\
            e^{-i 2 \pi(2(8)) / 9  }\\\
            e^{-i 2 \pi(2(9)) / 9  }\\\
            \end{array}\right]" 
        ),
        MathTex(r"e^{-i 2 \pi(2(0)) / 19")
    ]


class ContinuousFourier(Scene):
    def construct(self):
        #### Global variables ####
        second = 1
        y_scale = 0.5
        a = TAU/second * 0.4
        k = 0.4
        Da = DecimalNumber(a,num_decimal_places=2).shift(DOWN*2).move_to(LEFT*10)
        Dk = DecimalNumber(k,num_decimal_places=2).move_to(LEFT*10)

        # function f
        f = lambda x: y_scale*(np.cos(5*2*PI*x)+1)
        Df = lambda x: y_scale*(np.cos(1/Dk.get_value()*5*2*PI*x)+1)

        # formulas & text
        formula0 = formula_set.formula_01[0]
        formula1 = formula_set.formula_01[1].next_to(ORIGIN,RIGHT).shift(DOWN)
        formula2 = formula_set.formula_01[2].next_to(ORIGIN,RIGHT).shift(DOWN)
        formula5 = MathTex(r'k=0.4')
        text3 = MathTex(r'radius')
        

        def get_f3():
            return MathTex(r"2\pi \times",' {0} = {1}'.format(
                        str(round(Dk.get_value(),1)),str(round(Da.get_value(),1)) ))
        formula3 =  get_f3()
        formula3.add_updater(lambda obj : obj.become(get_f3()).to_edge(RIGHT))
        
        formula_group1 = VGroup(formula3,text3).arrange(RIGHT,aligned_edge=DOWN,buff=0.1)
        formula_group2 = VGroup(formula5).arrange(RIGHT,aligned_edge=DOWN,buff=0.1).shift(DOWN*3).shift(LEFT)

        text1 = Tex('Fourier Transform')

        # Cartesian coordinates
        axis_c = Axes(
            x_range=[0 , second + 0.1 , 1],y_range=[0, 1.5, 1],
            y_length=2,axis_config={"include_numbers": True},tips=False,
            ).to_edge(UP)
        axis_label = axis_c.get_axis_labels(x_label='time',y_label='intensity')
        graph_c = axis_c.plot(f,x_range=[0,second,0.01],color=TEAL_E)
        

        # polar coordinates
        axis_polar = PolarPlane(radius_max=1,size=4,azimuth_step = 10,
            fill_opacity=0.5,
            azimuth_direction='CW',
            azimuth_label_font_size=36,
            azimuth_units="PI radians",
            background_line_style = {
                "stroke_color": ORANGE,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
            }).add_coordinates()
        polar_graph = axis_polar.plot_parametric_curve(
            lambda t : [
                +np.cos(a*t) * (f(t)),
                -np.sin(a*t) * (f(t)),
                0
            ],t_range=[0,second,0.01],color=TEAL_E
            )
        polar_group = VGroup(axis_polar,polar_graph)
        polar_group.to_edge(DL)
        
        # CoM
        com  = polar_graph.get_center_of_mass() # -> narray
        dot_CoM = Dot().move_to(com).set_color(YELLOW)\

        ### messPoint horizontal line ###
        def get_horiz_line():return axis_polar.get_horizontal_line(polar_graph.get_center_of_mass(),line_config={"dashed_ratio": 1},color= ORANGE).set_stroke(width=7)
        line_h = get_horiz_line()
        line_h.add_updater(lambda obj : obj.become(get_horiz_line()))

        pointer_CoM = Vector(DL).scale(0.5).next_to(dot_CoM,UR)
        pointer_label_CoM = Tex("Center of Mass").next_to(pointer_CoM, UP)
        pointer_label_CoM.add_updater(lambda m: m.next_to(pointer_CoM, UP))       
        pointer_CoM.add_updater(
            lambda m: m.next_to(dot_CoM,UR)
        )
        IndicateCoM = VGroup(pointer_CoM,pointer_label_CoM)


        # upfunc
        upfunc_polar = lambda obj : obj.become(axis_polar.plot_parametric_curve(
            lambda t : [
                +np.cos(Da.get_value()*t) * (f(t)),
                -np.sin(Da.get_value()*t) * (f(t)),
                0
            ],
            t_range=[0,second,0.01],
            color=TEAL_E
        ))
        polar_graph.add_updater(upfunc_polar)

        upfunc_c = lambda obj : obj.become(axis_c.plot(Df,x_range=[0,second,0.01],color=TEAL_E))
        
        # dot
        updot = lambda obj : obj.move_to(polar_graph.get_center_of_mass()).set_color(YELLOW)
        dot_CoM.add_updater(updot)
        
        #################### Progress Bar #########################
        number_line = NumberLine(x_range=[0,1,0.5],length=2,include_numbers=True).next_to(formula1,DOWN).shift(DOWN*2)
        tracker = ValueTracker(0)
        
        pointer = Vector(UP).scale(0.5).next_to(
                        axis_c.c2p(tracker.get_value(),0),
                        DOWN
                    )
        label = MathTex("t=").next_to(pointer, DOWN)
        #number t and its updater
        t = DecimalNumber(tracker.get_value()).next_to(label,RIGHT)
        label.add_updater(lambda m: m.next_to(pointer, DOWN))       
        pointer.add_updater(
            lambda m: m.next_to(
                        axis_c.c2p(tracker.get_value(),0),
                        DOWN
                    )
        )

        def get_labelBox():return SurroundingRectangle(VGroup(label,t), corner_radius=0)
        box_label = get_labelBox()
        box_label.add_updater(lambda obj : obj.become(get_labelBox()))


        # Dot/vector on the graph and its updater
        # polar vector
        vec_e_intitial = axis_polar.get_vector([np.cos(-PI/6),np.sin(-PI/6)])
        vec_e = axis_polar.get_vector([np.cos(-PI/6),np.sin(-PI/6)])
        upvector_e = lambda obj : obj.become(
                    axis_polar.get_vector([np.cos(2 * 3.14 * 0.4 * tracker.get_value()),
                            np.sin(-2 * 3.14 * 0.4 * tracker.get_value())])
                    )
        vec_e.add_updater(upvector_e)
        upvector_polar_f = lambda obj : obj.become(
            axis_polar.get_vector([np.cos(TAU * 0.4 * tracker.get_value()) * (f(tracker.get_value())),
                    np.sin(-TAU * 0.4 * tracker.get_value()) * (f(tracker.get_value()))])
            )
        
        def get_arc():return ArcBetweenPoints( 
                       end= axis_polar.coords_to_point(0.3,0),
                       start= axis_polar.coords_to_point(0.3*np.cos(Da.get_value()),-0.3*np.sin(Da.get_value())),
                       stroke_color=YELLOW)
        arc= get_arc()
        arc.add_updater(lambda ob : ob.become(get_arc()))
        label_arc = MathTex(r"radius").next_to(arc,DL)



        # polar dot
        dot_polar = Dot()#
        updot_polar_f = lambda m : m.move_to(axis_polar.i2gp(graph=polar_graph,x=tracker.get_value()))#
        dot_polar.add_updater(updot_polar_f)#

        # cartessian dot
        dot_cartesian = Dot()
        updot_cartesian = lambda m : m.move_to(axis_c.i2gp(graph=graph_c,x=tracker.get_value()))
        dot_cartesian.add_updater(updot_cartesian)
        
        # tex
        label_e = MathTex('e^{}'.format('{-2\pi 0.4 \cdot '+str(round(tracker.get_value(),2))+' i}')).next_to(vec_e, DOWN)
        label_e.add_updater(lambda m: m.become(MathTex('e^{}'.format('{-2\pi 0.4 \cdot'+str(round(tracker.get_value(),2))+' i}'))).next_to(vec_e, DOWN))


        
        t.add_updater(lambda obj : obj.become(DecimalNumber(round(tracker.get_value(),2))).next_to(label,RIGHT))
        ######################### Progress Bar ##################################

        ####### frequency domain #######lo
        axis_freq = Axes(x_range=[0, 15, 1], y_range=[-0.1, 0.8],
                          x_length=8, y_length=3,
                          axis_config={"include_numbers": True}).next_to(axis_polar, RIGHT).align_to(axis_polar, DOWN)
        def get_freqDomain_sample(wind):
            return scipy.integrate.quad(
                lambda t: f(t)*np.exp(complex(0, -TAU*wind*t)),
                0, second
            )[0].real
            
        graph_freqD = axis_freq.plot(
            get_freqDomain_sample, x_range=[0, 10, 0.1],color=YELLOW)
        dot_freq = Dot().move_to(axis_freq.i2gp(Dk.get_value(),graph_freqD))
        
        def up_dot(dot):
            temp_dot = Dot(radius=0.02, color=YELLOW, fill_opacity=0.8)
            temp_dot.move_to(axis_freq.i2gp(Dk.get_value(),graph_freqD))
            dot.move_to(temp_dot)
        
        dot_freq.add_updater(up_dot)
        
        def get_vertic_line():return axis_freq.get_vertical_line(axis_freq.i2gp(Dk.get_value(),graph_freqD),line_config={"dashed_ratio": 1},color= ORANGE).set_stroke(width=7)
        line_v = get_vertic_line()
        line_v.add_updater(lambda obj : obj.become(get_vertic_line()))

        path = VMobject()
        path.set_points_as_corners([dot_freq.get_center(), dot_freq.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_freq.get_center()])
            path.become(previous_path)
            path.set_color(YELLOW)
        path.add_updater(update_path)



        ########################################################
        #                  Start Animation                     #
        ########################################################
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text1))
        self.wait()
        self.play(Write(formula0))
        self.wait()
        
        self.play(FadeOut(formula0[0],formula0[2]))
        self.play(formula0[1].animate.move_to(formula1))
        self.wait()
        self.add(axis_c,axis_label,axis_polar)
        self.wait()
        
        self.play(Circumscribe(formula0[1][0:4]))
        self.wait()
        self.play(ReplacementTransform(formula0[1][0:4].copy(),graph_c))
        self.wait()
                          # shift up animation
        self.play(Circumscribe(formula0[1][4:11]))
        self.wait()
        self.play(ReplacementTransform(formula0[1][4:11].copy(),vec_e_intitial))
      
        # progress bar

        bar_group = VGroup(pointer,label,box_label,t)
        self.add(bar_group)
        self.add(vec_e,label_e)
        self.play(FadeOut(vec_e_intitial))
        
        tracker += 1
        self.wait()
        tracker -= 0.5
        self.wait(0.5)
        self.play(tracker.animate.set_value(1))
        self.wait(0.5)
        self.play(tracker.animate.set_value(0.1))
        self.play(tracker.animate.increment_value(0.6))
        self.wait(0.5)
                    
        self.play(Circumscribe(formula0[1][6:10]))
        self.wait()
        
        self.wait() 

        self.play(FadeOut(vec_e,label_e))  

        self.add(polar_graph.set_color(PURPLE))
           
        self.add(dot_cartesian,dot_polar)
        self.add(arc,label_arc)
        self.bring_to_front(arc)

        self.play(tracker.animate.set_value(0))
        self.wait(0.5)
        self.play(tracker.animate.set_value(1),run_time=5),
        self.wait(0.5)
        self.play(tracker.animate.set_value(0.1),run_time=5)
        self.play(tracker.animate.increment_value(0.6),run_time=5)
        self.wait(0.5)      
        self.play(FadeOut(bar_group))
        self.play(FadeOut(dot_cartesian))
        self.wait()


        # winding animation
        self.play(ReplacementTransform(graph_c.copy(),polar_graph),
            run_time=3.5,
            path_arc = -TAU*2/3)
        self.wait()
        
        
        # CoM
        self.play(ReplacementTransform(formula0[1],formula2))
        self.wait() 
        self.play(Circumscribe(formula2[0]))
        self.wait() 
        self.play(ReplacementTransform(polar_graph.copy(),dot_CoM))        
        self.wait() 
        self.play(FadeIn(IndicateCoM))
        #formula_group1.next_to(formula_group2,RIGHT)
        #self.play(FadeOut(formula_group2))
        #self.add(formula_group1)
        self.wait()
        graph_c.add_updater(upfunc_c)
        self.wait()

        # changing the CoM with k & draw freq_domain
        
        self.play(ChangeDecimalToValue(Da,0.7*TAU),ChangeDecimalToValue(Dk,0.7)) #turn back to 0
        self.wait()
        self.play(ChangeDecimalToValue(Da,0.3*TAU),ChangeDecimalToValue(Dk,0.3)) #turn back to 0

        #self.play(FadeOut(formula_group1))
        self.play(FadeOut(IndicateCoM))
        self.play(FadeOut(arc,label_arc))

        self.add(axis_freq,dot_freq,line_v,line_h,path)

        self.play(ChangeDecimalToValue(Da,0.3*TAU),ChangeDecimalToValue(Dk,0.3)) #turn back to 0
        self.wait()
        self.play(ChangeDecimalToValue(Da,5*TAU),ChangeDecimalToValue(Dk,5),rate_func=rate_functions.linear,run_time=20)
        self.wait()
        self.play(ChangeDecimalToValue(Da,10*TAU),ChangeDecimalToValue(Dk,10),rate_func=rate_functions.linear,run_time=15)

        # explanation on why there is peaks at frequency 5
            # Audio text: The reason behind might be that at this winding frequency, every period of f are just wound in one full circle, so we can gather all the peaks of f(t) on the right of the graph. Therefore by tracing the positon of CoM, we get feedback on whether the current k is similar to the true frequency of f. We are able to reveal the unknown frequencies of f(t) by looking at the position of CoM, with this mathematical wounding machine.

        # change f and see the polar
            #self.play(ReplacementTransform(polar_graph,polar_graph_new))


class WindingAndFreqdomain(Scene):
    def construct(self):
        def play_change_channel(change_to:int,run_time:float=1,before_wait:float=0,then_wait:float=0):
            self.wait(before_wait)
            graph_polar.remove_updater(up_polar_graph)
            dot_freqDomain.remove_updater(up_dot)
            self.__channel__= change_to
            self.play(
                Transform(graph_polar,get_pc(set_data['f_set'][change_to],_color=set_data['color_set'][change_to])),#改极坐标
                Transform(graph_label,set_data['graph_label_set'][self.__channel__]),
                Transform(graph_c,set_data['graph_c_set'][self.__channel__]),
                Transform(graph_freqD,axis_freqD.plot(get_freqDomain_sample,x_range=[0,15,0.1],color=YELLOW)),#改freqD图像
                dot_freqDomain.animate.move_to(get_dot_freqDomain(Da.get_value())),
                run_time=run_time
                )
            self.bring_to_front(dot_freqDomain,graph_label)
            dot_freqDomain.set_color(set_data['color_set'][self.__channel__])
            dot_freqDomain.add_updater(up_dot)
            graph_polar.add_updater(up_polar_graph)
            self.wait(then_wait)

        #### Global variables ####
        self.__channel__=0

        second = 2
        y_scale = 0.5
        Da = DecimalNumber(0.2)

        f1_lambda = 5;f2_lambda = 11;f3_lambda = 8
        set_data = {'f_set':[
            lambda x: y_scale*(np.cos(f1_lambda*TAU*x)+1),
            lambda x: y_scale*(np.cos(f2_lambda*TAU*x)+1),
            lambda x: y_scale*(np.cos(f1_lambda*TAU*x)+0.5*np.cos(f2_lambda*TAU*x)+1.5),
            lambda x: y_scale*(np.cos(f1_lambda*TAU*x)+0.5*np.cos(f3_lambda*TAU*x)+1.5),
            lambda x: y_scale*(np.cos(f1_lambda*TAU*x)+np.cos(f3_lambda*TAU*x)+2),
#
        ],
        'color_set':[
            TEAL_A,
            TEAL_B,
            TEAL_C,
            TEAL_D,
            TEAL_E,
            RED_D,
        ],
        #It will be normalized the style automatically,like match the color,scale and Mobject position.
        'tex_set':[
            MathTex(r'\cos({}\pi \cdot x)'.format(f1_lambda)),
            MathTex(r'\cos({}\pi \cdot x)'.format(f2_lambda)),
            MathTex(r'\cos({}\cdot 2\pi \cdot x)+0.5\cos({}\cdot 2\pi \cdot x)'.format(f1_lambda,f2_lambda)),
            MathTex(r'\cos({}\cdot 2\pi \cdot x)+0.5\cos({}\cdot 2\pi \cdot x)'.format(f1_lambda,f3_lambda)),
            MathTex(r'\cos({}\cdot 2\pi \cdot x)+0.5\cos({}\cdot 2\pi \cdot x)'.format(f1_lambda,f2_lambda)),
        ],
        #It will be initializated automatically
        'graph_label_set':[],
        'graph_c_set':[],
        }
        #Initilization
            # Cartesian coordinates
        axis_c = Axes(
            x_range=[0 , second + 0.1 , 1],y_range=[0, 2, 1],
            y_length=2,axis_config={"include_numbers": True},tips=False,
            ).to_edge(UP)
        label_axis_c = axis_c.get_axis_labels(x_label='time',y_label='intensity')
        for index,mathtex in enumerate(set_data['tex_set']):
            mathtex.set_color(set_data['color_set'][index]).scale(1.5).shift(UP*2.5)
        set_data['graph_label_set'] = [VGroup(_texf_,BackgroundRectangle(_texf_, color=WHITE, fill_opacity=0.15)) 
                                for _texf_ in set_data['tex_set']]

        set_data['graph_c_set'] = [axis_c.plot(set_data['f_set'][x],x_range=[0,second,0.01],color=set_data['color_set'][x])
                            for x in range(len(set_data['f_set']))]

        #### polar ####
        def get_pc(_func,_color=RED):
            return axis_polar.plot_parametric_curve(
                lambda t: [
                +np.cos(Da.get_value()*TAU*t) * (_func(t)),
                -np.sin(Da.get_value()*TAU*t) * (_func(t)),
                0
            ], t_range=[0, second, 0.01], color=_color,stroke_width=2)
        def get_mess_point():
            return Dot(graph_polar.get_center_of_mass())

        #axis_polar = PolarPlane(radius_max=1.9,size=4.5).to_edge(DL)
        axis_polar = PolarPlane(radius_max=1.9,size=3.5,azimuth_step = 10,
            fill_opacity=0.5,
            azimuth_direction='CW',
            azimuth_label_font_size=36,
            azimuth_units="PI radians",
            background_line_style = {
            "stroke_color": ORANGE,
            "stroke_width": 2,
            "stroke_opacity": 0.5,
        }).add_coordinates().to_edge(DL)

        graph_polar = VMobject().become(get_pc(set_data['f_set'][self.__channel__],set_data['color_set'][self.__channel__]))
        dot_mess = VMobject().become(get_mess_point())
        def up_polar_graph(obj): return obj.become(get_pc(set_data['f_set'][self.__channel__],set_data['color_set'][self.__channel__]))
        def up_mess_point(obj): return obj.become(get_mess_point())

        #####freqDomain####
        t_min = 0
        t_max = second
        scale = 1 / t_max - t_min
        axis_freqD = Axes(x_range=[0, 15, 1], y_range=[-0.1, 0.8],
                          x_length=7, y_length=3,
                          axis_config={"include_numbers": True}).next_to(axis_polar, RIGHT).align_to(axis_polar, UP)
        label_axis_freqD = axis_freqD.get_axis_labels(
            x_label='freq(TAU)', y_label='')

        def get_freqDomain_sample(wind):
            return scale * scipy.integrate.quad(
                lambda t: set_data['f_set'][self.__channel__](
                    t)*np.exp(complex(0, -TAU*wind*t)),
                t_min, t_max
            )[0].real

        graph_freqD = axis_freqD.plot(
            get_freqDomain_sample, x_range=[0, 15, 0.1])

        def get_dot_freqDomain(wind_freq):  # 'wind_freq'no need to times TAU
            color = set_data['color_set'][self.__channel__]
            return Dot(axis_freqD.input_to_graph_point(x=wind_freq, graph=graph_freqD), color=color)
        dot_freqDomain = get_dot_freqDomain(0.1)
        def up_dot(mob): return mob.become(get_dot_freqDomain(Da.get_value()))
        dot_freqDomain.add_updater(up_dot)

        label_Da = Text('Winding Freq:')
        group_Da = VGroup(label_Da, Da).arrange(RIGHT).next_to(axis_freqD, DOWN)

        ###############
        #绘制三个坐标轴
        self.add(axis_c, axis_polar, axis_freqD,
                 label_axis_c, label_axis_freqD)
        #绘制初始直角坐标图像
        self.add(graph_freqD, dot_freqDomain)
        #绘制Winding Freq动态数字
        self.add(group_Da)

        #现在场景中，除了三幅图像和一个点没画
        #绘制直角坐标的c_g_1 初始的
        graph_c = set_data['graph_c_set'][0].copy()
        graph_label = set_data['graph_label_set'][0].copy()
        self.play(Create(graph_c), FadeIn(graph_label))

        self.play(ReplacementTransform(graph_c.copy(), graph_polar),
                  run_time=3.5,
                  path_arc=-TAU*2/3)

        #添加质点动画
        self.play(ReplacementTransform(graph_polar.copy(), dot_mess))
        graph_polar.add_updater(up_polar_graph)
        dot_mess.add_updater(up_mess_point)

        self.wait()

        self.play(ChangeDecimalToValue(Da, 5, run_time=5))

        play_change_channel(1, before_wait=1, then_wait=1)

        self.play(ChangeDecimalToValue(Da, 11, run_time=5))

        play_change_channel(2, before_wait=1, then_wait=1)

        self.play(ChangeDecimalToValue(Da, 8, run_time=5))

        play_change_channel(3, before_wait=1, then_wait=1)

        self.play(ChangeDecimalToValue(Da, 5, run_time=5))

        play_change_channel(4, before_wait=1, then_wait=1)

        self.play(ChangeDecimalToValue(Da, 8, run_time=5))

