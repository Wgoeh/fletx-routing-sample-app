"""
Page1 Controller.

This Page class is generated from a template.
"""

from flet import * 
from fletx.core import FletXPage 
from fletx.navigation import navigate, go_back
from fletx.utils import get_page 

# Import your modules here...


class Page1Page(FletXPage):
    """Page1 Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Colors.ORANGE,
        )

        # ...

    def on_init(self):
        """Hook called when Page1Page in initialized"""

        print("Page1Page is initialized")

    def on_destroy(self):
        """Hook called when Page1Page will be unmounted."""

        print("Page1Page is destroyed")

    def build(self)-> Control:
        """Method that build Page1Page content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Container(
                    expand = True,
                    content = Text("Page1Page works!", size=24),
                ),
                Container(
                    expand = True,
                    content = ElevatedButton(
                        "Go back",
                        on_click=lambda e: go_back()  # Auto UI update
                    )
                ),
                Container(
                    expand = True,
                    content = ElevatedButton(
                        "See page 3",
                        on_click=lambda e: navigate('/page3')  # Auto UI update
                    )
                ),
            ]
        )