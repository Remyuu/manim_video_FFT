'''###Update inf###
    8.19 
        1、修复DFT_Illustration中散点图像的错误

    8.15
        1、公式写在<formula_set>类中，统一管理 12:39
        2、建立<sample_set>类，统一管理数据样本 13:03
        3、统一化manim动画流程
    8.30
        1、改进Introduction视频流程
    8.31
        1、完成多公式多轨道切换图像
    9.1
        1、已上传至https://github.com/Remyuu/manim_video_FFT/

'''
#拖鞋 挂钩 转换插头
#药
#眼镜 保暖内衣 wilko -枕头被子不买
#数据线 密码器 
#筷子 吹风机（200的连负离子都没有

from manim import *
import librosa
import numpy as np
import scipy
import pickle #写出读取打包 序列化二进制list

# 文件都是以二进制的方式储存在硬盘上
# 那么如果有一个int ：13 存在硬盘，转成二进制即可
# 如果我们有一个list [1,2,3,4,5]呢 甚至是 ["hello",12,1.11,Dot()]
# 那么我们就要序列化list 打包好--使用pickle
# 所有文件都是序列化的，方式不同。我用list写出到文件，我就用list的方式读取，中间过程需要序列化。

#import librosa
#import pickle
#samp = [1,2,3,1.11]
#with open('test.iiiiii','rb') as pickle_file:
#    #序列化samp对象，以二进制的方式写到文件
#    pickle.dump(samp,pickle_file)
###################################################
#
#import librosa
#import pickle
#with open('winter.libyy','rb') as pickle_file:
#    #反序列化对象
#    samp_read = pickle.load(pickle_file)
#    print(samp_read)
#>>> samp_read = [1,2,3,1.11]
#

# # ##生成wave文件的数据集样本文件##
# class UsingLibrosa():
#     #利用librosa读取wave文件
#     yy44,fs44 = librosa.load('winter.wav',sr=44100)
#     #写出数据样本文件
#     with open('winter.libyy','wb') as pickle_file:
#         #序列化对象
#         pickle.dump(yy44, pickle_file)


##数据类##
class sample_set:
    def get_winter_wav():
        with open('winter.libyy','rb') as pickle_file:
            #反序列化对象
            sample = pickle.load(pickle_file)
            
            return sample,max(sample)

    # WAVE_FILE, SAM_RATE = librosa.load(r'003.wav')
    # NUM_DOTS = len(WAVE_FILE)  # number of discrete point
    # DURATION = NUM_DOTS/SAM_RATE  # duration of the audio (second)
    # SAMPLE_DENSITY = 1 / 1 # the density of point
    # data = WAVE_FILE[1000:1030:int(1/SAMPLE_DENSITY)]
    #len_data = len(data)
    
##公式类##
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

