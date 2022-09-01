'''###Update inf###
    8.23
        完成了Freq_Domain_Curve,利用manimlib提高了渲染效率。
    8.24
        优化Freq_Domain_Curve代码,提高渲染效率、渲染曲线更平滑。
        更新Freq_Domain_Curve,添加了区域标识。


此工程使用manimlib
控制台使用
manimgl MainVideoLib.py      -ow --uhd 
----------------------------
--low_quality
-l 使用低质量渲染(默认 480p15) --medium_quality
-m 使用中等质量渲染(默认 720p30)
--hd 使用高质量渲染(默认 1080p30)
--uhd 使用 4K 质量渲染
'''

from manimlib import *
import numpy as np
import librosa
import scipy

dir = 'wav_dir'

class show_song_wav(Scene):
    def get_graph(self,wave_show,len_wave_show):
        ax = Axes(
            x_range=[0, len_wave_show,len_wave_show],
            y_range=[-1, 1, 1],

        )
        
        xs = np.arange(len_wave_show)
        points = ax.c2p(xs, wave_show)
        graph = VMobject()
        graph.set_points_as_corners(points)

        return ax,graph

    def show_wave(self,ax,graph):
        self.play(Write(ax))
        self.play(Write(graph),
            run_time=2,
            rate_func=squish_rate_func(linear, 0.05, 1))
        self.wait(0.1)
        

    def show_zoom_camera(self, axes, graph, zoom_start,zoom_rect_dims,run_time = 4):
        point = graph.point_from_proportion(zoom_start) * RIGHT
        zoom_rect = Rectangle(*zoom_rect_dims)
        zoom_rect.move_to(point)
        zoom_rect.set_stroke(BLUE, 2)

        graph_snippet = VMobject()
        graph_points = graph.get_anchors()
        lx = zoom_rect.get_left()[0]
        rx = zoom_rect.get_right()[0]
        xs = graph_points[:, 0]
        snippet_points = graph_points[(xs > lx) * (xs < rx)]
        graph_snippet.set_points_as_corners(snippet_points)
        graph_snippet.match_style(graph)
        point = graph_snippet.get_center().copy()
        point[1] = axes.get_origin()[1]
        zoom_rect.move_to(point)

        movers = [axes, graph, graph_snippet, zoom_rect]

        frame = self.camera.frame
        for mover in movers:
            mover.save_state()
            mover.generate_target()
            mover.target.stretch(frame.get_width() / zoom_rect.get_width(), 0, about_point=point)
            mover.target.stretch(frame.get_height() / zoom_rect.get_height(), 1, about_point=point)
            mover.target.shift(-point)
        graph_snippet.target.set_stroke(width=3)
        zoom_rect.target.set_stroke(width=0)
        axes.target.set_stroke(opacity=0)

        new_axes = Axes(x_range=[0, 40,1],
            y_range=[-1, 1, 1],)
        #new_axes.shift(new_axes.get_origin())

        self.play(Write(zoom_rect))
        self.play(
            *map(MoveToTarget, movers),
            FadeIn(new_axes),
            run_time=run_time,
        )
        self.remove(graph, axes)

        # Swap axes

        # if fade_in_new_axes:
        #     self.play(FadeIn(new_axes))

        self.original_graph = graph
        self.original_axes = axes
        self.axes = new_axes
        self.graph = graph_snippet

        return new_axes, graph_snippet


    def construct(self):
        WAVE_FILE,FS = librosa.load('Example01_BreakAndColumn.wav')
        SUM_NUM = len(WAVE_FILE) #number of discrate point
        WAVE_TIME = SUM_NUM/FS #Aduio Clip Last Time (s)
        SAMPLE_DENSITY = 1 #the density of point
 
        wave_show = WAVE_FILE[::SAMPLE_DENSITY]
        len_wave_show = len(wave_show)

        print(str(WAVE_FILE)+'/'+str(SUM_NUM)+'\n'+"SAMPLE_DENSITY:"+str(len_wave_show/SUM_NUM))

        ax,graph = self.get_graph(wave_show,len_wave_show)#得到图像与坐标

#################show_part##################
#1-show wave


        self.show_wave(ax,graph)

