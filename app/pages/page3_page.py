"""
Page3 Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage
from fletx.navigation import navigate, go_back
from fletx.utils import get_page

# Import your modules here...


class Page3Page(FletXPage):
    """Page3 Page"""

    def __init__(self):
        super().__init__(
            padding = 10,
            bgcolor = Colors.TEAL,
        )

        # ...

    def on_init(self):
        """Hook called when Page3Page in initialized"""

        print("Page3Page initialized")

    def on_destroy(self):
        """Hook called when Page3Page will be unmounted."""

        print("Page3Page is destroyed")

    def build(self)-> Control:
        """Method that build Page3Page content"""

        return Column(
            expand = True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Container(
                    expand = True,
                    content = Text(f"Page3Page works!", size=24),
                ),
                Container(
                    expand = True,
                    content = ElevatedButton(
                        "Go back",
                        on_click=lambda e: navigate('/page1')  # Auto UI update
                    )
                ),
                Container(
                    expand = True,
                    content = ElevatedButton(
                        "See page 2",
                        on_click=lambda e: navigate('/page2/23')  # Auto UI update
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