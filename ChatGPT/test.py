from manim import *
import numpy as np

class IntegralPlot(Scene):
    def construct(self):
        # axes = Axes(
        #     x_range=[0, PI/4, PI/16],
        #     y_range=[0, 1, 0.5],
        #     x_length=5,
        #     y_length=3
        # )
        # func = ParametricFunction(lambda t: np.array([t, np.sin(t), 0]), color=BLUE)
        axes = Axes((0,4), (-1.1,1.1))
        axes.add_coordinates()
        func = axes.plot(lambda x: np.sin(x))
        self.play(Create(axes), Create(func))
        self.wait(1)

        # area = axes.get_area(graph=func, x_range=(0, PI/4))
        area = axes.get_area(graph=func, x_range=(0, (PI/4)))#dx_scaling=0.5)#, area_opacity=0.3, color=YELLOW)
        self.play(Create(area), run_time=2)
        result = ParametricFunction(lambda t: np.array([t, np.cos(t) - 1, 0]), t_range=[0, PI/4], color=RED)
        # self.play(Write(result))
        self.play(Transform(func, result))
        self.wait(5)