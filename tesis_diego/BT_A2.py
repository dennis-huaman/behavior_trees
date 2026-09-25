import py_trees
from py_trees.common import Status


# Definición de acciones
class SetFlightPlan(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(SetFlightPlan, self).__init__(name)
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


class StartToGo(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(StartToGo, self).__init__(name)
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


class PipeDetection(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(PipeDetection, self).__init__(name)
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


class CheckAbort(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(CheckAbort, self).__init__(name)
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


class RequestAbort(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(RequestAbort, self).__init__(name)
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


class CheckCloseToPipe(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(CheckCloseToPipe, self).__init__(name)
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


class ActivatePipeDetector(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(ActivatePipeDetector, self).__init__(name)
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


class CheckPipeDetected(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(CheckPipeDetected, self).__init__(name)
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


class CheckIsHovering(py_trees.behaviour.Behaviour):
    def __init__(self, name: str):
        super(CheckIsHovering, self).__init__(name)
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


# Creacion del arbol, definicion de jerarquía
def create_root() -> py_trees.behaviour.Behaviour:

    # Definicion de los nodos accion
    set_flight_plan = SetFlightPlan(name="set_flight_plan")
    start_to_go = StartToGo(name="start_to_go")
    pipe_detected = PipeDetection(name="pipe_detected")
    check_abort = CheckAbort(name="check_abort")
    request_abort_fourth_sequence = RequestAbort(name="request_abort4s")
    request_abort_fifth_sequence = RequestAbort(name="request_abort5s")
    check_close_to_pipe = CheckCloseToPipe(name="check_close_to_pipe")
    activate_pipe_detector = ActivatePipeDetector(name="activate_pipe_detector")
    check_pipe_detected = CheckPipeDetected(name="check_pipe_detected")
    check_is_hovering = CheckIsHovering(name="check_is_hovering")

    # Definicion de los nodos composites del BT
    first_sequence = py_trees.composites.Sequence(name="first_sequence", memory=False)
    second_sequence = py_trees.composites.Sequence(name="second_sequence", memory=False)
    third_sequence = py_trees.composites.Sequence(name="third_sequence", memory=False)
    fourth_sequence = py_trees.composites.Sequence(name="fourth_sequence", memory=False)
    fifth_sequence = py_trees.composites.Sequence(name="fifth_sequence", memory=True)
    first_fallback = py_trees.composites.Selector(name="first_fallback", memory=False)

    # Definicion de los decoradores de los composites
    decorador_second_sequence = py_trees.decorators.Retry(
        name="decorador_second_sequence", child=second_sequence, num_failures=3
    )
    decorador_third_sequence = py_trees.decorators.Retry(
        name="decorador_third_sequence", child=third_sequence, num_failures=3
    )
    decorador_fourth_sequence = py_trees.decorators.Inverter(
        name="decorador_fourth_sequence", child=fourth_sequence
    )

    # Definicion de los decoradores de los nodos de accion
    decorador_request_abort_fourth_sequence = py_trees.decorators.Retry(
        name="decorador_request_abort_fourth_sequence",
        child=request_abort_fourth_sequence,
        num_failures=3,
    )
    decorador_request_abort_fifth_sequence = py_trees.decorators.Retry(
        name="decorador_request_abort_fifth_sequence",
        child=request_abort_fifth_sequence,
        num_failures=3,
    )
    decorador_activate_pipe_detector = py_trees.decorators.Retry(
        name="decorador_activate_pipe_detector",
        child=activate_pipe_detector,
        num_failures=3,
    )

    # Composicion de la jerarquía
    first_sequence.add_children([set_flight_plan, decorador_second_sequence])
    second_sequence.add_children([start_to_go, decorador_third_sequence, pipe_detected])
    third_sequence.add_children([decorador_fourth_sequence, first_fallback])
    fourth_sequence.add_children([check_abort, decorador_request_abort_fourth_sequence])
    first_fallback.add_children([fifth_sequence, check_is_hovering])
    fifth_sequence.add_children(
        [
            check_close_to_pipe,
            decorador_activate_pipe_detector,
            check_pipe_detected,
            decorador_request_abort_fifth_sequence,
        ]
    )

    # Devolvemos solo la raiz del BT, como el nodo root esta decorado, devolvemos el decorador en lugar del nodo root
    return first_sequence


def main() -> None:
    # Linea para imprimir en CLI el log de ejecucion del BT
    py_trees.logging.level = py_trees.logging.Level.DEBUG
    root = create_root()
    root.setup_with_descendants()
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)

    # Se declara esta funcion para imprimir en consola la estructura del arbol
    def post_tick_handler(tree):
        print(f"\n--------- Tick {tree.count} ---------\n")
        print(py_trees.display.unicode_tree(root, show_status=True))

    tree.tick_tock(period_ms=2000, post_tick_handler=post_tick_handler)


if __name__ == "__main__":
    main()
