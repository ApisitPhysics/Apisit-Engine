R"""
    This library is a further development from original ManimCe.
    See ManimnCe: https://www.manim.community
    Also see Manim by Grant Sanderson: https://github.com/3b1b/manim,
    and his animation created by his own Manim: https://www.3blue1brown.com/
"""

R"""
    This is very simple to use this module.
    just input Text or Tex or MathTex to the parameter and tell the direction

    Example:

    ```
    class ExMultiText(Scene):
        def construct(self):
            multi_text = MultiText(
                Text("Hello"),
                Text("World!),
                direction=DOWN
            )
            self.play(Write(multi_text))
    ```

    result

    ***
        rendered:
            Hello
            World!
    ***
"""

from manim.constants import *
from manim.mobject.text.tex_mobject import MathTex, Tex
from manim.mobject.text.text_mobject import Text
from manim.mobject.types.vectorized_mobject import VGroup
from manim.typing import Vector3D

class MultiText(VGroup):
    def __init__(
        self,
        *strings_class: MathTex | Tex | Text,
        direction: Vector3D | None = RIGHT
    ):
        before_text = None
        elements = VGroup()
        for string in strings_class:
            if before_text:
                string.next_to(before_text, direction)
            elements.add(string)
            before_text = string
        elements.move_to(ORIGIN)

        super().__init__(elements)
