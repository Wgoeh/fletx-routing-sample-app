"""
Page4 Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage
from fletx.navigation import navigate, go_back

# Import your modules here...


class Page4Page(FletXPage):
    """Page4 Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Colors.PINK
        )

        # ...

    def on_init(self):
        """Hook called when Page4Page in initialized"""

        print("Page4Page is initialized")

    def on_destroy(self):
        """Hook called when Page4Page will be unmounted."""

        print("Page4Page is destroyed")

    def build(self)-> Control:
        """Method that build Page4Page content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Container(
                    expand = True,
                    content = Text(f"Page4Page works!", size=24),
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
                        "Return home",
                        on_click=lambda e: navigate('/')  # Auto UI update
                    )
                ),
            ]
        )