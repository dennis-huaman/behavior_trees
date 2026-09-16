#!/usr/bin/env python3


import argparse
import time
import typing
import py_trees
import py_trees.console as console

import os

os.system("clear")


class Counter(py_trees.behaviour.Behaviour):
    def __init__(self, name: str = "Counter"):
        """Configure the name of the behaviour."""
        super(Counter, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        """No delayed initialisation required for this example."""
        self.logger.debug(f"{self.__class__.__name__}.setup()")

    def initialise(self) -> None:
        """Reset a counter variable."""
        self.logger.debug(f"{self.__class__.__name__}.initialise()")
        self.counter = 0

    def update(self) -> py_trees.common.Status:
        self.counter += 1

        if self.counter == 3:
            new_status = py_trees.common.Status.SUCCESS
            self.feedback_message = f"counting...{self.counter} - enough for today"
        else:
            self.feedback_message = "still counting"
            new_status = py_trees.common.Status.RUNNING

        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status}->{new_status}][{self.feedback_message}]"
        )

        return new_status


def main() -> None:

    py_trees.logging.level = py_trees.logging.Level.DEBUG
    counter = Counter()
    counter.setup()

    for _unused_i in range(0, 7):
        counter.tick_once()
        time.sleep(0.5)
    print("\n")


if __name__ == "__main__":
    main()
