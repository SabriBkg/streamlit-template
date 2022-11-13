from .home import home
from .mapping_demo import mapping_demo
from .plotting_demo import plotting_demo
from ..utils import Page

from typing import Dict, Type


PAGE_MAP: Dict[str, Type[Page]] = {
    "Home": home,
    "Mapping Demo": mapping_demo,
    "Plotting Demo": plotting_demo,
}

__all__ = ["PAGE_MAP"]