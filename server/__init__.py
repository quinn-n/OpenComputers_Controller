from typing import Union

import click
import pyglet
import uvicorn
from fastapi import FastAPI, Request

_INPUTS = (
    # analog inputs
    "leftx",
    "lefty",
    "rightx",
    "righty",
    "lefttrigger",
    "righttrigger",
    # digital inputs
    "a",
    "b",
    "x",
    "y",
    "leftshoulder",
    "rightshoulder",
    "start",
    "back",
    "guide",
    "leftstick",
    "rightstick",
    "dpleft",
    "dpright",
    "dpup",
    "dpdown",
)

_INPUT_DICT_T = dict[str, bool | float]

app = FastAPI()


@app.get("/controller_inputs")
def get_controller_inputs(request: Request) -> _INPUT_DICT_T:
    """Endpoint that serves controller inputs"""
    process_events()
    inputs: _INPUT_DICT_T = {}
    for input_key in _INPUTS:
        inputs[input_key] = getattr(controller, input_key)
    return inputs


@click.command()
def run_app() -> None:
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        log_level="debug",
    )


def process_events() -> None:
    """Steps through all of the events queued by pyglet to update the controller inputs."""
    while pyglet.app.platform_event_loop.step(timeout=0):
        pass


controllers = pyglet.input.get_controllers()
if not controllers:
    click.echo("No controllers connected!", err=True)
    exit(1)

controller = controllers[0]
controller.open()

click.echo(f"Connected to {controller.name}")
