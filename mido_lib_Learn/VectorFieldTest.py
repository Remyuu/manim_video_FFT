'''
2022-7-26
Learn Vector field Rend
Using StreamLines

'''
from manim import *

#一张图片
class VF001(Scene):
    def construct(self):
        function01 = lambda p : np.cos(p[0])+np.sin(p[1])
        sl = StreamLines(function01)
        self.add(sl)

#配置StreamLines的参数
#Defalut : min_color_scheme_value=0, max_color_scheme_value=2, 
    #colors=['#236B8E', '#83C167', '#FFFF00', '#FC6255'], 
    #three_dimensions=False, 
    #noise_factor=None, n_repeats=1, dt=0.05, virtual_time=3, 
    #max_anchors_per_line=100, 
    #padding=3, stroke_width=1, opacity=1,

    #x_range y_range -- x_min,x_max,delta_x /...
    #color & color_scheme -- Set color
    #noise_factor -- Default:delta_y/2
    #max_anchors_per_line -- complicated,Change the number of anchors per line 平滑度咯 3就够了
class VF002(Scene):
    def construct(self):
        function01 = lambda p : np.cos(p[0])+np.sin(p[1])*LEFT
        sl = StreamLines(function01,
            x_range=[-6,6,0.2],y_range=[-4,4,0.2],
            #color=[RED,GREEN_D,BLUE_B],
            noise_factor=0.2,
            max_anchors_per_line = 3,
            
            )
        self.add(sl)

#Test Methods 
#############DO NOT use #1,2 with #3#############
    #1 create -- The creation of the StreamLines 
        # -- return:Animation 
    #2 end_animation -- smooth ending 
        # -- return:Animation 
    #3 start_animate -- using the updater to animates the StreamLines 
        # -- return:None
class VF003(Scene):
    def construct(self):
        function01 = lambda p : np.cos(p[0])+np.sin(p[1])*LEFT
        sl = StreamLines(function01,x_range=[-2,2,0.1],y_range=[-1,1,0.2],
            virtual_time=2,
            max_anchors_per_line = 10,#better performance to render
        )
        sl_animate = StreamLines(function01,virtual_time=4)
        self.play(sl.create())#run_time depends on virtual_time 
        self.wait(1)
        #sl.start_animation(warm_up=True,flow_speed=2,time_width=0.5) 
        self.play(sl.end_animation())#run_time depends on virtual_time 

#start_animation -- Default:warm_up=True, flow_speed=1, time_width=0.3, rate_func=<function linear>
class VF004(Scene): 
    def construct(self):
        func = lambda pos : np.sin(pos[0])+np.cos(pos[1])
        sl = StreamLines(func,stroke_width=3,max_anchors_per_line=50)
        self.add(sl)
        sl.start_animation(flow_speed=2)
        self.wait(10)


#animate with updater
class VF005(Scene):
    def construct(self):
        rou1 = DecimalNumber(1)
        rou2 = DecimalNumber(1)
        function01 = lambda p : np.cos(rou1.get_value()*p[0])+np.sin(rou2.get_value()*p[1])
        sl = StreamLines(function01,x_range=[-2,2,0.1],y_range=[-1,1,0.2])
        upfunc = lambda mob : mob.become(StreamLines(function01,
            x_range=[- 2,2,0.1],y_range=[-1,1,0.2],
            max_anchors_per_line=5))
        sl.add_updater(upfunc)
        self.add(sl)
        self.play(ChangeDecimalToValue(rou1,5),ChangeDecimalToValue(rou2,5),run_time=5)

        #Render Speed Is Very LOW!!!

#animate with updater
class VF999(Scene):
    def construct(self):
        dt = 0.1
        function01 = lambda p : np.cos(p[0])+np.sin(p[1])*LEFT
        sl = StreamLines(function01,x_range=[-2,2,0.1],y_range=[-1,1,0.2])
        upfunc = lambda mob : mob.become(StreamLines(function01,x_range=[-2,2,0.1],y_range=[-1,1,0.2]))
        sl.add_updater(upfunc)
        self.add(sl)
      