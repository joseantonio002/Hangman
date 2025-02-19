'''
https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

Modelo: Gestiona las tareas (crear, editar, eliminar).
Vista: Muestra la lista de tareas en una interfaz gráfica.
Controlador: Recibe las acciones del usuario (como agregar una tarea) y actualiza el modelo y la vista.

'''
from hangmanController import HangmanController
 
if __name__ == "__main__" :
    theApp = HangmanController()
    theApp.on_execute()