from pickle import TRUE
from turtle import fillcolor, width
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

    def update_speed(self):
        speed = self.velocity
        speed[0] = speed[0] * 1.25
        speed[1] = speed[1] * 1.25
        speed[2] = speed[2] * 1.25
        self.velocity = speed

class NormalBacteria(Dot):
    def __init__(self, point=ORIGIN, ** kwargs):
        Dot.__init__(self, point=point, color=GREEN, radius=0.04, ** kwargs)

        vel = 3.8
        intervals = [[1.5, 2.2], [-2.2, -1.5]]
        random.uniform(*random.choices(intervals, weights=[r[1]-r[0] for r in intervals])[0])
        speeds = np.asarray([random.uniform(*random.choices(intervals,weights=[r[1]-r[0] for r in intervals])[0]) for i in range(2)])
        speeds = np.append(speeds, np.sqrt(vel**2 + speeds[0]**2 + speeds[1]**2))
        self.velocity = speeds

    def update_speed(self):
        speed = self.velocity
        speed[0] = speed[0] * 0.56
        speed[1] = speed[1] * 0.56
        speed[2] = speed[2] * 0.56
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


class BouncingBacteria(Scene):
    def construct(self):
        # Create objects
        box = Rectangle(width=5, height=5, fill_color=BLUE, fill_opacity=0.25).shift(LEFT*2.5)
        box2 = Rectangle(width=5, height=5, fill_color=RED, fill_opacity=0.25).shift(RIGHT*2.5)
        big_box = Rectangle(width=10, height=5, fill_color=YELLOW_A, fill_opacity=0.14)
        second_law = Text("Second Law of Thermodynamics", font_size=40).next_to(box.get_right(), UP)
        second_law.shift(UP*2.3)
        self.play(FadeIn(box, box2, second_law))

        # Creation of the slower bacteria, placing them randomly in the left box
        slow_bacteria_array = []
        for i in range(0, 10):
            bacteria_position = np.array([random.uniform(-4.5, -0.5), random.uniform(-2, 2), random.random()])
            slow_bacteria_array.append(SlowBacteria(bacteria_position))
        list_bact_slow = VGroup(*[bact for bact in slow_bacteria_array])
        self.play(FadeIn(list_bact_slow))

        # Creation of the faster bacteria, placing them randomly in the right box
        fast_bacteria_array = []
        for i in range(0, 10):
            bacteria_position = np.array([random.uniform(0.5, 4.5), random.uniform(-2, 2), random.random()])
            fast_bacteria_array.append(FastBacteria(bacteria_position))
        list_bact_fast = VGroup(*[bact for bact in fast_bacteria_array])
        self.play(FadeIn(list_bact_fast))

        # Collision detection for the left box
        def update_slow_bacteria(bacteria, dt):
            bacteria.acceleration = 2 * np.random.random_sample(3) - 1 # [-1, 1] interval
            bacteria.velocity = bacteria.velocity + bacteria.acceleration * dt
            bacteria.shift(bacteria.velocity * dt)

            # Bounce off walls
            if bacteria.get_left()[0] <= box.get_left()[0] or bacteria.get_right()[0] >= box.get_right()[0]:
                bacteria.velocity[0] = -bacteria.velocity[0]

            # Bounce off ground and roof
            if bacteria.get_bottom()[1] <= box.get_bottom()[1] or bacteria.get_top()[1] >= box.get_top()[1]:
                bacteria.velocity[1] = -bacteria.velocity[1]
        
        # Collision detection for the right box
        def update_fast_bacteria(bacteria, dt):
            bacteria.acceleration = 2 * np.random.random_sample(3) - 1 # [-1, 1] interval
            bacteria.velocity = bacteria.velocity + bacteria.acceleration * dt
            bacteria.shift(bacteria.velocity * dt)

            # Bounce off walls
            if bacteria.get_left()[0] <= box2.get_left()[0] +0.1 or bacteria.get_right()[0] >= box2.get_right()[0]-0.1:
                bacteria.velocity[0] = -bacteria.velocity[0]

            # Bounce off ground and roof
            if bacteria.get_bottom()[1] <= box2.get_bottom()[1]+0.1 or bacteria.get_top()[1] >= box2.get_top()[1]-0.1:
                bacteria.velocity[1] = -bacteria.velocity[1]

        # Collision detection for the big box
        def update_bigbox(bacteria, dt):
            bacteria.acceleration = 2 * np.random.random_sample(3) - 1 # [-1, 1] interval
            bacteria.velocity = bacteria.velocity + bacteria.acceleration * dt
            bacteria.shift(bacteria.velocity * dt)

            # Bounce off walls
            if bacteria.get_left()[0] <= big_box.get_left()[0]+0.1 or bacteria.get_right()[0] >= big_box.get_right()[0]-0.1:
                bacteria.velocity[0] = -bacteria.velocity[0]

            # Bounce off ground and roof
            if bacteria.get_bottom()[1] <= big_box.get_bottom()[1]+0.1 or bacteria.get_top()[1] >= big_box.get_top()[1]-0.1:
                bacteria.velocity[1] = -bacteria.velocity[1]

        # Attach collision detection to updater
        for bacteria in slow_bacteria_array:
            bacteria.add_updater(update_slow_bacteria)
        
        for bacteria in fast_bacteria_array:
            bacteria.add_updater(update_fast_bacteria)
        self.wait(10)

        #Have both of the boxes fade to purple to show temperature equality
        #Replace temp_comparison with temp_equality
        self.play(FadeOut(box, box2), FadeIn(big_box))
        for (slow, fast) in zip(slow_bacteria_array, fast_bacteria_array):
            slow.clear_updaters()
            slow.add_updater(update_bigbox)
            fast.clear_updaters()
            fast.add_updater(update_bigbox)

        self.wait(10)

        #It gets harder and harder to achieve a sense of order the more particles you jam into the box
        #Disorder among fast and slow particles is far more likely
        new_bacteria_array = []
        for i in range(0, 10):
            slow_bacteria_position = np.array([random.uniform(-4.5, 4.5), random.uniform(-2, 2), random.random()])
            fast_bacteria_position = np.array([random.uniform(-4.5, 4.5), random.uniform(-2, 2), random.random()])
            new_bacteria_array.append(SlowBacteria(slow_bacteria_position).add_updater(update_bigbox))
            new_bacteria_array.append(FastBacteria(fast_bacteria_position).add_updater(update_bigbox))
            new_list_bact = VGroup(*[new_bacteria_array[-1], new_bacteria_array[-2]])
            self.play(FadeIn(new_list_bact))
        #for bact in new_bacteria_array:
        #    bact.add_updater(update_bigbox)

        self.wait(15)


