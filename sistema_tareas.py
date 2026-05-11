# sistema_tareas.py
# Sistema de Gestión de Tareas - Software bajo prueba

class Tarea:
    def __init__(self, id, titulo, descripcion, prioridad="media"):
        if not titulo or not titulo.strip():
            raise ValueError("El título no puede estar vacío.")
        prioridades_validas = ["alta", "media", "baja"]
        if prioridad not in prioridades_validas:
            raise ValueError(f"Prioridad inválida. Use: {prioridades_validas}")
        self.id = id
        self.titulo = titulo.strip()
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def completar(self):
        self.completada = True

    def __repr__(self):
        estado = "✓" if self.completada else "✗"
        return f"[{estado}] #{self.id} - {self.titulo} ({self.prioridad})"


class GestorTareas:
    def __init__(self):
        self.tareas = []
        self._contador = 1

    def agregar_tarea(self, titulo, descripcion="", prioridad="media"):
        tarea = Tarea(self._contador, titulo, descripcion, prioridad)
        self.tareas.append(tarea)
        self._contador += 1
        return tarea

    def eliminar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                self.tareas.remove(tarea)
                return True
        raise ValueError(f"No existe una tarea con ID {id}.")

    def obtener_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
        return None

    def completar_tarea(self, id):
        tarea = self.obtener_tarea(id)
        if tarea is None:
            raise ValueError(f"No existe una tarea con ID {id}.")
        tarea.completar()
        return tarea

    def listar_pendientes(self):
        return [t for t in self.tareas if not t.completada]

    def listar_completadas(self):
        return [t for t in self.tareas if t.completada]

    def filtrar_por_prioridad(self, prioridad):
        return [t for t in self.tareas if t.prioridad == prioridad]
