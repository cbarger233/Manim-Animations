from tkinter import BOTTOM
from manim import *


class Oct18d22y(Scene):
    def construct(self):
        #Write out the problem and the pythagorean identity used to simplify it
        problem = MathTex(r'\int x {{\tan^2(x)}}dx').scale(2)
        pyth_identity = MathTex(r'\tan^2(x) = \sec^2(x)-1', color=GREEN_D).next_to(problem, DOWN).scale(1.5)
        self.play(Write(problem), run_time=2)
        self.wait()
        self.play(Write(pyth_identity),
                problem.animate.shift(UP*0.5),
                problem.animate.set_color_by_tex(r'\tan^2(x)', GREEN_D),
                run_time=1.3)
        self.wait()

        #Write the next step to solving the problem and move it underneath the posed problem
        second_step = MathTex(r'=\int x {{\left(\sec^2(x)-1 \right)}}dx').scale(1.5)
        second_step.set_color_by_tex(r'\left(\sec^2(x)-1 \right)', GREEN_D)
        self.play(Write(second_step),
                problem.animate.to_edge(UP).scale(0.75),
                pyth_identity.animate.to_corner(DOWN + LEFT).scale(0.5),
                run_time=2)
        self.wait()

        third_step = MathTex(r'={{\int x\sec^2(x)dx}} - {{\int xdx}}').scale(1.5)
        #Move the original equation to the left wall and
        #put the next step of the equation netx to it
        self.play(
            problem.animate.to_edge(LEFT)
        )
        self.play(
            second_step.animate.next_to(problem, RIGHT)
        )
        #group together the second and third equation to more easily align them
        two_and_three = VGroup(second_step, third_step)
        two_and_three.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(
            #align VGroup to upper right corner of original problem
            Write(third_step),
            run_time=1.3
        )
        self.wait()
        self.play(
            #Indicate the easy second integral
            Indicate(third_step[3], scale_factor=1.3),
        )
        self.play(third_step.animate.set_color_by_tex(r'\int xdx', YELLOW), run_time=0.1)
        self.play(third_step.animate.set_color_by_tex(r'-', YELLOW), run_time=0.1)
        self.wait()

        #G  ive soolution to easy sub-integral
        easy_integral = MathTex(r'=-\frac{1}{2}x^2', color=YELLOW).scale(1.5).next_to(third_step[3], DOWN)
        self.play(Write(easy_integral))
        self.wait()

        remaining_integral = MathTex(r'\int {{x}} \cdot {{\sec^2(x)dx}}').scale(1.3)
        target = VGroup(easy_integral, problem, second_step, third_step, pyth_identity)
        self.play(FadeOut(target))
        self.play(Write(remaining_integral))
        self.wait()

        parts = MathTex(r'=uv-\int vdu').scale(1.5)
        u = MathTex(r'u=x', color=BLUE).shift(LEFT*1.5)
        du = MathTex(r'du=dx', color=BLUE).next_to(u, DOWN)

        dv = MathTex(r'dv=\sec^2(x)dx', color=YELLOW).next_to(u, RIGHT*1.5)
        v = MathTex(r'v=\tan(x)', color=YELLOW).next_to(du, RIGHT)

        self.play(remaining_integral.animate.to_corner(UP+LEFT))
        self.play(Write(parts))
        self.play(parts.animate.next_to(remaining_integral, RIGHT))
        self.wait()

        self.play(
            remaining_integral[1].animate.set_color(BLUE),
            Write(u)
        )
        self.wait()
        self.play(
            remaining_integral.animate.set_color_by_tex(r'\sec^2(x)dx', YELLOW),
            Write(dv)
        )
        self.wait()
        self.play(
            Write(du),
            Write(v)
        )
        self.wait()

        to_the_corner = VGroup(u, du, dv, v)
        self.play(to_the_corner.animate.to_corner(LEFT + DOWN))

        second_part = MathTex(r'={{x \tan(x)}} - \int {{\tan(x)}}dx').scale(1.3)
        second_and_parts = VGroup(parts, second_part)
        second_and_parts.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(
            Write(second_part),
            run_time=1.3
        )
        self.wait()

        tan_identity = MathTex(r'\tan(x) = \frac{\sin(x)}{\cos(x)}', color=GREEN).to_corner(RIGHT + DOWN)
        self.play(
            Write(tan_identity),
            second_part[3].animate.set_color(GREEN),
            run_time=1.2
        )
        self.wait()
        parts_result = MathTex(r'={{x\tan(x)}} - \int {{\frac{\sin(x)}{\cos(x)}}}dx').scale(1.3)
        parts_result[3].set_color(GREEN)
        second_and_parts.add(parts_result)
        second_and_parts.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(parts_result), run_time=1.3)
        self.wait()