class DemonTransfer(Scene):
    def construct(self):

        #Constructing the two boxes
        box = Rectangle(width=5, height=5, fill_color=YELLOW_A, fill_opacity=0.14).shift(LEFT*2.5)
        box2 = Rectangle(width=5, height=5, fill_color=YELLOW_A, fill_opacity=0.14).shift(RIGHT*2.5)

        self.play(FadeIn(box, box2))

        left_slow = []
        left_fast = []
        right_slow = []
        right_fast = []

        #Creating the particles in the left box
        for i in range(0, 5):
            slow_bacteria_position = np.array([random.uniform(-4.5, -0.5), random.uniform(-2, 2), random.random()])
            fast_bacteria_position = np.array([random.uniform(-4.5, -0.5), random.uniform(-2, 2), random.random()])
            left_slow.append(SlowBacteria(slow_bacteria_position))
            left_fast.append(FastBacteria(fast_bacteria_position))
        list_bact_slow = VGroup(*[bact for bact in left_slow])
        list_bact_fast = VGroup(*[bact for bact in left_fast])
        self.play(FadeIn(list_bact_slow, list_bact_fast))

        #Creating the particles in the right box
        for i in range(0, 5):
            slow_bacteria_position = np.array([random.uniform(0.5, 4.5), random.uniform(-2, 2), random.random()])
            fast_bacteria_position = np.array([random.uniform(0.5, 4.5), random.uniform(-2, 2), random.random()])
            right_slow.append(SlowBacteria(slow_bacteria_position))
            right_fast.append(FastBacteria(fast_bacteria_position))
        list_bact_slow = VGroup(*[bact for bact in right_slow])
        list_bact_fast = VGroup(*[bact for bact in right_fast])
        self.play(FadeIn(list_bact_slow, list_bact_fast))

                # Collision detection for the left box
        def update_left_box(bacteria, dt):
            bacteria.acceleration = 2 * np.random.random_sample(3) - 1 # [-1, 1] interval
            bacteria.velocity = bacteria.velocity + bacteria.acceleration * dt
            bacteria.shift(bacteria.velocity * dt)

            # Bounce off walls
            if bacteria.get_left()[0] <= box.get_left()[0]+0.1 or bacteria.get_right()[0] >= box.get_right()[0]-0.1:
                bacteria.velocity[0] = -bacteria.velocity[0]

            # Bounce off ground and roof
            if bacteria.get_bottom()[1] <= box.get_bottom()[1]+0.1 or bacteria.get_top()[1] >= box.get_top()[1]-0.1:
                bacteria.velocity[1] = -bacteria.velocity[1]
        
        # Collision detection for the right box
        def update_right_box(bacteria, dt):
            bacteria.acceleration = 2 * np.random.random_sample(3) - 1 # [-1, 1] interval
            bacteria.velocity = bacteria.velocity + bacteria.acceleration * dt
            bacteria.shift(bacteria.velocity * dt)

            # Bounce off walls
            if bacteria.get_left()[0] <= box2.get_left()[0] +0.1 or bacteria.get_right()[0] >= box2.get_right()[0]-0.1:
                bacteria.velocity[0] = -bacteria.velocity[0]

            # Bounce off ground and roof
            if bacteria.get_bottom()[1] <= box2.get_bottom()[1]+0.1 or bacteria.get_top()[1] >= box2.get_top()[1]-0.1:
                bacteria.velocity[1] = -bacteria.velocity[1]

        for lf, ls, rf, rs in zip(left_fast, left_slow, right_fast, right_slow):
            lf.add_updater(update_left_box)
            ls.add_updater(update_left_box)
            rf.add_updater(update_right_box)
            rs.add_updater(update_right_box)

        self.wait(15)

        demon = Demon().move_to(UP*2.7)
        demon_text = Text("Maxwell's Demon", font_size=42).move_to(DOWN*3)
        self.play(FadeIn(demon), FadeIn(demon_text))

        #Moving the fast ones from left to right and the slow ones from right to left
        for i in range(0,5):
            fast = left_fast[i]
            slow = right_slow[i]
            right_fast.append(fast)
            left_slow.append(slow)
            fast.clear_updaters()
            slow.clear_updaters()
            demon.wave_arm(self)
            self.play(Swap(fast, slow), run_time=2)
            fast.add_updater(update_right_box)
            slow.add_updater(update_left_box)

        self.play(box.animate.set_color(BLUE))
        self.play(box2.animate.set_color(RED))
        self.wait(5)


