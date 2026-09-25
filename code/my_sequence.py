import time
import py_trees
import random


## An action class is declared with the following methods: __init__, setup, initialise and update.
# Each method has its specifics function in order to maintain the correct working of the action.
class BTAction(py_trees.behaviour.Behaviour):

    def __init__(self, name: str = "BTAction"):
        """Configure the name of the behaviour."""
        super(BTAction, self).__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def setup(self, **kwargs: int) -> None:
        """Initialization setup parameters are declared here if necessary."""
        self.logger.debug(f"{self.__class__.__name__}.setup()")

    def initialise(self) -> None:
        """Reset a BTAction variable."""
        self.logger.debug(f"{self.__class__.__name__}.initialise()")
        self.counter = 0

    def update(self) -> py_trees.common.Status:
        self.counter = self.counter + 1
        if self.counter == 3:
            # This variable declaration allows the BT know when the action has finished succesfully
            new_status = py_trees.common.Status.SUCCESS
            self.feedback_message = "Task complete"
        else:
            self.feedback_message = "still counting"
            new_status = py_trees.common.Status.RUNNING

        self.logger.debug(
            f"{self.__class__.__name__}.update()[{self.status} -> {new_status}][{self.feedback_message}]"
        )
        return new_status


def create_root() -> py_trees.behaviour.Behaviour:
    # In this following line, we declare the root node with a sequence node. Inside the parameter configuration, the memory=True allows to the sequence node execute the child nodes in 'sequence' from left to right until receive a FAILURE STATUS from the last child executed. With memory=False, if all the child nodes didn't finish their actions (even though some of them were SUCCESS, the child nodes re-execute their actions again and in order)
    root = py_trees.composites.Sequence(name="Sequence", memory=True)
    # Here we declare the child nodes and bound them to the sequence node declared before (root).
    for action in ["Action 1", "Action 2", "Action 3"]:
        node = BTAction(name=action)
        root.add_child(node)
    return root


def main() -> None:
    # This is a declaration for debugging purposes (mandatory to notice all the process meanwhile the BT is in execution)
    py_trees.logging.level = py_trees.logging.Level.DEBUG
    root = create_root()
    root.setup_with_descendants()

    # Here we declare the tick duration that spreads from all over the BT, in this case, we declare 10 ticks with a 1Hz frequency
    for i in range(0, 7):
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
