#!/usr/bin/env python3


import time
import py_trees
import random

import os

os.system("clear")


class BTAction(py_trees.behaviour.Behaviour):

    def __init__(self, name: str = "BTAction"):
        """Configure the name of the behaviour."""
        super(BTAction, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        """No delayed initialisation required for this example."""
        self.logger.debug(f"{self.__class__.__name__}.setup()")

    def initialise(self) -> None:
        """Reset a BTAction variable."""
        self.logger.debug(f"{self.__class__.__name__}.initialise()")
        self.BTAction = 0

    def update(self) -> py_trees.common.Status:

        random_integer = random.randrange(1, 10)
        if random_integer > 5:
            self.feedback_message = (
                f"Number {random_integer} is greater than 5: Failure "
            )
            new_status = py_trees.common.Status.FAILURE
        else:
            self.feedback_message = f"Number {random_integer} is less than 5: Success "
            new_status = py_trees.common.Status.SUCCESS

        return new_status


def create_root() -> py_trees.behaviour.Behaviour:

    root = py_trees.composites.Sequence(
        name="Sequence", memory=True
    )  # With memory = True, the sequence node stills executing the child nodes until receiving a FAILURE (not reloading the actions from the beginning). With memory = False, if all the child nodes didn't finish their actions (even though some of them were SUCCESS, the child nodes re-execute all actions again and in order)

    for action in ["Action 1", "Action 2", "Action 3"]:
        node = BTAction(name=action)
        root.add_child(node)
    return root


def main() -> None:

    py_trees.logging.level = py_trees.logging.Level.DEBUG

    root = create_root()
    root.setup_with_descendants()

    for i in range(1, 6):

        try:
            print(f"\n--------- Tick {i} ---------\n")
            root.tick_once()
            print("\n")
            print(py_trees.display.unicode_tree(root=root, show_status=True))
            time.sleep(1.0)
        except KeyboardInterrupt:
            break
    print("\n")


if __name__ == "__main__":
    main()