class MultiplicityEx(MovingCameraScene):
    def construct(self):
        box = Rectangle(width=5, height=5, grid_xstep=5.0/14.0, grid_ystep=5.0/14.0, fill_color=RED, fill_opacity=0.25, color=BLACK).shift(LEFT*2.5)
        box2 = Rectangle(width=5, height=5, grid_xstep=5.0/14.0, grid_ystep=5.0/14.0, fill_color=BLUE, fill_opacity=0.25, color=BLACK).shift(RIGHT*2.5)
        #fade in the boxes
        self.play(FadeIn(box, box2))
        particles = MathTex(r"q=100").next_to(box.get_right(), UP*11)
        particles_A = MathTex(r"0\leq q_A\leq 100").next_to(box, DOWN)
        particles_B = MathTex(r"0\leq q_B\leq 100").next_to(box2, DOWN)
        A = Text("A").next_to(box, UP)
        B = Text("B").next_to(box2, UP)
        self.play(FadeIn(particles, particles_A, particles_B, A, B))

        # Creation of the bacteria, placing them randomly in the box
        bacteria_array = []
        for i in range(0, 100):
            bacteria_position = np.array([random.uniform(-4.7, 4.7), random.uniform(-2.3, 2.3), random.random()])
            bacteria_array.append(NormalBacteria(bacteria_position))
        list_bact = VGroup(*[bact for bact in bacteria_array])
        self.play(FadeIn(list_bact))
        #self.wait(2)

        # Collision detection for the big box
        def update_bigbox(bacteria, dt):
            bacteria.acceleration = 2 * np.random.random_sample(3) - 1 # [-1, 1] interval
            bacteria.velocity = bacteria.velocity + bacteria.acceleration * dt
            bacteria.shift(bacteria.velocity * dt)

            # Bounce off walls
            if bacteria.get_left()[0] <= box.get_left()[0]+0.1 or bacteria.get_right()[0] >= box2.get_right()[0]-0.1:
                bacteria.velocity[0] = -bacteria.velocity[0]

            # Bounce off ground and roof
            if bacteria.get_bottom()[1] <= box.get_bottom()[1]+0.1 or bacteria.get_top()[1] >= box.get_top()[1]-0.1:
                bacteria.velocity[1] = -bacteria.velocity[1]

        # Attach collision detection to updater
        for bacteria in bacteria_array:
            bacteria.add_updater(update_bigbox)
        self.wait(5)

        #Create the multiplicity formula and fade it in to the right of the simulation
        multiplicity_formula = MathTex(r"\Omega = \begin{pmatrix} q+N-1 \\ q \end{pmatrix}").next_to(box2.get_right(), RIGHT)
        self.play(FadeIn(multiplicity_formula))
        group = VGroup(box, box2, multiplicity_formula)
        self.play(self.camera.frame.animate.move_to(group.get_center()).scale(1.25))
        self.wait(8)

        #Move the multiplicity formula up and place the individual multiplicty formulas
        # below the general one
        self.play(multiplicity_formula.animate.shift(UP*1.8 + RIGHT*0.5))
        multiplicity_A = MathTex(r"\Omega_A = \begin{pmatrix} q_A+N_A-1 \\ q \end{pmatrix}").next_to(multiplicity_formula, DOWN)
        multiplicity_B = MathTex(r"\Omega_B = \begin{pmatrix} q_B+N_B-1 \\ q \end{pmatrix}").next_to(multiplicity_A, DOWN)
        self.play(FadeIn(multiplicity_A), FadeIn(multiplicity_B))
        self.wait(5)

        #Fade everything out or just make the table off screen somewhere and zoom in on it?
        #Hmm, decisions, decisions
        #I'll just put it offscreen somewhere
        table = MathTable(
            [[0, 1, 100, r"5.38\times 10^{80}", r"5.38\times 10^{80}"],
             [1, 196, 99, r"1.83\times 10^{80}", r"3.58\times 10^{82}"],
             [2, r"1.93\times 10^{4}", 98, r"6.15\times 10^{79}", r"1.19\times 10^{84}"],
             [r"\vdots",r"\vdots",r"\vdots",r"\vdots",r"\vdots"],
             [49, r"8.92\times 10^{51}", 51, r"2.11\times 10^{53}", r"1.88\times 10^{105}"],
             [50, r"4.37\times 10^{52}", 50, r"4.37\times 10^{52}", r"1.91\times 10^{105}"],
             [51, r"2.11\times 10^{53}", 51, r"8.92\times 10^{51}", r"1.88\times 10^{105}"],
             [r"\vdots",r"\vdots",r"\vdots",r"\vdots",r"\vdots"],
             [99, r"1.83\times 10^{80}", 1, 196, r"3.58\times 10^{82}"],
             [100, r"5.38\times 10^{80}", 0, 1, r"5.38\times 10^{80}"]],
            col_labels = [MathTex(r"q_A"), MathTex(r"\Omega_A"), MathTex(r"q_B"), MathTex(r"\Omega_B"), MathTex(r"\Omega_A \Omega_B")],
            include_outer_lines = TRUE
        ).move_to(UP*20, RIGHT*20)
        table.get_horizontal_lines().set_color(BLACK)
        table.get_vertical_lines().set_color(BLACK)

        table.add_highlighted_cell((1, 1), color=GREEN, fill_opacity=0.45)
        table.add_highlighted_cell((1, 2), color=BLUE, fill_opacity=0.45)
        table.add_highlighted_cell((1, 3), color=GREEN, fill_opacity=0.45)
        table.add_highlighted_cell((1, 4), color=BLUE, fill_opacity=0.45)
        table.add_highlighted_cell((1, 5), color=PURPLE, fill_opacity=0.45)

        for i in range(1, 11):
            table.add_highlighted_cell((i+1, 1), color=GREEN, fill_opacity=0.3)
            table.add_highlighted_cell((i+1, 2), color=BLUE, fill_opacity=0.3)
            table.add_highlighted_cell((i+1, 3), color=GREEN, fill_opacity=0.3)
            table.add_highlighted_cell((i+1, 4), color=BLUE, fill_opacity=0.3)
            table.add_highlighted_cell((i+1, 5), color=PURPLE, fill_opacity=0.3)

        self.play(FadeIn(table), self.camera.frame.animate.move_to(table.get_center()).scale(1.7))
        self.wait(3) #time (in seconds) the table remains on-screen alone


        #Displaying facts about most likely and least likely microstates
        total_micros = MathTex(r"\mathrm{Total: }2.69\times 10^{106}").next_to(table.get_columns()[-1], DOWN*2)
        #config.assets_dir = "C:/Users/cbarg/OneDrive/Desktop/Manim Testing/Maxwell/assets"
        graph = ImageMobject("C:/Users/cbarg/OneDrive/Desktop/Manim Testing/Maxwell/microstates.png").next_to(table.get_columns()[-1], RIGHT*80)
        graph.scale(10)
        self.play(FadeIn(total_micros))
        self.play(Indicate(total_micros))
        self.wait(5)

        self.play(FadeIn(graph), self.camera.frame.animate.move_to(graph.get_center()).scale(1.4))
        self.wait(10)

class Testing(Scene):
    def construct(self):
        config.assets_dir = "C:/Users/cbarg/OneDrive/Desktop/Manim Testing/Maxwell/assets"
        graph = ImageMobject("../assets/microstates.png")
        graph.scale(3)
        self.play(FadeIn(graph))
        self.wait(8)