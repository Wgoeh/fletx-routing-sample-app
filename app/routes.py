"""
routing_app Application routing module.
Version: 0.1.0
"""


# Import your pages here
from fletx.navigation import ( # type: ignore
    ModuleRouter, TransitionType, RouteTransition
)
from fletx.decorators import register_router # type: ignore

from .pages import CounterPage, Page1Page, Page2Page, Page3Page, Page4Page
from .middlewares import MetricsMiddleware
from.guards import ConfirmNavigationGuard

# Define RoutingApp routes here
routes = [
    {
        'path': '/',
        'component': CounterPage,
    },
    {
        'path': '/page1',
        'component': Page1Page,
        'meta':{
            'transition': RouteTransition(
                transition_type = TransitionType.SLIDE_LEFT,
                duration = 350
            )
        }
    },
    {
        'path': '/page2/:id',
        'component': Page2Page,
        'meta':{
            'transition': RouteTransition(
                transition_type = TransitionType.ROTATE,
                duration = 350
            )
        }
    },
    {
        'path': '/page3',
        'component': Page3Page,
        'middleware': [
            MetricsMiddleware()
        ],
        'meta':{
            'transition': RouteTransition(
                transition_type = TransitionType.ZOOM_IN,
                duration = 350
            )
        }
    },
    {
        'path': '/page4',
        'component': Page4Page,
        'guards':[
            # ConfirmNavigationGuard()
        ],
        'meta':{
            'transition': RouteTransition(
                transition_type = TransitionType.FADE,
                duration = 350
            )
        }
    },
]

@register_router
class RoutingAppRouter(ModuleRouter):
    """routing_app Routing Module."""

    name = 'routing_app'
    base_path = '/'
    is_root = True
    routes = routes
    sub_routers = []