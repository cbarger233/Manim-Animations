from turtle import fillcolor
from manim import *
import numpy as np
import random


class FastBacteria(Dot):
    def __init__(self, point=ORIGIN, ** kwargs):
        Dot.__init__(self, point=point, color=RED, ** kwargs)

        vel = 5
        intervals = [[2.0, 2.4], [-2.4, -2.0]]
        random.uniform(*random.choices(intervals, weights=[r[1]-r[0] for r in intervals])[0])
        speeds = np.asarray([random.uniform(*random.choices(intervals,weights=[r[1]-r[0] for r in intervals])[0]) for i in range(2)])
        speeds = np.append(speeds, np.sqrt(vel**2 + speeds[0]**2 + speeds[1]**2))
        self.velocity = speeds
        self.speed = np.sqrt(speeds[0]**2 + speeds[1]**2)

    def update_speed(self):
        speed = self.velocity
        speed[0] = speed[0] * 0.56
        speed[1] = speed[1] * 0.56
        speed[2] = speed[2] * 0.56
        self.velocity = speed

class SlowBacteria(Dot):
    def __init__(self, point=ORIGIN, ** kwargs):
        Dot.__init__(self, point=point, color=BLUE, ** kwargs)

        vel = 1
        intervals = [[0.8, 1.2], [-1.2, -0.8]]
        random.uniform(*random.choices(intervals, weights=[r[1]-r[0] for r in intervals])[0])
        speeds = np.asarray([random.uniform(*random.choices(intervals,weights=[r[1]-r[0] for r in intervals])[0]) for i in range(2)])
        speeds = np.append(speeds, np.sqrt(vel**2 + speeds[0]**2 + speeds[1]**2))
        self.velocity = speeds
        self.speed = np.sqrt(speeds[0]**2 + speeds[1]**2)

    def update_speed(self):
        speed = self.velocity
        speed[0] = speed[0] * 1.25
        speed[1] = speed[1] * 1.25
        speed[2] = speed[2] * 1.25
        self.velocity = speed

class Demon(VGroup):
    def __init__(self, ** kwargs):
        VGroup.__init__(self, ** kwargs)
        self.head = Dot(radius=0.18, fill_color=RED)
        self.body = Line(color=RED, start=self.head.get_center(), end=[0, -0.7, 0], stroke_width=12)
        self.left_arm = Line(color=RED, start=self.head.get_bottom(), end=[-0.3, -0.6, 0], stroke_width=8)
        self.right_arm = Line(color=RED, start=self.head.get_bottom(), end=[0.3, -0.6, 0], stroke_width=8)
        self.left_leg = Line(color=RED, start=self.body.get_bottom(), end=[-0.2, -1.2, 0], stroke_width=8)
        self.right_leg = Line(color=RED, start=self.body.get_bottom(), end=[0.2, -1.2, 0], stroke_width=8)
        self.left_ear = Triangle(color=RED).scale(0.06).move_to(self.head.get_corner(direction=UL)).rotate(30*DEGREES)
        self.right_ear = Triangle(color=RED).scale(0.06).move_to(self.head.get_corner(direction=UR)).rotate(-30*DEGREES)
        body_start = self.body.get_start()

        self.add(self.head, self.body, self.left_arm, self.right_arm, self.left_leg, self.right_leg, self.left_ear, self.right_ear)

    def wave_arm(self, scene):
        scene.play(Rotate(
            self.right_arm,
            angle=90*DEGREES,
            about_point=self.right_arm.get_start(),
            rate_func=linear
        ),
        Rotate(
            self.left_arm,
            angle=-90*DEGREES,
            about_point=self.left_arm.get_start(),
            rate_func=linear
        )
        )
        scene.play(Rotate(
            self.right_arm,
            angle=-90*DEGREES,
            about_point=self.right_arm.get_start(),
            rate_func=linear
        ),
        Rotate(
            self.left_arm,
            angle=90*DEGREES,
            about_point=self.left_arm.get_start(),
            rate_func=linear
        )
        )
    
    def walk(self, scene, steps):
        scene.play(Rotate(
            self.left_arm,
            angle=35*DEGREES,
            about_point=self.left_arm.get_start(),
            rate_func=linear
        ),
        Rotate(
            self.right_arm,
            angle=-5*DEGREES,
            about_point=self.right_arm.get_start(),
            rate_func=linear
        ))
        for i in range(0, steps):
            #first step
            scene.play(Rotate(
                self.left_leg,
                angle = 45*DEGREES,
                about_point=self.left_leg.get_start(),
                rate_func=linear
            ),
            Rotate(
                self.right_leg,
                angle=-45*DEGREES,
                about_point=self.right_leg.get_start(),
                rate_func=linear
            ),
            Rotate(
                self.left_arm,
                angle=40*DEGREES,
                about_point=self.left_arm.get_start(),
                rate_func=linear
            ),
            Rotate(
            self.right_arm,
            angle=-40*DEGREES,
            about_point=self.right_arm.get_start(),
            rate_func=linear
        ))
            #second step
            scene.play(Rotate(
                self.left_leg,
                angle = -45*DEGREES,
                about_point=self.left_leg.get_start(),
                rate_func=linear
            ),
            Rotate(
                self.right_leg,
                angle=45*DEGREES,
                about_point=self.right_leg.get_start(),
                rate_func=linear
            ),
            Rotate(
                self.left_arm,
                angle=-40*DEGREES,
                about_point=self.left_arm.get_start(),
                rate_func=linear
            ),
            Rotate(
                self.right_arm,
                angle=40*DEGREES,
                about_point=self.right_arm.get_start(),
                rate_func=linear
            ))

class DemonViolation(Scene):
    def construct(self):
        my_object = Demon()
        self.play(Create(my_object))
        #my_object.wave_arm(self)
        my_object.walk(self, 5)
        #self.play(Rotate(my_object.right_arm, angle=100*DEGREES, about_point=my_object.right_arm.get_start(), rate_func=linear))
        self.wait()