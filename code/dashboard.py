import time
import py_trees
import os

os.system("clear")


class Node1(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.blackboard = self.attach_blackboard_client()

        self.blackboard.register_key(
            key="current_speed", access=py_trees.common.Access.READ
        )
        self.blackboard.register_key(
            key="current_speed", access=py_trees.common.Access.WRITE
        )
        self.blackboard.register_key(
            key="maximum_speed", access=py_trees.common.Access.READ
        )
        self.blackboard.register_key(key="status", access=py_trees.common.Access.READ)

    def update(self) -> py_trees.common.Status:
        try:
            c_speed = self.blackboard.current_speed
            self.blackboard.current_speed = c_speed + 0.1
            success_indicator = self.blackboard.status
            print(f"{success_indicator}-.-.-.-.-.-")
        except KeyError:
            success_indicator = self.blackboard.status
            pass

        if success_indicator == "success":
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE


class Node2(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super().__init__(name)

        self.blackboard = self.attach_blackboard_client()
        self.blackboard.register_key(
            key="maximum_speed", access=py_trees.common.Access.READ
        )
        self.blackboard.register_key(
            key="current_speed", access=py_trees.common.Access.READ
        )
        self.blackboard.register_key(key="status", access=py_trees.common.Access.WRITE)

        self.blackboard.status = "success"

    def update(self) -> py_trees.common.Status:

        print(self.blackboard)

        if self.blackboard.current_speed > self.blackboard.maximum_speed:
            self.blackboard.status = "failure"
            return py_trees.common.Status.FAILURE
        else:
            self.blackboard.status = "success"
            return py_trees.common.Status.SUCCESS


def create_root() -> py_trees.behaviour.Behaviour:

    root = py_trees.composites.Parallel(
        name="Blackboard Demo", policy=py_trees.common.ParallelPolicy.SuccessOnAll()
    )
    node_1 = Node1(name="Writer")
    node_2 = Node2(name="ParamsAndState")

    root.add_children([node_1, node_2])
    return root


def main() -> None:
    py_trees.logging.level = py_trees.logging.Level.DEBUG
    blackboard = py_trees.blackboard.Client()
    blackboard.register_key(key="maximum_speed", access=py_trees.common.Access.WRITE)
    blackboard.register_key(key="current_speed", access=py_trees.common.Access.WRITE)
    blackboard.maximum_speed = 0.5
    blackboard.current_speed = 0.0

    print(blackboard)

    time.sleep(1)
    root = create_root()
    root.setup_with_descendants()

    i = 0

    for i in range(0, 10, 1):
        try:
            print("\n--------- Tick {0} ---------\n".format(i))
            root.tick_once()
            print("\n")
            print(py_trees.display.unicode_tree(root=root, show_status=True))
            i += 1
        except KeyboardInterrupt:
            break

        time.sleep(0.5)


if __name__ == "__main__":
    main()