class Introduction(Scene):
    def __init__(self, renderer=None, camera_class=..., always_update_mobjects=False, random_seed=None, skip_animations=False):
        super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)


    def construct(self):
        self.Introduction_Scene()
        self.Do_it_yourself()
        pass

    def Introduction_Scene(self):
        ax = Axes(
            x_range=[0 , 10*TAU , TAU],
            y_range=[-1, 1.1, 0.5],
            x_length=(7+1/9)*1.5,
            y_length=2,
        )
        #http://zhongguose.com/
        f_1 = ax.plot(lambda x : np.sin(x)+0.4*np.sin(4*x),x_range=[0 , 10*TAU , 0.1],color='#ed5a65')
        f_1_1 = ax.plot(lambda x : np.sin( x ),x_range=[0 , 10*TAU , 0.1],color='#eea2a4')
        f_1_2 = ax.plot(lambda x : 0.4*np.sin(4*x),x_range=[0 , 10*TAU , 0.1],color='#f1939c')
        Tex_1 = MathTex("f(x)=f_{1}(x)+f_{2}(x)",color='#ed5a65').scale(2)
        Tex_1_1 = MathTex(r"f_{1}(x)=?\sin(?x)",color='#eea2a4').scale(2)
        Tex_1_2 = MathTex(r"f_{2}(x)=?\sin(?x)",color='#f1939c').scale(2)
        scene_group=VGroup(f_1,f_1_1,f_1_2,Tex_1,Tex_1_1,Tex_1_2)

        sm = SVGMobject("sound_icon_intro_0.svg")
        self.play(Write(sm),run_time=0.5)
        self.play(Wiggle(sm,rotation_angle=0.03*TAU),run_time=1.5)

        
        self.play(ReplacementTransform(sm,f_1),run_time=1.5)
        self.play(f_1.animate.to_edge(UP*2))

        f_1_1.next_to(f_1,DOWN)
        f_1_2.next_to(f_1_1,DOWN)
        Tex_1.move_to(f_1)
        Tex_1_1.move_to(f_1_1)
        Tex_1_2.move_to(f_1_2)
        
        self.play(ReplacementTransform(f_1.copy(),f_1_1),ReplacementTransform(f_1.copy(),f_1_2),run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(f_1,Tex_1))

        self.wait()
        self.play(Transform(f_1_1,Tex_1_1),Transform(f_1_2,Tex_1_2),run_time=0.6)
        self.wait()
        self.play(scene_group.animate.set_color(GREY))
        self.play(FadeOut(scene_group))

    def Do_it_yourself(self):
        t_min = 0 ; t_max = 6*TAU ; t_dt=0.01
        ax = Axes(
            x_range=[t_min , t_max +TAU , TAU],
            y_range=[-2.5, 2.5, 1],
            x_length=(7+1/9)*1.5,
            y_length=3,
        ).shift(DOWN)
        text0 = Text(r'We try to build the sound ourselves',t2c={"sound":'#ed5a65'})

        f_sine_1 = ax.plot(lambda x:np.sin(x),color='#eea2a4',x_range=[t_min,t_max,t_dt])
        f_sine_2 = ax.plot(lambda x:2*np.sin(4*x)+4,color='#f1939c',x_range=[t_min,t_max,t_dt])
        Tex_f1 = ax.get_graph_label(f_sine_1,'sin(x)',x_val=t_max+TAU, direction=UP / 2,color=BLUE_A)
        Tex_f2 = ax.get_graph_label(f_sine_2,'2sin(4x)',x_val=t_max+TAU, direction=DOWN / 2,color=BLUE_B)

        f_sum_1 = ax.plot(lambda x:np.sin(x)+2*np.sin(4*x),color='#ed5a65',x_range=[t_min,t_max,t_dt])
        Tex_sf_1 = Text(r'f(x) = sin(x) + 2sin(4x)',
            t2c={'f(x)':'#ed5a65','sin(x)':'#eea2a4','2sin(4x)':'#f1939c'}
            ).next_to(f_sum_1,UP)

        text1 = Text('Or maybe these two',t2c={'two':PINK}).next_to(Tex_sf_1,UP)

        f_sum_2 = ax.plot(lambda x:np.sin(x)+0.5*np.sin(8*x),color='#ed5a65',x_range=[t_min,t_max,t_dt])
        Tex_sf_2 = Text(r'f(x) = sin(x) + 0.5sin(8x)',
            t2c={'f(x)':'#ed5a65','sin(x)':'#eea2a4','0.5sin(8x)':'#f1939c'}
            ).next_to(f_sum_1,UP)

        text2 = Text('Paterms can be seen as the intensity of the second wave is smaller,\n'+\
            'that adding periodic functions together looks like a wave in a wave.',
            font_size=36,
            color=BLUE).to_edge(UP)


        self.play(Write(text0))
        self.wait()
        self.play(Uncreate(text0))
        self.play(FadeIn(ax))
        #Show the graph and labels,then sum them up
        self.play(Write(f_sine_1),Write(Tex_f1))
        self.wait()
        self.play(Write(f_sine_2),Write(Tex_f2))
        self.wait()
        self.play(
            ReplacementTransform(f_sine_1,f_sum_1),
            ReplacementTransform(f_sine_2,f_sum_1),
            Transform(Tex_f1,Tex_sf_1[5:11]),
            Transform(Tex_f2,Tex_sf_1[11:21])
            )
        self.wait()
        self.play(FadeIn(Tex_sf_1),FadeOut(Tex_f1),FadeOut(Tex_f2))

        self.play(Create(text1),run_time=0.5)
        self.wait(2)
        self.play(
            FadeTransform(Tex_sf_1,Tex_sf_2),
            FadeTransform(f_sum_1,f_sum_2)
            )
        
        self.play(Unwrite(text1))
        self.wait()
        #Plot the first component again
        self.play(
            FadeTransform(Tex_sf_2,Tex_sf_1),
            FadeTransform(f_sum_2,f_sum_1)
        )
        self.wait()
        self.play(Write(text2))
        self.wait()
        

