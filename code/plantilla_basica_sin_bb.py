import py_trees
from py_trees.common import Status


# Definición de acciones
class GenericAction1(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(GenericAction1, self).__init__(name)
        # Indica en el log que método del comportamiento se esta ejecutando
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.logger.debug(f"{self.__class__.__name__}.__update__()")
        # Logica interna para devolver status
        return py_trees.common.Status.SUCCESS

    def terminate(self, new_status: Status) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__terminate__()")
        pass


class GenericAction2(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(GenericAction2, self).__init__(name)
        # Indica en el log que método del comportamiento se esta ejecutando
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.logger.debug(f"{self.__class__.__name__}.__update__()")
        # Logica interna para devolver status
        return py_trees.common.Status.SUCCESS

    def terminate(self, new_status: Status) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__terminate__()")
        pass


class GenericAction3(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(GenericAction3, self).__init__(name)
        # Indica en el log que método del comportamiento se esta ejecutando
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.logger.debug(f"{self.__class__.__name__}.__update__()")
        # Logica interna para devolver status
        return py_trees.common.Status.SUCCESS

    def terminate(self, new_status: Status) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__terminate__()")
        pass


class GenericAction4(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(GenericAction4, self).__init__(name)
        # Indica en el log que método del comportamiento se esta ejecutando
        self.logger.debug(f"{self.__class__.__name__}.__init__()")

    def initialise(self) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__initialise__()")

    def update(self) -> py_trees.common.Status:
        self.logger.debug(f"{self.__class__.__name__}.__update__()")
        # Logica interna para devolver status
        return py_trees.common.Status.FAILURE

    def terminate(self, new_status: Status) -> None:
        self.logger.debug(f"{self.__class__.__name__}.__terminate__()")
        pass


# Creacion del arbol, definicion de jerarquía
def create_root() -> py_trees.behaviour.Behaviour:

    # Asignacion de las acciones a un nodo declarado
    nodo1 = GenericAction1(name="Nodo1")
    nodo2 = GenericAction2(name="Nodo2")
    nodo3 = GenericAction3(name="Nodo3")
    nodo4 = GenericAction4(name="Nodo4")

    # Definicion de un nodo fallback
    selector = py_trees.composites.Selector(name="Fallback", memory=True)

    # Asignacion de nodos hijos a un nodo selector
    selector.add_children([nodo1, nodo2])

    # Definicion de un nodo sequence
    sequence = py_trees.composites.Sequence(name="Sequence", memory=True)

    # Asignacion de un nodo hijo a un nodo sequence
    sequence.add_child(nodo3)

    # Definicion de un nodo parallel
    parallel = py_trees.composites.Parallel(
        name="Parallel", policy=py_trees.common.ParallelPolicy.SuccessOnAll()
    )

    # Asignacion de un nodo hijo a un nodo parallel
    parallel.add_child(nodo4)

    # Definicion de un nodo pseudo maestro (para el ejemplo)
    root = py_trees.composites.Sequence(name="Pre Root", memory=True)
    root.add_children([selector, sequence, parallel])

    # Decorador del nodo pseudo maestro
    decorador_root = py_trees.decorators.Inverter(
        name="Inversor del Master", child=root
    )

    # Devolvemos solo la raiz del BT, como el nodo root esta decorado, devolvemos el decorador en lugar del nodo root
    return decorador_root


def main() -> None:
    # Linea para imprimir en CLI el log de ejecucion del BT
    py_trees.logging.level = py_trees.logging.Level.DEBUG
    root = create_root()
    root.setup_with_descendants()
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)

    # Se declara esta funcion para imprimir en consola la estructura del arbol
    def post_tick_handler(tree):
        print(py_trees.display.unicode_tree(root, show_status=True))

    tree.tick_tock(period_ms=1000, post_tick_handler=post_tick_handler)


if __name__ == "__main__":
    main()
