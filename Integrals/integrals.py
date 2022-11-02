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
        self.play(third_step.animate.set_color_by_tex(r'\int xdx', YELLOW), run_time=0.05)
        self.play(third_step.animate.set_color_by_tex(r'-', YELLOW), run_time=0.05)
        self.play(
            #Indicate the easy second integral
            Indicate(third_step[3], scale_factor=1.3),
        )
        #self.play(third_step.animate.set_color_by_tex(r'\int xdx', YELLOW), run_time=0.1)
        #self.play(third_step.animate.set_color_by_tex(r'-', YELLOW), run_time=0.1)
        self.wait()

        #G  ive soolution to easy sub-integral
        easy_integral = MathTex(r'=-\frac{1}{2}x^2 + c_1', color=YELLOW).next_to(third_step[3], DOWN)
        self.play(Write(easy_integral))
        self.wait()

        simplified_problem = MathTex(r'\int {{x}} \cdot {{\tan^2(x)dx}} = {{\int x\cdot \sec^2(x)dx}} - \frac{1}{2}x^2+c_1').scale(1.3)
        remaining_integral = MathTex(r'\int {{x}} \cdot {{\sec^2(x)dx}}').scale(1.3)
        target = VGroup(easy_integral, problem, second_step, third_step, pyth_identity)
        self.play(FadeOut(target))
        self.play(Write(simplified_problem))
        self.wait(2)
        self.play(Wiggle(simplified_problem[5]))
        self.play(FadeOut(simplified_problem), Write(remaining_integral))
        self.wait()

        parts = MathTex(r'=uv-\int vdu').scale(1.5)
        u = MathTex(r'u=x', color=BLUE).shift(LEFT*1.5)
        du = MathTex(r'du=dx').next_to(u, DOWN)

        dv = MathTex(r'dv=\sec^2(x)dx', color=YELLOW).next_to(u, RIGHT*1.5)
        v = MathTex(r'v=\tan(x)').next_to(du, RIGHT)

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


        get_rid = VGroup(remaining_integral, u, du, v, dv, parts_result, second_part, tan_identity, parts)
        sin_cos = MathTex(r'-\int \frac{\sin(x)}{\cos(x)}dx').scale(1.3).to_corner(LEFT + UP)
        self.play(Transform(get_rid, sin_cos))
        u = MathTex(r'u=\cos(x)')
        du = MathTex(r'du=-\sin(x)dx')
        u_sub = VGroup(u, du).arrange(DOWN, center=False, aligned_edge=LEFT)
        second_step = MathTex(r'=\int \frac{du}{u}').scale(1.3).next_to(sin_cos, RIGHT)
        third_step = MathTex(r'=\ln (u) + c_2').scale(1.3)
        fourth_step = MathTex(r'=\ln(\cos(x)) + c_2').scale(1.3)
        group = VGroup(second_step, third_step, fourth_step).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.2)
        
        self.wait(4)
        self.play(Write(u_sub))
        self.wait()
        self.play(u_sub.animate.to_corner(DOWN + LEFT))
        self.play(
            Write(second_step),
            run_time=1.3
        )
        self.play(
            Write(third_step),
            run_time=1.3
        )
        self.play(
            Write(fourth_step),
            run_time=1.3
        )
        self.wait()


        self.clear()
        prob = MathTex("\\int x", "\\tan^2(x)", "dx")
        prob[1].set_color(GREEN)
        second = MathTex("=", "\\int x", "{\\left(", "\\sec^2(x)-1", "\\right)}dx").scale(0.9)
        second[3].set_color(GREEN)
        pyth = Text("Pythagorean Identity").set_color(GREEN)
        third_step = MathTex("=","\\int x \\sec^2(x)dx","-\\int xdx").scale(0.9)
        third_step[1].set_color(YELLOW)
        third_step[2].set_color(RED)
        fourth_step = MathTex("=", "x\\tan (x)", "-\\int \\frac{\\sin (x)}{\\cos (x)}dx", "-\\frac{1}{2}x^2+c_1").scale(0.9)
        fourth_step[1].set_color(YELLOW)
        fourth_step[2].set_color(YELLOW)
        fourth_step[3].set_color(RED)
        to_square_step_4 = VGroup(fourth_step[2])
        fourth_step_exp = Text("Parts ").set_color(YELLOW)
        fourth_step_exp1 = Text("Power Rule").set_color(RED)
        fifth_step = MathTex("=x\\tan (x)", "+\\ln (\\cos(x))", "+", "c_2", "-\\frac{1}{2}x^2 +c_1").scale(0.9)
        to_square_step_5 = VGroup(fifth_step[1], fifth_step[2], fifth_step[3])
        fifth_step_exp = Text("u-sub")
        sixth_step = MathTex("=x\\tan (x)", "+\\ln (\\cos(x))", "+", "-\\frac{1}{2}x^2 +", "c").scale(0.9)

        self.play(Write(prob))
        self.wait()
        self.play(prob.animate.to_corner(UP + LEFT))
        self.wait()

        grouped = VGroup(prob, second, third_step, fourth_step, fifth_step, sixth_step)
        grouped.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.2)
        pyth.next_to(second, RIGHT).scale(0.8)
        fourth_step_exp.next_to(fourth_step, RIGHT).scale(0.8)
        fourth_step_exp1.next_to(fourth_step_exp, RIGHT).scale(0.8)
        four_rect = SurroundingRectangle(to_square_step_4).set_color(BLUE)
        fifth_step_exp.next_to(fifth_step, RIGHT).scale(0.8)
        five_rect = SurroundingRectangle(to_square_step_5).set_color(BLUE)
        five_rect_text = SurroundingRectangle(fifth_step_exp).set_color(BLUE)
        self.play(Write(second), Write(pyth))
        self.wait()
        self.play(Write(third_step))
        self.wait()
        self.play(Write(fourth_step), Write(fourth_step_exp), Write(fourth_step_exp1))
        self.wait()
        self.play(Write(fifth_step), Write(fifth_step_exp))
        self.play(Write(four_rect), Write(five_rect), Write(five_rect_text))
        self.wait()
        self.play(Write(sixth_step))
        self.wait(5)