#Almost Fourier Transform 
class ContinuousFourier(Scene):
    def construct(self):
        #### Global variables ####
        second = 1
        y_scale = 0.5
        a = TAU/second * 0.4
        k = 0.4
        Da = DecimalNumber(a).shift(DOWN*2)
        Dk = DecimalNumber(k,num_decimal_places=2)
        
        # function f
        f = lambda x: y_scale*(np.cos(5*2*PI*x)+1)

        # formulas & text
        formula0 = formula_set.formula_01[0]
        formula1 = formula_set.formula_01[1].next_to(ORIGIN,RIGHT)
        formula2 = formula_set.formula_01[2].move_to(formula1)
        formula3 = MathTex(r'2\pi \times').next_to(formula2,DOWN)
        formula4 = MathTex(r'=')
        formula5 = MathTex(r'k=0.4')
        
        text3 = MathTex(r'radius')
        formula_group1 = VGroup(formula3,Dk,formula4,Da,text3).arrange(RIGHT,aligned_edge=DOWN,buff=0.1)
        formula_group2 = VGroup(formula5).arrange(RIGHT,aligned_edge=DOWN,buff=0.1).shift(DOWN*3).shift(LEFT)
        
        text1 = Tex('Fourier Transform')


        # Cartesian coordinates
        c_axis = Axes(
            x_range=[0 , second + 0.1 , 1],
            y_range=[0, 1.1, 1],
            x_length=(7+1/9)*2*1.8,
            y_length=4*3/4,
            axis_config={"include_numbers": True},
        ).scale(0.5).to_edge(UP)
        c_graph = c_axis.plot(f,x_range=[0,second,0.01],color=YELLOW)

        axis_label = c_axis.get_axis_labels()
        # polar
        polar_axis = PolarPlane(radius_max=1,size=5)
        polar_graph = polar_axis.plot_parametric_curve(
            lambda t : [
                +np.cos(a*t) * (f(t)),
                -np.sin(a*t) * (f(t)),
                0
            ],t_range=[0,second,0.01],color=YELLOW
        )
        polar_group = VGroup(polar_axis,polar_graph)
        polar_group.to_edge(DL)
        
        # CoM
        com = polar_graph.get_center_of_mass() # -> narray
        CoM = Dot()
        CoM.move_to(com).set_color(BLUE)

        # upfunc
        upfunc = lambda obj : obj.become(polar_axis.plot_parametric_curve(
            lambda t : [
                +np.cos(Da.get_value()*t) * (f(t)),
                -np.sin(Da.get_value()*t) * (f(t)),
                0
            ],
            t_range=[0,second,0.01],
            color=YELLOW
        ))
        polar_graph.add_updater(upfunc)
        # dot
        updot = lambda obj : obj.move_to(polar_graph.get_center_of_mass()).set_color(BLUE)
        CoM.add_updater(updot)
        
#################### Progress Bar #########################
        number_line = NumberLine(x_range=[0,1,0.5],length=2,include_numbers=True).next_to(formula1,DOWN).shift(DOWN*2)
        tracker = ValueTracker(0)
        pointer = Vector(DOWN).scale(0.5).next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        label = MathTex("t=").next_to(pointer, UP)
        label.add_updater(lambda m: m.next_to(pointer, UP))       
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        )

        # Dot/vector on the graph and its updater
        # polar vector
        vec_e = polar_axis.get_vector([1,0])
        upvector_e = lambda obj : obj.become(
                    polar_axis.get_vector([np.cos(2 * 3.14 * 0.4 * tracker.get_value()),
                            np.sin(-2 * 3.14 * 0.4 * tracker.get_value())])
                    )
        vec_e.add_updater(upvector_e)
        upvector_polar_f = lambda obj : obj.become(
            polar_axis.get_vector([np.cos(TAU * 0.4 * tracker.get_value()) * (f(tracker.get_value())),
                    np.sin(-TAU * 0.4 * tracker.get_value()) * (f(tracker.get_value()))])
            )
        
        # polar dot
        dot_polar = Dot()#
        updot_polar_f = lambda m : m.move_to(polar_axis.i2gp(graph=polar_graph,x=tracker.get_value()))#
        dot_polar.add_updater(updot_polar_f)#

        # cartessian dot
        dot_cartesian = Dot()
        updot_cartesian = lambda m : m.move_to(c_axis.i2gp(graph=c_graph,x=tracker.get_value()))
        dot_cartesian.add_updater(updot_cartesian)
        
        
        # tex
        label_e = MathTex(r'e^{-2\pi 0.4 t i}').next_to(dot_polar, DOWN)
        label_e.add_updater(lambda m: m.next_to(vec_e, DOWN))

        #number t and its updater
        t = DecimalNumber(tracker.get_value()).next_to(label,RIGHT)
        t.add_updater(lambda obj : obj.become(DecimalNumber(tracker.get_value())).next_to(label,RIGHT))
