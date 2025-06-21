from typing import Optional
import time

from fletx.navigation import RouteMiddleware, RouteInfo, NavigationIntent # type: ignore
from fletx.utils import get_logger # type: ignore


class MetricsMiddleware(RouteMiddleware):
    """Middleware for collecting performance metrics."""
    
    def __init__(self):
        self._navigation_metrics = {}
        self._logger = get_logger('FletX.MetricsMiddleware')
    
    async def before_navigation(
        self, 
        from_route: RouteInfo, 
        to_route: RouteInfo
    ) -> Optional[NavigationIntent]:
        """Start measuring navigation performance."""

        navigation_id = f"{from_route.path}->{to_route.path}"
        self._navigation_metrics[navigation_id] = {
            'start_time': time.time(),
            'from_route': from_route.path,
            'to_route': to_route.path
        }
        print('\n\n\n\n before navigation metrics: ', self._navigation_metrics[navigation_id], '\n\n\n\n')
        return None
    
    async def after_navigation(self, route_info: RouteInfo) -> None:
        """Record navigation performance metrics."""

        # Find the matching navigation in progress
        for nav_id, metrics in self._navigation_metrics.items():
            if metrics['to_route'] == route_info.path:
                metrics['duration'] = time.time() - metrics['start_time']
                
                print('\n\n\n\n after navigation metrics: ', metrics, '\n\n\n\n')
                
                # Clean up
                del self._navigation_metrics[nav_id]
                break