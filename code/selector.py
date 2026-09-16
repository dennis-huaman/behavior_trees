import time
from traceback import print_tb
import py_trees
import random

import os

os.system("clear")


class BTAction1(py_trees.behaviour.Behaviour):
    def __init__(self, name: str = "BTAction1"):
        super(BTAction1, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.commos.Status:

        random_integer = random.randrange(1, 10)
        if random_integer < 3:
            self.feedback_message = f"Number {random_integer} is less than 3: Success"
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = (
                f"Number {random_integer} is greater than 3: Success"
            )
            new_status = py_trees.common.Status.FAILURE

        return new_status


class BTAction2(py_trees.behaviour.Behaviour):
    def __init__(self, name: str = "BTAction2"):
        super(BTAction2, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.commos.Status:

        random_integer = random.randrange(1, 10)
        if random_integer < 5:
            self.feedback_message = f"Number {random_integer} is less than 5: Success"
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = (
                f"Number {random_integer} is greater than 5: Success"
            )
            new_status = py_trees.common.Status.FAILURE

        return new_status


class BTAction3(py_trees.behaviour.Behaviour):
    def __init__(self, name: str = "BTAction3"):
        super(BTAction3, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.commos.Status:

        random_integer = random.randrange(1, 10)
        if random_integer < 8:
            self.feedback_message = f"Number {random_integer} is less than 8: Success"
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = (
                f"Number {random_integer} is greater than 8: Success"
            )
            new_status = py_trees.common.Status.FAILURE

        return new_status


def create_root() -> py_trees.behaviour.Behaviour:
    root = py_trees.composites.Selector(name="Selector", memory=True)
    node1 = BTAction1(name="Action1")
    root.add_child(node1)

    node2 = BTAction2(name="Action2")
    root.add_child(node2)

    node3 = BTAction3(name="Action3")
    root.add_child(node3)
