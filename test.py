from turtle import fillcolor
from manim import *

class MovingFrame(Scene):
    def construct(self):
        self.camera.background_color = '#ece6e2'
        logo_green = '#87c2a5'
        logo_blue = '#525893'
        logo_red = '#e07a5f'
        logo_black = '#343434'

        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)

        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)

        logo = VGroup(triangle, square, circle, ds_m)
        logo.move_to(ORIGIN)
        self.add(logo)

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)

class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -2, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        
        b1 = Brace(line)
        b1text = b1.get_text('Horizontal Distance')

        b2 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector())
        b2text = b2.get_tex('x-x_1')

        self.add(line, dot, dot2, b1, b2, b1text, b2text)

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP*3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT*3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT*5 + UP*2.5))
        intersection_text = Text("Intersection", font_size=23).move_to(i, UP*4)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN*1.5, buff=union_text.height*3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN*1.5, buff=exclusion_text.height*3))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        self.wait()

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT*2)
        self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=10, rate_func=exponential_decay)
        self.play(Rotating(dot, about_point=[4, 0, 0]), run_time=2)
        self.wait()

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center(), dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()