class Test(Scene):
    def construct(self):
        prob = MathTex("\\int x", "\\tan^2(x)", "dx")
        prob[1].set_color(GREEN)
        second = MathTex("=", "\\int x", "{\\left(", "\\sec^2(x)-1", "\\right)}dx").scale(0.9)
        second[3].set_color(GREEN)
        pyth = Text("Pythagorean Identity").set_color(GREEN)
        third_step = MathTex("=","\\int x \\sec^2(x)dx","-\\int xdx").scale(0.9)
        third_step[1].set_color(YELLOW)
        third_step[2].set_color(RED)
        fourth_step = MathTex("=", "x\\tan (x)", "-\\int \\frac{\\sin (x)}{\\cos (x)}dx", "-\\frac{1}{2}x^2+c_1").scale(0.9)
        fourth_step[1].set_color(YELLOW)
        fourth_step[2].set_color(YELLOW)
        fourth_step[3].set_color(RED)
        to_square_step_4 = VGroup(fourth_step[2])
        fourth_step_exp = Text("Parts ").set_color(YELLOW)
        fourth_step_exp1 = Text("Power Rule").set_color(RED)
        fifth_step = MathTex("=x\\tan (x)", "+\\ln (\\cos(x))", "+", "c_2", "-\\frac{1}{2}x^2 +c_1").scale(0.9)
        to_square_step_5 = VGroup(fifth_step[1], fifth_step[2], fifth_step[3])
        fifth_step_exp = Text("u-sub")
        sixth_step = MathTex("=x\\tan (x)", "+\\ln (\\cos(x))", "+", "-\\frac{1}{2}x^2 +", "c").scale(0.9)

        self.play(Write(prob))
        self.wait()
        self.play(prob.animate.to_corner(UP + LEFT))
        self.wait()

        grouped = VGroup(prob, second, third_step, fourth_step, fifth_step, sixth_step)
        grouped.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.2)
        pyth.next_to(second, RIGHT).scale(0.8)
        fourth_step_exp.next_to(fourth_step, RIGHT).scale(0.8)
        fourth_step_exp1.next_to(fourth_step_exp, RIGHT).scale(0.8)
        four_rect = SurroundingRectangle(to_square_step_4).set_color(BLUE)
        fifth_step_exp.next_to(fifth_step, RIGHT).scale(0.8)
        five_rect = SurroundingRectangle(to_square_step_5).set_color(BLUE)
        five_rect_text = SurroundingRectangle(fifth_step_exp).set_color(BLUE)
        self.play(Write(second), Write(pyth))
        self.wait()
        self.play(Write(third_step))
        self.wait()
        self.play(Write(fourth_step), Write(fourth_step_exp), Write(fourth_step_exp1))
        self.wait()
        self.play(Write(fifth_step), Write(fifth_step_exp))
        self.play(Write(four_rect), Write(five_rect), Write(five_rect_text))
        self.wait()
        self.play(Write(sixth_step))
        self.wait(5)




class FormulaColor3Fixed2(Scene): 
    def construct(self): 
        text = MathTex("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(3)




