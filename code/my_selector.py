import time
import py_trees
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
            self.feedback_message = f"Number {random_integer} is less than 5: Success"
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = (
                f"Number {random_integer} is greater than 5: Failure"
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
            self.feedback_message = f"Number {random_integer} is less than 8: Success"
            new_status = py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = (
                f"Number {random_integer} is greater than 8: Failure"
            )
            new_status = py_trees.common.Status.FAILURE
        return new_status


def create_root() -> py_trees.behaviour.Behaviour:

    root = py_trees.composites.Selector(name="Selector", memory=False)
    node1 = BTAction1(name="Action 1")
    root.add_child(node1)

    node2 = BTAction2(name="Action 2")
    root.add_child(node2)

    node3 = BTAction3(name="Action 3")
    root.add_child(node3)

    return root


def main() -> None:

    py_trees.logging.level = py_trees.logging.Level.DEBUG

    root = create_root()
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)

    # El SnapshotVisitor registra que nodos se visitan (se tickean) en cada tick.
    # Es necesario porque display.unicode_tree(show_status=True) pinta el estado
    # *almacenado* de TODOS los nodos, incluidos los que no se ejecutaron en el
    # tick actual (selectores/fallbacks cortan la ejecucion y dejan a los
    # hermanos de menor prioridad con su status y feedback_message antiguos).
    snapshot = py_trees.visitors.SnapshotVisitor()
    tree.visitors.append(snapshot)

    for i in range(1, 6):

        try:
            print("\n--------- Tick {0} ---------\n".format(i))
            tree.tick()
            # Al pasar 'visited' sin 'show_status', solo los nodos realmente
            # tickeados muestran su status y su mensaje de feedback.
            print(py_trees.display.unicode_tree(root=root, visited=snapshot.visited))
            visited_names = [
                node.name for node in root.iterate() if node.id in snapshot.visited
            ]
            print("\nvisited: {0}".format(", ".join(visited_names)))
            tip = root.tip()
            print("tip    : {0}".format(tip.name if tip is not None else "None"))
            time.sleep(1.0)
        except KeyboardInterrupt:
            break
    print("\n")


if __name__ == "__main__":
    main()