######################### Progress Bar ##################################

        #######freqDomain

        

###需要优化###
    #锚点逐个显示，优化性能
    #2022.8.30
###------###




        ########################################################
        #                  Start Animation                     #
        ########################################################
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text1),Write(formula0))
        self.wait()
        self.play(FadeOut(formula0[0],formula0[2]))
        self.play(formula0[1].animate.move_to(formula1))
        #self.play(ReplacementTransform(formula0,formula1))
        self.add(c_axis,axis_label,polar_axis)
        self.wait()
        
        self.play(Circumscribe(formula0[1][0:4]))
        self.wait()
        self.play(ReplacementTransform(formula0[1][0:4].copy(),c_graph))
        self.wait()
        # shift up animation
        self.play(Circumscribe(formula0[1][4:11]))
        self.wait()
      
        # progress bar
        bar_group = VGroup(number_line, pointer,label,label_e,t)
        self.add(bar_group)
        self.add(vec_e)
      
        tracker += 1
        self.wait(1)
        tracker -= 0.5
        self.wait(0.5)
        self.play(tracker.animate.set_value(1))
        self.wait(0.5)
        self.play(tracker.animate.set_value(0.1))
        self.play(tracker.animate.increment_value(0.6))
        self.wait(0.5)
               
        self.play(Circumscribe(formula0[1][6:10]))
        self.wait()
        self.play(Write(formula_group2))
          # show arc 2pi0.4 animation
        text2 = MathTex(r'2\pi\times0.4').next_to(formula_group2,DOWN)
        self.play(Write(text2))
        self.wait() 

        vec_e.remove_updater(upvector_e)
        self.add(polar_graph.set_color(PURPLE))
        #vec_e.add_updater(upvector_polar_f) 
        self.play(FadeOut(vec_e))     
        self.add(dot_cartesian,dot_polar)

        self.play(tracker.animate.set_value(0))
        self.wait(0.5)
        self.play(tracker.animate.set_value(1),run_time=5),
        self.wait(0.5)
        self.play(tracker.animate.set_value(0.1),run_time=5)
        self.play(tracker.animate.increment_value(0.6),run_time=5)
        self.wait(0.5)      

        # winding animation
        self.play(ReplacementTransform(c_graph.copy(),polar_graph),
            run_time=3.5,
            path_arc = -TAU*2/3)
        self.wait()
        self.play(FadeOut(bar_group))
        self.wait()
        # CoM
        self.play(ReplacementTransform(formula0[1],formula2))
        self.wait() 
        self.play(Circumscribe(formula2[0]))
        self.wait() 
        self.play(ReplacementTransform(polar_graph.copy(),CoM))        
        self.wait() 
        formula_group1.next_to(formula_group2,RIGHT)
        self.play(FadeOut(formula_group2))
        self.add(formula_group1)
        self.wait()

        # changing the CoM with k & draw freq_domain
        self.play(ChangeDecimalToValue(Da,0),ChangeDecimalToValue(Dk,0)) #turn back to 0

        self.wait()
        self.play(ChangeDecimalToValue(Da,32),ChangeDecimalToValue(Dk,5.09),rate_func=rate_functions.linear,run_time=20)
        self.wait()

        # explanation on why there is peaks at frequency 5
            # Audio text: The reason behind might be that at this winding frequency, every period of f are just wound in one full circle, so we can gather all the peaks of f(t) on the right of the graph. Therefore by tracing the positon of CoM, we get feedback on whether the current k is similar to the true frequency of f. We are able to reveal the unknown frequencies of f(t) by looking at the position of CoM, with this mathematical wounding machine.

        # change f and see the polar
        #self.play(ReplacementTransform(polar_graph,polar_graph_new))

