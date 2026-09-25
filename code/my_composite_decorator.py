import time
import py_trees
import py_trees.decorators
import random


class BTAction1(py_trees.behaviour.Behaviour):

    def __init__(self, name: str = "BTAction1"):
        super(BTAction1, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.logger.debug(f"{self.__class__.__name__}.__update__()")

        random_integer = random.randrange(1, 10)
        if random_integer < 3:
            self.feedback_message = f"Number {random_integer} is less than 3: Success"
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = (
                f"Number {random_integer} is greater than 3: Failure"
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

    def update(self) -> py_trees.common.Status:
        self.logger.debug(f"{self.__class__.__name__}.__update__()")

        random_integer = random.randrange(1, 10)
        if random_integer < 5:
            self.feedback_message = f"Number {random_integer} is less than 5: Success "
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = (
                f"Number {random_integer} is greater than 5: Failure "
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

    def update(self) -> py_trees.common.Status:

        self.logger.debug(f"{self.__class__.__name__}.__update__()")

        random_integer = random.randrange(1, 10)
        if random_integer < 8:
            self.feedback_message = "Number {0} is less than 8: Success ".format(
                random_integer
            )
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "Number {0} is greater than 8: Failure ".format(
                random_integer
            )
            new_status = py_trees.common.Status.FAILURE

        return new_status


def create_root() -> py_trees.behaviour.Behaviour:

    root = py_trees.composites.Selector(name="Selector", memory=False)
    # Decorador Inverter aplicado al nodo selector
    decorated_root = py_trees.decorators.Inverter(
        name="Decorador del Selector", child=root
    )

    node1 = BTAction1(name="Action 1")
    inverterNode1 = py_trees.decorators.Inverter(name="inverterNode1", child=node1)
    root.add_child(inverterNode1)

    node2 = BTAction2(name="Action 2")
    success_is_failure = py_trees.decorators.SuccessIsFailure(
        name="success_is_failure", child=node2
    )
    root.add_child(success_is_failure)

    node3 = BTAction3(name="Action 3")
    inverterNode3 = py_trees.decorators.Inverter(name="inverterNode3", child=node3)
    root.add_child(inverterNode3)
    # Don't forget to return the decorated node of the selector node, instead of only the selector node, because we want the status of the decorator.
    return decorated_root


def main() -> None:

    py_trees.logging.level = py_trees.logging.Level.DEBUG

    root = create_root()
    root.setup_with_descendants()

    print(py_trees.display.unicode_tree(root=root, show_status=True))

    for i in range(1, 6):

        try:
            print("\n--------- Tick {0} ---------\n".format(i))
            root.tick_once()
            print("\n")
            print(py_trees.display.unicode_tree(root=root, show_status=True))
            time.sleep(1.0)
        except KeyboardInterrupt:
            break
    print("\n")


if __name__ == "__main__":
    main()
