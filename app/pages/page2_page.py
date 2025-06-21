"""
Page2 Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage
from fletx.navigation import navigate, go_back
from fletx.utils import get_page

# Import your modules here...


class Page2Page(FletXPage):
    """Page2 Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Colors.BLUE,
        )

        # ...

    def on_init(self):
        """Hook called when Page2Page in initialized"""

        print("Page2Page initialized")

    def on_destroy(self):
        """Hook called when Page2Page will be unmounted."""

        print("Page2Page is destroyed")

    def build(self)-> Control:
        """Method that build Page2Page content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Container(
                    expand = True,
                    content = Text(f"Page2Page works with param {self.route_info.params}!", size=24),
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
                        "See page 4",
                        on_click=lambda e: navigate('/page4')  # Auto UI update
                    )
                ),
            ]
        )