class test(Scene):
    def construct(self):
        def play_change_channel(change_to:int,run_time:float=1):
            graph_polar.remove_updater(up_polar_graph)
            dot_freqDomain.remove_updater(up_dot)
            self.__channel__= change_to
            self.play(
                Transform(graph_polar,get_pc(set_data['f_set'][change_to],_color=set_data['color_set'][change_to])),#改极坐标
                Transform(graph_label,set_data['graph_label_set'][self.__channel__]),#改直角坐标图像标签
                Transform(graph_c,set_data['graph_c_set'][self.__channel__]),#改直角坐标图像
                Transform(graph_freqD,freqD_axis.plot(get_freqDomain_sample,x_range=[0,15,0.1])),#改freqD图像
                dot_freqDomain.animate.move_to(get_dot_freqDomain(Da.get_value())),#质心点在freqD
                run_time=run_time#设置动画时间
                )
            self.bring_to_front(dot_freqDomain,graph_label)#将 直角坐标Tex、质心点 放在最前面
            dot_freqDomain.set_color(set_data['color_set'][self.__channel__])#修改质心点颜色

            dot_freqDomain.add_updater(up_dot)
            graph_polar.add_updater(up_polar_graph)

        #### Global variables ####
            #意思是现在选中需要扭转与分析的函数是哪一个（为了加updater显示不同颜色
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
        ],
        'color_set':[
            YELLOW_A,
            YELLOW_B,
            YELLOW_C,
            PINK,
            RED_A,
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
        c_axis = Axes(
            x_range=[0 , second + 0.1 , 1],y_range=[0, 2, 1],
            y_length=2,axis_config={"include_numbers": True},tips=False,
            ).to_edge(UP)
        c_axis_label = c_axis.get_axis_labels(x_label='time',y_label='intensity')
        for index,mathtex in enumerate(set_data['tex_set']):
            mathtex.set_color(set_data['color_set'][index]).scale(1.5).shift(UP*2.5)
        set_data['graph_label_set'] = [VGroup(_texf_,BackgroundRectangle(_texf_, color=WHITE, fill_opacity=0.15)) 
                                for _texf_ in set_data['tex_set']]

        set_data['graph_c_set'] = [c_axis.plot(set_data['f_set'][x],x_range=[0,second,0.01],color=set_data['color_set'][x])
                            for x in range(len(set_data['f_set']))]



        #### polar ####
        polar_axis = PolarPlane(radius_max=1.9,size=4.5).to_edge(DL)
        graph_polar = polar_axis.plot_parametric_curve(
            lambda t : [
                +np.cos(Da.get_value()*TAU*t) * (set_data['f_set'][0](t)),
                -np.sin(Da.get_value()*TAU*t) * (set_data['f_set'][0](t)),
                0
            ],t_range=[0,second,0.01],color=set_data['color_set'][0]
            ) 
        def get_pc(_func,_color=RED):
            return polar_axis.plot_parametric_curve(
                lambda t: [
                +np.cos(Da.get_value()*TAU*t) * (_func(t)),
                -np.sin(Da.get_value()*TAU*t) * (_func(t)),
                0
            ], t_range=[0, second, 0.01], color=_color)

        def up_polar_graph(obj): return obj.become(get_pc(set_data['f_set'][self.__channel__],set_data['color_set'][self.__channel__]))

        graph_polar.add_updater(up_polar_graph)

        #####freqDomain####
        t_min = 0;t_max = second
        scale = 1 / t_max - t_min
        freqD_axis = Axes(x_range=[0,15,1],y_range=[-0.1,0.8],
                x_length=7,y_length=3,
                axis_config={"include_numbers": True}).next_to(polar_axis,RIGHT).align_to(polar_axis,UP)
        freqD_axis_label = freqD_axis.get_axis_labels(x_label='freq(TAU)',y_label='')
        def get_freqDomain_sample(wind):
            return scale * scipy.integrate.quad(
                lambda t : set_data['f_set'][self.__channel__](t)*np.exp(complex(0, -TAU*wind*t)),
                t_min, t_max
                )[0].real

        graph_freqD = freqD_axis.plot(get_freqDomain_sample,x_range=[0,15,0.1])
        def get_dot_freqDomain(wind_freq):#'wind_freq'no need to times TAU
            color=set_data['color_set'][self.__channel__]
            return Dot(freqD_axis.input_to_graph_point(x=wind_freq,graph=graph_freqD),color=color)
        dot_freqDomain = get_dot_freqDomain(0.1)
        def up_dot(mob): return mob.become(get_dot_freqDomain(Da.get_value()))
        dot_freqDomain.add_updater(up_dot)


        label_Da = Text('Winding Freq:')
        group_Da = VGroup(label_Da,Da).arrange(RIGHT).next_to(freqD_axis,DOWN)

        ###############
        #绘制三个坐标轴
        self.add(c_axis,polar_axis,freqD_axis,
                 c_axis_label,freqD_axis_label)
        #绘制初始直角坐标图像
        self.add(graph_freqD,dot_freqDomain)
        #绘制Winding Freq动态数字
        self.add(group_Da)

        #现在场景中，除了三幅图像和一个点没画
        #绘制直角坐标的c_g_1 初始的
        graph_c = set_data['graph_c_set'][0].copy()
        graph_label = set_data['graph_label_set'][0].copy()
        self.play(Create(graph_c),FadeIn(graph_label))

        self.play(ReplacementTransform(graph_c.copy(),graph_polar),
            run_time=3.5,
            path_arc = -TAU*2/3)

        self.wait()
        self.play(ChangeDecimalToValue(Da,5,run_time=5))
        self.wait()
        play_change_channel(1)
        self.wait()
        self.play(ChangeDecimalToValue(Da,11,run_time=5))
        self.wait()
        play_change_channel(2)
        self.wait()
        self.play(ChangeDecimalToValue(Da,8,run_time=5))
        self.wait()
        play_change_channel(3)
        self.wait()
        self.play(ChangeDecimalToValue(Da,5,run_time=5))
        self.wait()
        play_change_channel(4)
        self.wait()
        self.play(ChangeDecimalToValue(Da,11,run_time=5))





class DFT_preparation(Scene):
    def construct(self):
        # After zoom in in Lib 散点图作为背景，虚化。前面显示以下。
        tex = Text("Dicrete Fourier Transform")
        formula = VGroup(*formula_set.formula_002)
        formula.arrange(DOWN,aligned_edge=LEFT,buff=0.8)

        second = 1
        y_scale = 0.5
        f = lambda x: y_scale*np.cos(30 * x)+y_scale
        ax = Axes(
            x_range=[0 , second , 1],
            y_range=[0, 1.1, 1],
            x_length=(7+1/9)*2*1.8,
            y_length=4*3/4,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)
        wave = ax.plot(f,color=YELLOW)
        group = VGroup(ax,wave).scale(0.5)
        ########################################################
        #                   Start Animation                    #
        ########################################################

        self.play(FadeIn(tex))
        self.wait()
        self.play(tex.animate.to_edge(UL),FadeIn(formula))
        self.wait()
        self.play(FadeOut(formula),FadeIn(group))
        self.wait()


class PlotDots(Scene):
    def Create_Dot_Set(self,axes,sample,Vg,run_time=1):
        dots_set = []
        _len_sample = int(len(sample))
        for x in range(_len_sample):
            dots_set.append(Dot(radius=0.02,color=BLUE_A,fill_opacity=0.8))
            dots_set[x].move_to(axes.c2p(x,sample[x]))
            self.add(dots_set[x])
            Vg.add(dots_set[x])
        return dots_set

    def construct(self):
        ########################################################
        #                     GET SAMPLE                       #
        ########################################################
        sample,_abs_big_ = sample_set.get_winter_wav()
        windows_dot_num = 2048
        shift = 10000

        sample_part=sample[shift:shift+windows_dot_num]
        _big_ = max([abs(max(list(sample_part))),abs(min(list(sample_part)))])
        
        
        print("样本点总数量:"+str(len(sample))+"\n当前节选样本区域:"+str(shift)+","+str(shift+windows_dot_num))

        #### manim_graph ####
        axes = Axes(x_range=(0,windows_dot_num+1,512),
                y_range=(-_big_,_big_,round((_big_)/2,2)),
                axis_config={"include_numbers": True},)
        #np.hanning(windows_dot_num)

        ax_TOTAL = VGroup(axes)
        dots_set = self.Create_Dot_Set(axes,sample_part,ax_TOTAL,run_time=1)

        formula_004 = formula_set.formula_004.to_edge(LEFT).scale(0.5)
        
        ########################################################
        #                   Start Animation                    #
        ########################################################
        self.add(axes)#Add coordinates()
        self.play(Write(formula_004),ax_TOTAL.animate.next_to(formula_004,RIGHT))
        _tc = 0 #temp Int_counter
        _ts=[] #temp Animation_set
        for dot in dots_set:
            if _tc <= 9 * 2:
                _ts.append(Transform(dot,formula_004[0][18+_tc:20+_tc]))
            _tc = _tc +2
        self.play(*_ts,run_time=3)
        self.wait()


class FormulaTest(Scene):
    def construct(self):
        formula_002 = formula_set.formula_002[0].shift(UP)
        formula_003 = formula_set.formula_002[1].next_to(formula_002, DOWN)

        formula_002[0][11:13].color=YELLOW 

        ########################################################
        #                  Start Animation                     #
        ########################################################
        self.add(formula_002[0],formula_003) 
        self.play(Write(formula_002[0]), Write(formula_002[1]), run_time=2)
        self.play(formula_002[0][11:13].animate.set_color(YELLOW))
        self.play(Wiggle(formula_002[0][11:13]))
        self.play(Indicate(formula_002[0][11:13]))  
        self.wait()

#连续图像上打点，然后扭动
    #After Change the dot number,need to delete the cached data.
class DFT_Illustration(Scene):
    def construct(self):
        #### Global variables ####
        ## Duration of sound wave
        second = 3
        ## Winding frequency
        a = 1
        Da = DecimalNumber(a)
        ## Ini Dot
        num_OF_DOT = 128
        
        #### formulas ####
        formula_004 = formula_set.formula_004.to_edge(RIGHT)
        formula_006 = formula_set.formula_006
        formula_006[0].next_to(formula_004,LEFT)

        #### functions ####
        f = lambda x: 0.5*np.cos(3*2*PI*x)+0.5

        Wind_f =lambda t : [
                +np.cos(Da.get_value()*t) * (f(t)),
                -np.sin(Da.get_value()*t) * (f(t)),
                0
            ]

        #### manim_graph ###a#
        ax = PolarPlane(radius_max=1,size=7)

        #### Curve Mobject ####
        def _get_curve_graph_(func):
            return ax.plot_parametric_curve(
                func,
                t_range=[0,second],
                color=YELLOW)
        curve = _get_curve_graph_(Wind_f)

        #### Dot Mobject ####
        def _set_plot_dot_(D_set,curve):
            for value in range(num_OF_DOT+1):
                position = ax.i2gp(graph=curve,x=value*second/num_OF_DOT)
                D_set.append(Dot(color=WHITE).move_to(position))
        _dot_set = []
        _set_plot_dot_(_dot_set,curve)

        ########################################################
        #                  UPDATE FUNCTION                     #
        ########################################################
        
        def upfunc(curve):
            curve.become(_get_curve_graph_(Wind_f))

        def up_dots(curve):
            new_dot_set = []
            _set_plot_dot_(new_dot_set,curve)
            for dot,new_dot in zip(_dot_set,new_dot_set):
                dot.move_to(new_dot)
            self.add(*_dot_set)

        ####Add updater####
        curve.add_updater(up_dots)
        curve.add_updater(upfunc)


        ########################################################
        #                  Start Animation                     #
        ########################################################
        #self.play(Write(formula_004),Write(formula_006[0]))
        #self.play(FadeOut(formula_004,formula_006[0]))

        self.add(ax, curve)
        self.play(ChangeDecimalToValue(Da,15,rate_func=rate_functions.linear),run_time=20)

        
class DFT_RealData(Scene):
    def Create_DotSet_Polar(self,axes,sample,Vg,freq=0,run_time=1):
        dots_set = []
        _len_sample = int(len(sample))
        for x in range(_len_sample):
            dots_set.append(Dot(radius=0.02,color=BLUE_A,fill_opacity=0.8))
            dots_set[x].move_to(axes.polar_to_point(sample[x],x/_len_sample*freq))
            Vg.add(dots_set[x])
        return dots_set

    def construct(self):
        ########################################################
        #                     GET SAMPLE                       #
        ########################################################
        sample,_abs_big_ = sample_set.get_winter_wav()
        windows_dot_num = 512
        shift = 10000

        sample_part=abs(sample[shift:shift+windows_dot_num])
        _big_ = max([abs(max(list(sample_part))),abs(min(list(sample_part)))])
        
        print("number of sample:"+str(len(sample))+"\ncurrent interval:"+str(shift)+","+str(shift+windows_dot_num))

        #### manim_graph ####
        polar_axis = Axes(x_range=(-_big_,_big_),
                y_range=(-_big_,_big_),
                x_length=8,y_length=8,
                axis_config={"include_numbers": True})
        graph_total = VGroup(polar_axis)

        polar_data = self.Create_DotSet_Polar(polar_axis, sample_part,graph_total)
        
        ########################################################
        #                  Start Animation                     #
        ########################################################
        
        self.add(polar_axis,*polar_data)
        
        旋转圈数 = 3
        播放倍数 = 1
        _精细度_ = config.frame_rate*旋转圈数/播放倍数
        for x in range(int(_精细度_)+1):
            new_dots=self.Create_DotSet_Polar(polar_axis, sample_part,graph_total,(x)/(_精细度_)*TAU*旋转圈数)#即绕一个圈中间有多少帧
            count=-1;ani_set=[]
            for obj in polar_data:
                count=count+1
                ani_set.append(Transform(obj,new_dots[count]))
            self.play(*ani_set,run_time=1/config.frame_rate,rate_func=rate_functions.linear)


class STFT(Scene):
    def construct(self):
        self.wait()
        # formula_004a = MathTex(r"e^{-i 2 \pi(2(0)) / 19")
        # self.add_subcaption("Hello sub!", duration=1)
        # self.play(Write(formula_004a))


class M_Shift(Scene):
    def Create_Dot_Set(self,axes,sample,Vg,run_time=1):
        dots_set = []
        _len_sample = int(len(sample))
        for x in range(_len_sample):
            dots_set.append(Dot(radius=0.02,color=BLUE_A,fill_opacity=0.8))
            dots_set[x].move_to(axes.c2p(x,sample[x]))
            #self.add(dots_set[x])
            Vg.add(dots_set[x])
        return dots_set

    def Create_DotSet_Polar(self,axes,sample,Vg,freq=0,run_time=1):
        dots_set = []
        _len_sample = int(len(sample))
        for x in range(_len_sample):
            dots_set.append(Dot(radius=0.02,color=BLUE_A,fill_opacity=0.8))
            dots_set[x].move_to(axes.polar_to_point(sample[x],x/_len_sample*freq))
            Vg.add(dots_set[x])
        return dots_set
#方案：
#1、先往左边移动，然后Transform到新的点集
    def drew_Manim_Graph(self,sample,windows_dot_num,shift):

            sample_part=sample[shift:shift+windows_dot_num]
            _big_ = max(sample)

            print("number of sample:"+str(len(sample))+"\ncurrent interval:"+str(shift)+","+str(shift+windows_dot_num))
            
            #### manim_graph ####
            axes = Axes(x_range=(0,windows_dot_num+1,512),
                y_range=(-_big_,_big_,round((_big_)/2,2)),
                axis_config={"include_numbers": True},)
        
            text_pos = VGroup(Text('Time Domain x_range:',font_size=22),
                          Text('['+str(shift)+','+str(shift+windows_dot_num)+']',font_size=22))

            text_pos.arrange(DOWN,aligned_edge=ORIGIN,buff=0.2).to_edge(UP)
        
            #np.hanning(windows_dot_num)

            ax_TOTAL = VGroup(axes).next_to(text_pos,DOWN)
            dots_set = self.Create_Dot_Set(axes,sample_part,ax_TOTAL)

            #self.add(ax_TOTAL,text_pos)#Add coordinates()
            #self.add(text_pos)
            
            self.wait()
            return ax_TOTAL,VGroup(*dots_set)

    def construct(self):
        ########################################################
        #                     GET SAMPLE                       #
        ########################################################
        sample,_abs_big_ = sample_set.get_winter_wav()
        windows_dot_num = 256
        shift = 10000
        ax_TOTAL=VMobject();temp_ax_TOTAL = VMobject()
        text_pos=VMobject();temp_text_pos = VMobject()
        temp_ax_TOTAL,temp_text_pos=self.drew_Manim_Graph(sample,windows_dot_num,shift)

        for x in range(10):
            shift=int(shift+windows_dot_num/2)
            #self.remove(ax_TOTAL,text_pos)
            ax_TOTAL,text_pos=self.drew_Manim_Graph(sample,windows_dot_num,shift)
            self.play(Transform(temp_ax_TOTAL,ax_TOTAL),Transform(temp_text_pos,text_pos))

class uAndM(Scene):
    def construct(self):
        ss = ImageMobject('uam.jpeg').scale(0.8)
        self.play(FadeIn(ss))
        