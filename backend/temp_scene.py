from manim import*

class GenScene(Scene):
    def construct(self):
        # Title
        title = Text("Friction Between Two Surfaces", font_size=36)
        title.to_edge(UP)
        self.play(FadeIn(title))
        self.wait(0.5)

        # Ground
        ground = Line(LEFT * 6, RIGHT * 6, color=GRAY).shift(DOWN * 2)
        self.play(Create(ground))

        # Block
        block = Square(side_length=1, fill_color=BLUE, fill_opacity=0.8, stroke_color=WHITE)
        block.move_to(LEFT * 4 + UP * 0.5)  # start left of center, sitting on ground        self.play(FadeIn(block))

        # Normal force arrow (upwards from block)
        normal_arrow = Arrow(
            start=block.get_bottom(),
            end=block.get_bottom() + UP * 0.8,
            buff=0,
            color=YELLOW,
            max_tip_length_to_length_ratio=0.2,
        )
        normal_label = Text("N", font_size=24).next_to(normal_arrow, LEFT)
        self.play(GrowArrow(normal_arrow), FadeIn(normal_label))
        self.wait(0.5)

        # Applied force arrow (to the right)
        applied_arrow = Arrow(
            start=block.get_left(),
            end=block.get_left() + RIGHT * 1.5,
            buff=0,
            color=RED,
            max_tip_length_to_length_ratio=0.2,
        )
        applied_label = Text("F_app", font_size=24).next_to(applied_arrow, UP)
        self.play(GrowArrow(applied_arrow), FadeIn(applied_label))
        self.wait(0.5)

        # Friction force arrow (to the left)
        friction_arrow = Arrow(
            start=block.get_right(),
            end=block.get_right() + LEFT * 1.0,
            buff=0,
            color=GREEN,
            max_tip_length_to_length_ratio=0.2,
        )
        friction_label = Text("f", font_size=24).next_to(friction_arrow, DOWN)
        self.play(GrowArrow(friction_arrow), FadeIn(friction_label))
        self.wait(0.5)

        # Show net force and resulting acceleration (optional)
        net_force = applied_arrow.get_end()[0] - friction_arrow.get_end()[0]  # simplified magnitude
        net_text = Text(f"Net Force ≈ {net_force:.1f} N →", font_size=24).next_to(block, DOWN)
        self.play(FadeIn(net_text))
        self.wait(1)

        # Animate block moving right with decreasing speed