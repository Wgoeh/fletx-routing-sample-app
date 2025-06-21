import asyncio
import flet as ft # type: ignore
from fletx.navigation import RouteGuard, RouteInfo # type: ignore
from fletx.utils import get_logger, get_page, get_event_loop # type: ignore
from typing import Callable, Optional

class ConfirmNavigationGuard(RouteGuard):
    """Guard that requires user confirmation before leaving a route."""
    
    def __init__(self):
        self._confirmation_event = asyncio.Event()
        self._confirmation_result = False
        self._logger = get_logger('FletX.ConfirmNavigationGuard')
    
    async def can_activate(self, route_info: RouteInfo) -> bool:
        """Confirmation required"""

        # if not self._confirmation_result:
        #     return self._confirmation_result
        
        return await self.show_dialog()
    
    async def can_deactivate(self, current_route: RouteInfo) -> bool:
        """Require confirmation to leave."""
        return True
    
    async def redirect_to(self, route_info: RouteInfo) -> Optional[str]:
        return None
    
    async def show_dialog(self) -> bool:
        """Show a confirmation dialog and wait for user input."""

        page = get_page()
        self._confirmation_event.clear()
        self._confirmation_result = False

        def handle_action_click(e):
            self._confirmation_result = e.control.text == "Yes"
            page.close(dialog)
            # self._confirmation_event.set()

        dialog = ft.AlertDialog(
            modal = True,
            title = ft.Text("Confirm Navigation Guard"),
            content = ft.Text("Do you really want to leave this page?"),
            actions = [
                ft.TextButton(text="Yes", on_click=handle_action_click),
                ft.TextButton(text="No", on_click=handle_action_click),
            ],
            on_dismiss = lambda _: print()
        )

        # dialog.open = True
        page.open(dialog)
        # await self._confirmation_event.wait()
        await asyncio.sleep(.2)
        print(f'\n\n\n {self._confirmation_result} \n\n\n')

        # # Wait for user to click a button
        # await self._confirmation_event.wait()
        return self._confirmation_result
