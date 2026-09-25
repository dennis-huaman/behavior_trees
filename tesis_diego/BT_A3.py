import time
import py_trees
import random
import os

os.system("clear")


class StartLanding(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(StartLanding, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.landing = "OK"
        if self.landing == "OK":
            landing_status = py_trees.common.Status.SUCCESS
            self.feedback_message = "Landing succesfully"
        else:
            landing_status = py_trees.common.Status.FAILURE
            self.feedback_message = "Landing was nos succesfully"
        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {landing_status}][{self.feedback_message}]"
        )
        return landing_status


class FinishedFalse(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(FinishedFalse, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")
        self.counter = 0

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.counter = self.counter + 1
        if self.counter == 5:
            loop_status = py_trees.common.Status.SUCCESS
            self.feedback_message = "Still in loop"
        else:
            loop_status = py_trees.common.Status.FAILURE
            self.feedback_message = "Loop finished"
        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {loop_status}][{self.feedback_message}]"
        )
        return loop_status


class CheckIsLanded(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(CheckIsLanded, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.landing = "OK"
        if self.landing == "OK":
            landing_status = py_trees.common.Status.SUCCESS
            self.feedback_message = "Landed Checked Succesfully"
        else:
            landing_status = py_trees.common.Status.FAILURE
            self.feedback_message = "Landed Fail"
        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {landing_status}][{self.feedback_message}]"
        )
        return landing_status


class CheckAbort(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(CheckAbort, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.checkAbort = "OK"
        if self.checkAbort == "OK":
            abort_check = py_trees.common.Status.SUCCESS
            self.feedback_message = "Abort chequed succesfully"
        else:
            abort_check = py_trees.common.Status.FAILURE
            self.feedback_message = "Abort not checked succesfully"
        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {abort_check}][{self.feedback_message}]"
        )
        return abort_check


class RequestAbort(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(RequestAbort, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.request_abort = "OK"
        if self.request_abort == "OK":
            abort_status = py_trees.common.Status.SUCCESS
            self.feedback_message = "Abort requested"
        else:
            abort_status = py_trees.common.Status.FAILURE
            self.feedback_message = "Abort not requested"
        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {abort_status}][{self.feedback_message}]"
        )
        return abort_status


def create_root() -> py_trees.behaviour.Behaviour:
    first_sequence = py_trees.composites.Sequence("First Secuence", memory=True)
    node1 = StartLanding(name="Start Landing")
    node2 = FinishedFalse(name="Finished False")
    second_sequence = py_trees.composites.Sequence("Second Secuence", memory=True)
    decorator_second_sequence = py_trees.decorators.Repeat(
        "Second Secuence Decorator", child=second_sequence, num_success=-1
    )
    first_sequence.add_children([node1, node2, decorator_second_sequence])

    node3 = CheckIsLanded("Check is Landed")
    third_sequence = py_trees.composites.Sequence("Third Secuence", memory=True)
    decorator_third_sequence = py_trees.decorators.Inverter(
        "Third Secuence Decorator", child=third_sequence
    )
    second_sequence.add_children([decorator_third_sequence, node3])

    node4 = CheckAbort("Check Abort")
    node5 = RequestAbort("Resquest Abort")
    decorator_node5 = py_trees.decorators.Repeat(
        name="Decorator node5", child=node5, num_success=-1
    )
    third_sequence.add_children([node4, decorator_node5])

    return first_sequence


def main() -> None:

    py_trees.logging.level = py_trees.logging.Level.DEBUG

    root = create_root()
    root.setup_with_descendants()

    print(py_trees.display.unicode_tree(root=root, show_status=True))

    for i in range(1, 100):

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
