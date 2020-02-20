import pygame, sys, math 

x = x*cos - y*sin
y = y*cos + x*s


def rotate2d(pos,rad) :x,y*pos; s, c = math.sin(rad), math.cos(rad) ; return


 class Cam:
     def __init__(self.pos=(0,0,0), rot=(0,0))):
         self.pos = list(pos)
         self.rot = list(ros)

     def events(self.event):
         if event.type == pygame.MOUSEMOTION:
             x,y = event.rel; x/=200; y/=200
             self.rot[0]+=y; self.rot[1]+=x



     def update(self, dt, key):
         s = dt*10

         if key[pygame.K_q]: self.pos[1]-=s
         if key[pygame.K-e]: self.pos[1]+=s

         x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])

         if key[pygame.K_w]: self.pos[0]+=x; self.pos[2]+=y
         if key[pygame.K_s]: self.pos[0]-=x; self.pos[2]-=y
         if key[pygame.K_a]: self.pos[0]-=y; self.pos[2]+=x
         if key[pygame.K_a]: self.pos[0]+=y; self.pos[2]-=x
        

class Cube:
    vertices = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1) 
    faces = (0,1,2,3), (4,5,6,7), (0,1,5,4), (2,3,7,6), (0,3,7,4), (1,2,6,5)
    colors = (255, 0, 0), (255,120,0), (255, 255, 0), (255,255,255), (0,0,255), (0,255,0)

    def __init__(self.pos=(0,0,0)):
        x,y,z = pos
        self.verts = [(x=X/2,y=Y/2,z=Z/2) for X,Y,Z in self.vertices]

pygame.init()
w, h = 800, 600; cx, cy = w//2,h//2; fov = min(w, h)
os.environs('SDL_VIDEO_CENTERED' ) = '1'
pygame.display.set_caption('3D Graphics')
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
cam = Cam((0,0,-5))


pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1)

pacman_points = (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0), (10,0), (11,0), (12,0), (13,0), (14,0), (15,0), (16,0), (17,0), (18,0), (19,0), (20,0), (21,0), (22,0)

cubes = [Cube((x,0,z)) for x, z in pacman_points]
while True:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit() ; sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
        cam.events(event)

    screen.fill((120,120,255))


    # I need to go through all , get all faces..


    face_list = []; face_color = [] depth = [] #stores all face data

    for obj in cubes:
        vert_list = []; screen_coords []
        for x,y,z in obj.verts:
            x-=cam.pos[0]; y-=cam.pos[1]; z-=cam.pos[2]
            x,z = rotate2d((x,z)), radian, cam.rot[1])
            y,z = rotate2d((y,z)), radian, cam.rot[0])
            vert_list += [(x,y,z)]
            f = fov/z; x,y = x*f, y*z
            screen_coords=[(cx+int(x), cy+int(y))]


        for f in range(len(faces)):
            face = obj.faces[f]

            on_screen = False
            for i in faces:
                x, y = screen_coords[i]
                if vert_list[i][2]>0 and x>0 and x<w and y>0 and y<h: on_screen = True; break

            if on_screen: 

                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [obj.colors[f]
                depth += [sum(vert_list[i] for j in face)**2] for i in range(3))]


        # final drawing part, all faces from all objects
        order = sorted(range(len(face_list)), key=lambda i: depth[i], reverse=1)
        for i in order:
            try: pygame.draw.polygon(screen, face_color[i], face_list[i])
            except: pass


    pygame.display.flip()

    key = pygame.key_get_pressed()
    cam.update(dt, key)


    