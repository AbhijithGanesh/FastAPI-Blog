__all__ = ("get_posts", "template_router")

from .templates import templates_view as template_router
from .posts import posts_fetcher as get_posts
