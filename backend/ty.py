# from manim import *

# class NewtonsLaws(Scene):
#     def construct(self):
#         # INTRO
#         intro_text = Text("Newton's Laws of Motion", font_size=48, color=BLUE)
#         self.play(FadeIn(intro_text))
#         self.wait(1)
#         self.play(FadeOut(intro_text))

#         # LAW 1: Inertia
#         ball = Circle(radius=0.3, color=YELLOW).shift(LEFT*2)
#         hand = Square(side_length=0.5, color=RED).shift(LEFT*4)
#         label1 = Text("Inertia = Resistance to Motion").next_to(ball, DOWN)
#         self.play(FadeIn(ball), FadeIn(hand))
#         self.play(ApplyMethod(ball.shift, RIGHT*4))
#         self.play(FadeIn(label1))
#         self.wait(1)
#         self.play(FadeOut(ball), FadeOut(hand), FadeOut(label1))

#         # LAW 2: F = ma
#         small_ball = Circle(radius=0.2, color=GREEN).shift(LEFT*2)
#         big_ball = Circle(radius=0.5, color=ORANGE).shift(LEFT*2 + UP*2)
#         label2 = Text("F = ma", font_size=36).to_edge(UP)
#         self.play(FadeIn(small_ball), FadeIn(big_ball), FadeIn(label2))
#         self.play(small_ball.animate.shift(RIGHT*4), big_ball.animate.shift(RIGHT*2))
#         self.wait(1)
#         self.play(FadeOut(small_ball), FadeOut(big_ball), FadeOut(label2))

#         # LAW 3: Action-Reaction
#         rocket = Triangle().scale(0.5).set_color(RED).shift(DOWN*2)
#         flame = Polygon([-0.2,0,0],[0.2,0,0],[0,-0.5,0], color=ORANGE).shift(DOWN*2)
#         label3 = Text("Action = Opposite Reaction").to_edge(DOWN)
#         self.play(FadeIn(rocket), FadeIn(flame), FadeIn(label3))
#         self.play(rocket.animate.shift(UP*3), flame.animate.shift(DOWN*1))
#         self.wait(1)
#         self.play(FadeOut(rocket), FadeOut(flame), FadeOut(label3))

#         # EXAMPLE: Soccer Kick
#         ball2 = Circle(radius=0.3, color=YELLOW).shift(LEFT*3)
#         player_foot = Rectangle(width=0.5, height=0.2, color=BLUE).next_to(ball2, LEFT)
#         self.play(FadeIn(ball2), FadeIn(player_foot))
#         self.play(ball2.animate.shift(RIGHT*4))
#         self.wait(1)
#         self.play(FadeOut(ball2), FadeOut(player_foot))

#         # CONCLUSION
#         summary = Text("1. Inertia  2. F=ma  3. Action-Reaction", font_size=36, color=BLUE)
#         self.play(FadeIn(summary))
#         self.wait(2)
#         self.play(FadeOut(summary))
