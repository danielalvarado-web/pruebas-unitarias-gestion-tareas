# test_sistema_tareas.py
# Casos de Prueba Unitaria - Sistema de Gestión de Tareas
# Framework: unittest (Python estándar)

import unittest
from sistema_tareas import Tarea, GestorTareas


class TestCasoPrueba1_AgregarTarea(unittest.TestCase):
    """CP-001: Creación y registro de una tarea válida"""

    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea_valida(self):
        tarea = self.gestor.agregar_tarea("Diseñar base de datos", "Crear esquema ER", "alta")
        self.assertEqual(tarea.titulo, "Diseñar base de datos")
        self.assertEqual(tarea.prioridad, "alta")
        self.assertFalse(tarea.completada)
        self.assertEqual(len(self.gestor.tareas), 1)

    def test_agregar_tarea_sin_titulo_lanza_error(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Sin título")

    def test_agregar_tarea_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("Tarea X", "Desc", "urgente")


class TestCasoPrueba2_CompletarTarea(unittest.TestCase):
    """CP-002: Marcar una tarea como completada"""

    def setUp(self):
        self.gestor = GestorTareas()
        self.tarea = self.gestor.agregar_tarea("Implementar login", "Módulo de autenticación", "alta")

    def test_completar_tarea_existente(self):
        self.gestor.completar_tarea(self.tarea.id)
        self.assertTrue(self.tarea.completada)

    def test_completar_tarea_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.gestor.completar_tarea(999)

    def test_tarea_pasa_a_lista_completadas(self):
        self.gestor.completar_tarea(self.tarea.id)
        self.assertIn(self.tarea, self.gestor.listar_completadas())
        self.assertNotIn(self.tarea, self.gestor.listar_pendientes())


class TestCasoPrueba3_EliminarTarea(unittest.TestCase):
    """CP-003: Eliminación de una tarea del sistema"""

    def setUp(self):
        self.gestor = GestorTareas()
        self.tarea = self.gestor.agregar_tarea("Pruebas de regresión", "QA completo", "media")

    def test_eliminar_tarea_existente(self):
        resultado = self.gestor.eliminar_tarea(self.tarea.id)
        self.assertTrue(resultado)
        self.assertEqual(len(self.gestor.tareas), 0)

    def test_eliminar_tarea_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.gestor.eliminar_tarea(999)

    def test_lista_queda_vacia_tras_eliminar_unica_tarea(self):
        self.gestor.eliminar_tarea(self.tarea.id)
        self.assertEqual(self.gestor.listar_pendientes(), [])


class TestCasoPrueba4_FiltrarPorPrioridad(unittest.TestCase):
    """CP-004: Filtrado de tareas según prioridad"""

    def setUp(self):
        self.gestor = GestorTareas()
        self.gestor.agregar_tarea("Deploy producción", prioridad="alta")
        self.gestor.agregar_tarea("Actualizar docs", prioridad="baja")
        self.gestor.agregar_tarea("Fix bug crítico", prioridad="alta")

    def test_filtrar_tareas_alta_prioridad(self):
        resultado = self.gestor.filtrar_por_prioridad("alta")
        self.assertEqual(len(resultado), 2)

    def test_filtrar_tareas_baja_prioridad(self):
        resultado = self.gestor.filtrar_por_prioridad("baja")
        self.assertEqual(len(resultado), 1)

    def test_filtrar_prioridad_sin_coincidencias(self):
        resultado = self.gestor.filtrar_por_prioridad("media")
        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
