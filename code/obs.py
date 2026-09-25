from pyclbr import Class
import py_trees
from py_trees.common import Status
import time


class CheckBattery(py_trees.behaviour.Behaviour):
    def __init__(self, name: str = "Bateria Suficiente?"):
        super().__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")
        self.battery_level = 50

    def update(self) -> py_trees.common.Status:
        if self.battery_level == 0:
            self.battery_level = 50
        self.logger.debug(f"{self.__class__.__name__}.__update__()")
        self.battery_level = self.battery_level - 1
        self.logger.debug(
            f"{self.__class__.__name__}.__update__()[{self.status} -> [Nivel de batería: {self.battery_level}]"
        )
        if self.battery_level > 20:
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE


class MoveTo(py_trees.behaviour.Behaviour):
    def __init__(self, target, name="MoveTo"):
        super().__init__(name)
        self.logger.debug(f"{self.__class__.__name__}.__init__()")
        self.target = target

    def initialise(self):  # 1 vez, al arrancar
        pass  # (o al re-arrancar tras no-RUNNING)

    def update(self) -> py_trees.common.Status:
        return py_trees.common.Status.SUCCESS  # aún no termino -> me re-tickean

    def terminate(self, new_status):  # al salir de RUNNING (fin o interrupción)
        pass


py_trees.logging.level = py_trees.logging.Level.DEBUG
root = py_trees.composites.Sequence(name="Misión", memory=True)
root.add_children([CheckBattery(), MoveTo("B")])





tree = py_trees.trees.BehaviourTree(root)
tree.setup(timeout=15)


def pre_tick_handler(tree):
    print(py_trees.display.unicode_tree(root, show_status=True))


tree.tick_tock(period_ms=500, pre_tick_handler=pre_tick_handler)
# tree.tick_tock(period_ms=500)  # tickea para siempre (Ctrl-C para parar)
