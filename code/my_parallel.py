import time
import py_trees
import random
import os

os.system("clear")


class Node1(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(Node1, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.random_number = random.randrange(0, 10)
        self.feedback_message = f"Maximum speed: {self.random_number}"
        if self.random_number < 5:
            new_status = py_trees.common.Status.SUCCESS
        else:
            new_status = py_trees.common.Status.FAILURE
        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {new_status}][{self.feedback_message}]"
        )
        return new_status


class Node2(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(Node2, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__setup__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.random_number = random.randrange(0, 10)
        self.feedback_message = f"Variable value: {self.random_number}"
        if self.random_number < 5:
            new_status = py_trees.common.Status.SUCCESS
        else:
            new_status = py_trees.common.Status.RUNNING
        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {new_status}][{self.feedback_message}]"
        )
        return new_status


def create_root() -> py_trees.behaviour.Behaviour:

    root = py_trees.composites.Parallel(
        name="Parallel", policy=py_trees.common.ParallelPolicy.SuccessOnOne()
    )
    node_1 = Node1(name="Nodo1")
    node_2 = Node2(name="Nodo2")

    root.add_children([node_1, node_2])
    return root


def main() -> None:
    py_trees.logging.level = py_trees.logging.Level.DEBUG
    root = create_root()
    root.setup_with_descendants()

    for i in range(0, 10, 1):
        try:
            print("\n--------- Tick {0} ---------\n".format(i))
            root.tick_once()
            print("\n")
            print(py_trees.display.unicode_tree(root=root, show_status=True))
            time.sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
