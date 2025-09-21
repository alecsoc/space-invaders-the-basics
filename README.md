# 👾 Space Invaders: The Basics (by Alejandro Capriles/alecso caprix)

Space Invaders: The Basics es un videojuego de prueba técnica, el que era y es mi primer proyecto de programación como tal. Está evidentemente basado en el famoso y clásico juego de arcade matamarcianos [*Space Invaders*](https://es.wikipedia.org/wiki/Space_Invaders).

## Origen del proyecto

Este fue mi primer proyecto publicado en GitHub, desarrollado originalmente en el TechCamp **Adakademy 2022**, durante el curso de *Diseño de Videojuegos con Python*.  
La versión inicial fue una implementación básica centrada en entender los fundamentos y la lógica de la programación, mediante el uso de la librería de *Pygame*.

A finales del año 2025, el proyecto ha sido refactorizado por completo para demostrar una evolución técnica y conceptual, incluyendo cosas como:
- Implementación del paradigma de Programación Orientada a Objetos (POO)
- Separación modular por responsabilidades
- HUD personalizado con sistema de Game Over  
- Integración de sonido con sistema propio (`SoundPlayer`)
- Colisiones optimizadas con `pygame.Rect`  
- Mejoras en correlación a la lógica de la jugabilidad (distribución de los enemigos, incremento de velocidad progresivo, nuevo puntaje en decenas, entre otras cosas)

## Estructura del proyecto


```
Space Invaders - The Basics/
├── assets/
│   ├── fonts/
│   ├── images/
│   └── sounds/
│
├── src/
│   ├── core/
│   │   ├── game.py
│   │   ├── settings.py
│   │   └── soundplayer.py
│   │
│   ├── entities/
│   │   ├── bullet.py
│   │   ├── enemy.py
│   │   └── player.py
│   │
│   ├── hud/
│   │   ├── gameover.py
│   │   └── scoreboard.py
│   │
│   └── main.py
```

## Instalación y cómo jugar

### Requisitos
- Python 3.10 o superior
- Pygame instalado

```bash
pip install pygame
```

### Instalación

Descarga directamente como archivo `.ZIP` desde GitHub.

1. Ir al repositorio en GitHub
2. Hacer clic en el botón "Code"
3. Seleccionar "Download ZIP"
4. Extraer el contenido en tu carpeta de trabajo

Alternativamente, puedes clonar el repositorio con Git:

```bash
> git clone https://github.com/tu_usuario/space-invaders-the-basics.git
> cd space-invaders-the-basics
```

### Ejecución del juego


```bash
python src/main.py
```

### Controles

| Acción | Teclas |
| --- | --- |
| Mover al jugador | ← / → |
| Disparar | Espacio |
| Reiniciar tras Game Over | Enter |

___

<br>

Space Invaders: The Basics is a technical test game — the one that was and still is my first programming project. It’s clearly inspired by the famous and classic arcade shoot ’em up game [*Space Invaders*](https://en.wikipedia.org/wiki/Space_Invaders).

## Origin of the project

This was my first project published on GitHub, originally developed at the TechCamp **Adakademy 2022**, during the course “Videogame Design with Python.”  
The initial version was a basic implementation focused on understanding programming fundamentals and logic using the Pygame library.

By late 2025, the project has been completely refactored to demonstrate technical and conceptual evolution, including:
- Implementation of the Object-Oriented Programming (OOP) paradigm  
- Modular separation by responsibilities  
- Custom HUD with a Game Over system  
- Sound integration with a dedicated system (`SoundPlayer`)  
- Optimized collisions using `pygame.Rect`  
- Gameplay logic improvements (enemy distribution, progressive speed increase, new scoring in tens, among other things)

## Project structure

```
Space Invaders - The Basics/
├── assets/
│   ├── fonts/
│   ├── images/
│   └── sounds/
│
├── src/
│   ├── core/
│   │   ├── game.py
│   │   ├── settings.py
│   │   └── soundplayer.py
│   │
│   ├── entities/
│   │   ├── bullet.py
│   │   ├── enemy.py
│   │   └── player.py
│   │
│   ├── hud/
│   │   ├── gameover.py
│   │   └── scoreboard.py
│   │
│   └── main.py
```

## Installation and how to play

### Requirements
- Python 3.10 or higher
- Pygame installed

```bash
pip install pygame
```

### Installation

Download directly as a `.ZIP` file from GitHub.

1. Go to the repository on GitHub
2. Click the “Code” button
3. Select “Download ZIP”
4. Extract the contents to your working folder

Alternatively, you can clone the repository with Git:

```bash
git clone https://github.com/tu_usuario/space-invaders-the-basics.git
cd space-invaders-the-basics
```

### Run the game

```bash
python src/main.py
```

### Controls

| Action | Keys |
| --- | --- |
| Move the player | ← / → |
| Shoot | Space |
| Restart after Game Over | Enter |