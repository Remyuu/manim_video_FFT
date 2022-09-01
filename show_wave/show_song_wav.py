'''
此工程使用manimlib
控制台使用

manimgl show_song_wav.py show_song_wav -ow --uhd 

编译
----------------------------
--low_quality
-l
使用低质量渲染(默认 480p15)
--medium_quality
-m
使用中等质量渲染(默认 720p30)
--hd
使用高质量渲染(默认 1080p30)
--uhd
使用 4K 质量渲染

'''


from manim import *
import librosa

dir = 'wav_dir'

class show_song_wav(Scene):
    def construct(self):
        WAVE_FILE,FS = librosa.load(dir+'/Example01_BreakAndColumn.wav')
        SUM_NUM = len(WAVE_FILE) #number of discrate point
        WAVE_TIME = SUM_NUM/FS #Aduio Clip Last Time (s)
        SAMPLE_DENSITY = 1 #the density of point
 
        wave_show = WAVE_FILE[::SAMPLE_DENSITY]
        len_wave_show = len(wave_show)

        print(str(len_wave_show)+'/'+str(SUM_NUM)+'\n'+"SAMPLE_DENSITY:"+str(len_wave_show/SUM_NUM))

        ax,graph = self.get_graph(wave_show,len_wave_show)#得到图像与坐标


#################show_part##################
#1-show wave
        self.show_wave(ax,graph)

#2-zoom camera
        new_axes, graph_snippet = self.show_zoom_camera(axes=ax,graph=graph,zoom_start=0.5,zoom_rect_dims=(0.4, 5.0))


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
            run_time=5,
            rate_func=squish_rate_func(linear, 0.05, 1))
        self.wait()
        

    def show_zoom_camera(self, axes, graph, zoom_start,zoom_rect_dims,run_time = 8):
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

        new_axes = Axes((-2, 12), (-1, 1, 0.25), width=7+1/9 + 1)
        new_axes.shift(new_axes.get_origin())

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
