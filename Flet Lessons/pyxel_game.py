import pyxel

class Game:
    rect_y = 0
    rect_x = 0


    def __init__(self):
         pyxel.init(300, 200, title='my game')
         pyxel.mouse(True)
         pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_W):
             self.rect_x -= 1
        if pyxel.btn(pyxel.KEY_S):
             self.rect_x += 1

        if pyxel.btn(pyxel.KEY_A):
             self.rect_y -= 1
        if pyxel.btn(pyxel.KEY_D):
             self.rect_y += 1

    def draw(self):
         pyxel.cls(0)
         pyxel.text(120, 100, "Hello Pyxel", pyxel.frame_count % 15)
         pyxel.rect(self.rect_y, self.rect_x, 20, 15, 14)
         # pyxel.circ(100, 100, 20, 15)
    
if __name__ == "__main__":
     Game()
