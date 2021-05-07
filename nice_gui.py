from inspect import trace
import traceback
from typing import final
import justpy as jp
from icecream import ic
from contextlib import contextmanager
import asyncio
import time


class Group():

    def label(self, text) -> jp.P:

        return jp.P(text=text, a=self.jp, classes='flex text-xl p-1 m-2')

    def button(self, text, on_click=None):

        def click(self, _):
            try:
                on_click(self)
            except:
                traceback.print_exc()

        d = jp.Div(text=text, a=self.jp, classes='w-48 text-xl m-2 p-1 bg-blue-700 text-white text-center')
        d.on('click', click)
        return d

    @contextmanager
    def column(self):
        yield Column(self.jp)

    def timer(self, invervall, callback):

        async def loop():

            while True:
                start = time.time()
                try:
                    callback()
                    jp.run_task(self.jp.update())
                except:
                    traceback.print_exc()
                finally:
                    dt = time.time() - start
                    await asyncio.sleep(invervall - dt)

        ic()
        jp.run_task(loop())


class Page(Group):

    def __init__(self):

        self.jp = jp.WebPage(delete_flag=False)

        def build():
            return self.jp

        jp.justpy(build, start_server=False)


class Column(Group):

    def __init__(self, parent_jp) -> None:

        self.jp = jp.Div(a=parent_jp, classes='flex flex-wrap')


main = Page()
ui = jp.app

# bind methods to simplify API -- justpy creates an app which must be found by uvicorn via string "module:attribute"
ui.label = main.label
ui.button = main.button
ui.column = main.column
ui.timer = main.timer