#2-zoom camera
        new_axes, graph_snippet = self.show_zoom_camera(axes=ax,graph=graph,zoom_start=0.5,zoom_rect_dims=(0.1, 5.0))
        #self.remove(new_axes, graph_snippet)
        D_set = [] ;vg = VGroup()
        for value in range(43):
            position = new_axes.i2gp(graph=graph_snippet,x=value-1)
            dot = Dot(color=YELLOW)
            dot.move_to(position)
            D_set.append(dot)
            vg.add(dot)
            #self.play(FadeIn(dot))
        self.wait()
        self.play(Write(vg),FadeOut(graph_snippet))
        self.wait()
        new_axes, graph_snippet = self.show_zoom_camera(axes=new_axes,graph=graph_snippet,zoom_start=0.5,zoom_rect_dims=(0.1, 5.0))
        
        D_set = [] ;vg = VGroup()
        
        for value in range(43):
            position = new_axes.i2gp(graph=graph_snippet,x=value-1)
            dot = Dot(color=YELLOW)
            dot.move_to(position)
            D_set.append(dot)
            vg.add(dot)
            #self.play(FadeIn(dot))
        self.wait()
        self.play(Write(vg),FadeOut(graph_snippet))
        self.wait()

#Freq_Domain_Curve
class OutPutFFTClip(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 4000, 1000],
            y_range=[0, 90, 30],
            axis_config={"include_numbers": True},
        )
        yy44,fs44 = librosa.load('winter.wav')

        Dmove_step = Integer(0)
        f_size = 2048
        n_hop = f_size / 2

        _MAX_SAFE_STEP = (np.round(len(yy44))-np.round(len(yy44))%n_hop)/n_hop-1
        _SONG_TIME = len(yy44)/fs44

        #在窗大小为:2048下的xf索引值:187 约等于 freq=4000，所以limit_sample_length这样写。
        def get_freqDomain(show_dot=False,smoothly=True,line_color=RED,limit_sample_length=int(187*f_size/2048)):
            step = int(Dmove_step.get_value())
            n1 = int(n_hop*step)
            n2 = int(n_hop*step + f_size)
            x_i = yy44[n1:n2]

            X_i = np.abs(scipy.fft.rfft(x_i * np.hanning(len(x_i))))
            xf = scipy.fft.rfftfreq(f_size,1/44100)
            x_values, y_values = map(np.array, (xf[0:limit_sample_length], X_i[0:limit_sample_length]))
            line_graph = VGroup(color=line_color)
            vertices = [
                ax.c2p(x, y)
                for x, y in zip(x_values, y_values)
            ]
            line_graph.set_points_as_corners(vertices)

            if smoothly:
                line_graph.make_approximately_smooth()
                
            if show_dot:
                dot_graph = Group(
                    *(Dot(point=vertex, radius=0.5) for vertex in vertices)
                )
                return line_graph,dot_graph

            return [line_graph]
        
        def get_label():
            step = int(Dmove_step.get_value())
            n1 = int(n_hop*step)
            n2 = int(n_hop*step + f_size)
            label_g = Group(
                Text("Frequency Domain"),
                Text("HanningWindow:{}/{}".format(step,_MAX_SAFE_STEP),font_size=32),
                Text("[{},{}]".format(n1,n2),font_size=32)
                )
            label_g.arrange(DOWN,buff=0.2)
            return label_g
        up_graph = lambda mob: mob.become(get_freqDomain()[0])
        up_label = lambda mob :mob.become(get_label())

        lab = get_label()
        self.add(ax,lab)
        
        self.play(ChangeDecimalToValue(Dmove_step,_MAX_SAFE_STEP),
                UpdateFromFunc(Dmove_step,up_graph),
                UpdateFromFunc(lab, up_label)
                ,run_time=_SONG_TIME,rate_func=linear)

class show_hanning_windows(Scene):
    def plot(self,x_value,y_value,ax,show_dot=True):
        x_values, y_values = map(np.array,(x_value, y_value))
        graph = VGroup(color=RED)
        vertices = [
            ax.coords_to_point(x, y)
            for x, y in zip(x_values, y_values)
        ]
        graph.set_points_as_corners(vertices)
        if show_dot:
            vertex_dots = VGroup(*(
                    Dot(point=vertex, radius=0.02)
                    for vertex in vertices))
            return [graph,vertex_dots]
        return [graph]

    def construct(self):
        f_size = 1024
        ax = Axes(
            x_range=[0, f_size, f_size/4],
            y_range=[0, 1, 0.5],
            axis_config={"include_numbers": True},
        )
        graph ,dot_set= self.plot(range(f_size),np.hanning(f_size),ax,show_dot=True)
        self.play(FadeIn(ax))
        self.play(Write(graph),Write(dot_set))

        