'''
'Almost' Fourier Transformation (Dynamic)


'''

from manim import *
import scipy.integrate

class FourierTrans_First(Scene):
    def construct(self):
        ######### parameters #########
        #intial
        rou1 = 1*TAU  # frequency*2*pi
        rou2 = 2*TAU
        rou3 = 3*TAU
        move = 2 # coeficient for polar coordinate transform

        ########################################

        dn_kwargs = {'num_decimal_places':3,}
        D_rou1 = DecimalNumber(rou1,**dn_kwargs).shift(RIGHT)
        D_rou2 = DecimalNumber(rou2,**dn_kwargs).shift(RIGHT*2)
        D_rou3 = DecimalNumber(rou3,**dn_kwargs).shift(RIGHT*3)
        D_move = DecimalNumber(move,**dn_kwargs).next_to(D_rou1,DOWN)

        ####### The signal function #######
        # cos(2*pi*t)+cos(2*2*pi*t)+cos(3*2*pi*t)
        r = lambda t: \
            np.cos(D_rou1.get_value()*t)+\
            np.cos(D_rou2.get_value()*t)+\
            np.cos(D_rou3.get_value()*t)
        ############################################

        par = lambda t: np.array([
            (r(t))*np.cos(D_move.get_value()*t),
            (r(t))*np.sin(D_move.get_value()*t),
            0])


        #coordinate system & labels
        axes = Axes(
            x_range=[-1, 5, 0.5],
            y_range=[-2.1, 2.5, 1],
            x_length=14,
            y_length=2,
            axis_config={"include_numbers": True},
            ).to_edge(UP)
        axes_label = axes.get_axis_labels('Time','Intensity')

        #polar plane
        polarPlane = PolarPlane(
            radius_max=2.0,
            azimuth_units="TAU radians",
            size=4,
            azimuth_label_font_size=24,
            radius_config={"font_size": 24},
            ).add_coordinates().to_edge(DOWN+LEFT)

        #point track plane
        pointAxes = Axes(
            x_range=[0, 6,1],
            y_range=[-0.5, 1],
            x_length=7,
            y_length=4
            ).to_edge(UP).to_edge(DOWN+RIGHT)


    
        def Func_axes():
            return axes.plot(r,color=PINK)
    
        def Func_polar():
            return polarPlane.plot_polar_graph(r, [0, 2 * PI,0.1], color=ORANGE)

        def Func_para():
            para = ParametricFunction(
                par, 
                t_range = np.array([0, 3.14*2]),
                fill_opacity=0)\
                    .set_color(color=[RED,YELLOW,BLUE,RED])
            return para

        def Func_fourier_graph():
            def get_fourier_transform(
                func, t_start, t_end,
            ):
                scal = 1.0/(t_end-t_start)
                def fourier_trans(f):
                    return scal * scipy.integrate.quad(
                        lambda t: func(t)*np.exp(complex(0, -TAU*f*t)),
                        t_start, t_end
                    )[0].real
                return fourier_trans

            return pointAxes.plot(
                get_fourier_transform(r,t_start=0,t_end=3), 
                )
            

        axes_graph = Func_axes()
        polar_graph = Func_polar()
        para_graph = Func_para()
        freq_graph = Func_fourier_graph()


        # Add updater
        axU = lambda mob: mob.become(Func_axes())
        poU = lambda mob: mob.become(Func_polar())
        paU = lambda mob: mob.become(Func_para().shift(DOWN+RIGHT*3))
        frU = lambda mob: mob.become(Func_fourier_graph().move_to(freq_graph))
        
        axes_graph.add_updater(axU)
        polar_graph.add_updater(poU)
        para_graph.add_updater(paU)
        freq_graph.add_updater(frU)


        ################################################
        #################### Start Animation ###########
        ################################################

      
        group_axes = VGroup(axes,axes_label,axes_graph) 
        group_polar = VGroup(polarPlane)

        self.add(D_rou1,D_move)

        self.play(Write(group_axes),Write(group_polar),run_time=0.1)

        para_graph.remove_updater(paU)

        self.play(GrowFromCenter(pointAxes),run_time=0.1)

        self.add(freq_graph)

        self.play(
            ChangeDecimalToValue(D_rou1,3*TAU),
            ChangeDecimalToValue(D_rou2,4*TAU),
            ChangeDecimalToValue(D_rou3,5*TAU),
            run_time=3,
            rate_func=linear)
        self.play(
            ChangeDecimalToValue(D_rou1,3*TAU),
            ChangeDecimalToValue(D_rou2,1*TAU),
            ChangeDecimalToValue(D_rou3,6*TAU),
            run_time=3,
            rate_func=linear)
        self.add(pointAxes)
        self.wait(1)