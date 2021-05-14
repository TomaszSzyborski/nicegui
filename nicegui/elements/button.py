from typing import Callable
import justpy as jp
from .element import Element
from ..utils import handle_exceptions, provide_arguments

class Button(Element):

    def __init__(self,
                 text: str = '',
                 icon: str = None,
                 icon_right: str = None,
                 color: str = 'primary',
                 text_color: str = None,
                 design: str = '',
                 on_click: Callable = None):

        view = jp.QButton(
            label=text,
            icon=icon,
            icon_right=icon_right,
            color=color,
            text_color=text_color,
            **{key: True for key in design.split()}
        )

        if on_click is not None:
            view.on('click', handle_exceptions(provide_arguments(on_click)))

        super().__init__(view)