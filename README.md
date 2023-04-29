A small library for Python that allows you to work conveniently with levels for the game Supercow.
A short example of a primitive program:
```
from supercow_level import Level
Level = Level()

Level.draw_ground(2, 10, 10, 1, 3)
collision_x = Level.ground_to_objects_coordinates(10, 10)[0] + 1
collision_y = Level.ground_to_objects_coordinates(10, 10)[1] + 20
Level.object_create('semirigid', collision_x, collision_y, collision_x + 6, collision_y - 2)
Level.set_settings('Cool level', 8, 0, 3)
Level.save_level('C:/Games/Super Cow/level01')
```
