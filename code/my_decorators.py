import time
import py_trees
import py_trees.decorators
import random


class BTAction1(py_trees.behaviour.Behaviour):

    def __init__(self, name: str = "BTAction1"):
        super(BTAction1, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, **kwargs: int) -> None:
        self.logger.debug("%s.setup()" % (self.__class__.__name__))

    def initialise(self) -> None:
        self.logger.debug("%s.initialise()" % (self.__class__.__name__))

    def update(self) -> py_trees.common.Status:
        self.logger.debug("%s.update()" % (self.__class__.__name__))

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
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, **kwargs: int) -> None:
        self.logger.debug("%s.setup()" % (self.__class__.__name__))

    def initialise(self) -> None:
        self.logger.debug("%s.initialise()" % (self.__class__.__name__))

    def update(self) -> py_trees.common.Status:

        self.logger.debug("%s.update()" % (self.__class__.__name__))

        random_integer = random.randrange(1, 10)
        if random_integer < 5:
            self.feedback_message = "Number {0} is less than 5: Success ".format(
                random_integer
            )
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "Number {0} is greater than 5: Failure ".format(
                random_integer
            )
            new_status = py_trees.common.Status.FAILURE

        return new_status


class BTAction3(py_trees.behaviour.Behaviour):

    def __init__(self, name: str = "BTAction3"):
        super(BTAction3, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, **kwargs: int) -> None:
        self.logger.debug("%s.setup()" % (self.__class__.__name__))

    def initialise(self) -> None:
        self.logger.debug("%s.initialise()" % (self.__class__.__name__))

    def update(self) -> py_trees.common.Status:

        self.logger.debug("%s.update()" % (self.__class__.__name__))

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

    root = py_trees.composites.Selector(name="Selector", memory=True)
    node1 = BTAction1(name="Action 1")
    # This following line of code, puts a inverter decorator on the node1, that means that whenever the node1 returns a SUCCESS or a FAILURE status, the decorator will send a FAILURE or SUCCESS status in that order.
    inverterNode1 = py_trees.decorators.Inverter(name="inverterNode1", child=node1)
    root.add_child(inverterNode1)

    node2 = BTAction2(name="Action 2")
    # This following line of code, puts a FailureIsSuccess decorator on the node2, this means that when the node2 returns a SUCCESS status, the decorator will invert only that state.
    failure_is_success = py_trees.decorators.FailureIsSuccess(
        name="failure_is_success", child=node2
    )
    root.add_child(failure_is_success)

    node3 = BTAction3(name="Action 3")
    # This following line of code, puts a SuccessIsFailure decorator on the node3, this means that when the node3 returns a FAILURE status, the decorator will invert only that state.
    success_is_failure = py_trees.decorators.SuccessIsFailure(
        name="success_is_failure", child=node3
    )
    root.add_child(success_is_failure)

    return root


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
