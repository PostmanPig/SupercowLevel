class Level(object):
    def __init__(self):
        self.objects_amount = 0
        self.objects = []

        self.levelname = ''
        self.curlevelback = 0
        self.curleveltask = 0
        self.curlevelmusic = 0

        self.ground0 = [[0] * 256 for i in range(64)]
        self.ground1 = [[0] * 256 for i in range(64)]
        self.ground2 = [[0] * 256 for i in range(64)]
        self.ground3 = [[0] * 256 for i in range(64)]
        self.ground4 = [[0] * 256 for i in range(64)]
        self.ground5 = [[0] * 256 for i in range(64)]

    def object_create(self, name: str, x1: float, y1: float, x2: float, y2: float, drawlayer: int = 1, rotation: float = 0.0, endpos_x: float = 0.0, endpos_y: float = 0.0, invertobj: bool = False, extraparam: str = None):
        self.objects.append({'name': name, 'rect': '{%f,%f,%f,%f}' % (x1, y1, x2, y2), 'drawlayer': drawlayer, 'rotation': rotation, 'endpos': '{%f,%f}' % (endpos_x, endpos_y), 'invertobj': int(invertobj), 'extraparam': extraparam})
        self.objects_amount += 1

    def set_settings(self, levelname: str, curlevelback: int, curleveltask: int, curlevelmusic: int):
        self.levelname = levelname
        self.curlevelback = curlevelback
        self.curleveltask = curleveltask
        self.curlevelmusic = curlevelmusic

    def draw_ground(self, ground: int, x: int, y: int, drawlayer: int = 1, size: int = 3):
        for i in range(size):
            for w in range(size):
                exec(f'self.ground{drawlayer}[y-w][x+i] = ground')

    def save_level(self, name: str = 'level01'):
        with open(name + '.lev', 'w') as l:
            l.write('levelname=' + self.levelname)
            l.write('\nnumlevelobjs=' + str(self.objects_amount))
            l.write('\n\ncurlevelback=' + str(self.curlevelback))
            l.write('\n\ncurleveltask=' + str(self.curleveltask))
            l.write('\n\ncurlevelmusic=' + str(self.curlevelmusic))

            for j in range(self.objects_amount):
                l.write(f'\n\n<obj{j}/>')
                l.write('\n    name=' + self.objects[j]['name'])
                l.write('\n    rect=' + self.objects[j]['rect'])
                l.write('\n    drawlayer=' + str(self.objects[j]['drawlayer']))
                l.write('\n    rotation=' + str(self.objects[j]['rotation']))
                l.write('\n    endpos=' + self.objects[j]['endpos'])
                l.write('\n    invertobj=' + str(self.objects[j]['invertobj']))
                if self.objects[j]['extraparam'] != None:
                    l.write('\n    extrparam=' + self.objects[j]['extrparam'])
                l.write(f'\n</obj{j}>')

            l.write('\n\n\n\n')

            for m in range(6):
                exec(fr'''l.write('\ngroundlayer{m}=\n')
for i in range(len(self.ground{m})):
    for j in range(len(self.ground{m}[i])):
        l.write(str(self.ground{m}[i][j]))
    l.write('\n')''')

    def object_to_ground_coordinates(self, x, y):
        ground_x = int(round((x + 510) / 4))
        ground_y = int(round((110 - y) / 4))
        return ground_x, ground_y

    def ground_to_objects_coordinates(self, x, y):
        object_x = int(round(x * 4 - 510))
        object_y = int(round(110 - y * 4))
        return object_x, object_y
