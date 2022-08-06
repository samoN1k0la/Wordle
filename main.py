import pygame, random, json, sys, time
pygame.init()

with open('lista2.json') as f:
    word_list = json.load(f)['wordle']["vocab"]
    answer = random.choice(word_list)
print(answer)

BLACK, WHITE, GRAY, YELLOW, GREEN, DGRAY, BGRAY = (0, 0, 0), (255, 255, 255), (110, 110, 110), (219, 213, 94), (84, 204, 90), (60, 60, 60), (230, 230, 230)
FONT, FONT2, FONT3 = pygame.font.SysFont('mono', 55, bold=True), pygame.font.Font(None, 50), pygame.font.Font(None, 30)
not_allowed = [",", ".", "/", ";", "'", "[", "]", "-", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`", " ", pygame.K_RETURN]
win_res = (400, 540)
icon = pygame.image.load("icon.png")

class InputBox:
    def __init__(self, x, y, w, h, active, text=' ', color = DGRAY, delAllow = True):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = active
        self.delAllow = delAllow
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE and len(self.text) > 2 and self.delAllow:
                    self.text = self.text[:-2]
                else:
                    if(len(self.text) < 10):
                        if event.unicode not in not_allowed:
                            self.text += event.unicode.upper()
                            self.text += " "
                self.txt_surface = FONT.render(self.text, True, self.color)
    def changeColor(self, color):
        self.color = color
        self.txt_surface = FONT.render(self.text, True, self.color)
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
    def gatherText(self):
        return self.text
    def lengthText(self):
        return len(self.text)

class IspisTekst:
    def __init__(self, color, tekst = '', text = '', textRect = ''):
        self.color = color
        self.tekst = tekst
        self.text = FONT2.render(self.tekst, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (200, 570)
    def draw(self, surface):
        surface.blit(self.text, self.textRect)
    def updateText(self, promena):
        self.tekst = promena
        self.text = FONT2.render(self.tekst, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (200, 570)

class checkedCell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, 66, 81))
    def changeColor(self, new_color):
        self.color = new_color

class checkedCellB:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, 66, 81), 3)

def winningScreen(surface):
    surface.fill(WHITE)
    text = FONT3.render('CESTITAMO,  Pogodili ste rec', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (win_res[0] // 2, win_res[1] // 2)
    surface.blit(text, textRect)

win = pygame.display.set_mode(win_res)
pygame.display.set_caption("WORDLE")
pygame.display.set_icon(icon)

input_boxes = [InputBox(12, 15, 340, 80, True), 
               InputBox(12, 100, 340, 80, False), 
               InputBox(12, 185, 340, 80, False), 
               InputBox(12, 270, 340, 80, False), 
               InputBox(12, 355, 340, 80, False), 
               InputBox(12, 440, 340, 80, False)]
               
checkedCells = [[checkedCell(30, 10, WHITE), checkedCell(98, 10, WHITE), checkedCell(166, 10, WHITE), checkedCell(234, 10, WHITE), checkedCell(304, 10, WHITE)], 
                [checkedCell(30, 95, WHITE), checkedCell(98, 95, WHITE), checkedCell(166, 95, WHITE), checkedCell(234, 95, WHITE), checkedCell(304, 95, WHITE)], 
                [checkedCell(30, 180, WHITE), checkedCell(98, 180, WHITE), checkedCell(166, 180, WHITE), checkedCell(234, 180, WHITE), checkedCell(304, 180, WHITE)],
                [checkedCell(30, 265, WHITE), checkedCell(98, 265, WHITE), checkedCell(166, 265, WHITE), checkedCell(234, 265, WHITE), checkedCell(304, 265, WHITE)], 
                [checkedCell(30, 350, WHITE), checkedCell(98, 350, WHITE), checkedCell(166, 350, WHITE), checkedCell(234, 350, WHITE), checkedCell(304, 350, WHITE)], 
                [checkedCell(30, 435, WHITE), checkedCell(98, 435, WHITE), checkedCell(166, 435, WHITE), checkedCell(234, 435, WHITE), checkedCell(304, 435, WHITE)]]

cellBorders = [[checkedCellB(30, 10, DGRAY), checkedCellB(98, 10, DGRAY), checkedCellB(166, 10, DGRAY), checkedCellB(234, 10, DGRAY), checkedCellB(304, 10, DGRAY)], 
                [checkedCellB(30, 95, DGRAY), checkedCellB(98, 95, DGRAY), checkedCellB(166, 95, DGRAY), checkedCellB(234, 95, DGRAY), checkedCellB(304, 95, DGRAY)], 
                [checkedCellB(30, 180, DGRAY), checkedCellB(98, 180, DGRAY), checkedCellB(166, 180, DGRAY), checkedCellB(234, 180, DGRAY), checkedCellB(304, 180, DGRAY)],
                [checkedCellB(30, 265, DGRAY), checkedCellB(98, 265, DGRAY), checkedCellB(166, 265, DGRAY), checkedCellB(234, 265, DGRAY), checkedCellB(304, 265, DGRAY)], 
                [checkedCellB(30, 350, DGRAY), checkedCellB(98, 350, DGRAY), checkedCellB(166, 350, DGRAY), checkedCellB(234, 350, DGRAY), checkedCellB(304, 350, DGRAY)], 
                [checkedCellB(30, 435, DGRAY), checkedCellB(98, 435, DGRAY), checkedCellB(166, 435, DGRAY), checkedCellB(234, 435, DGRAY), checkedCellB(304, 435, DGRAY)]]

zavrsniTekst = IspisTekst(GRAY)

poceo = False

def main():
    global poceo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                sys.exit()
            
            for box in input_boxes:
                box.handle_event(event)
        
        n = 0
        for index, in_box in enumerate(input_boxes):
            temp = in_box.gatherText().replace(" ", "")
            if temp == answer.upper():
                for cell in checkedCells[index]:
                    cell.changeColor(GREEN)
                in_box.changeColor(WHITE)
                for row in checkedCells:
                    for cell in row:
                        cell.draw(win)
                for box in input_boxes:
                    box.draw(win)
                for row in cellBorders:
                    for border in row:
                        border.draw(win)
                pygame.display.update() 
                time.sleep(1)
                winningScreen(win)
                pygame.display.update()  
                time.sleep(1)
                pygame.quit()
                sys.exit()
            else:
                if len(temp) == 5:
                    temp2 = answer.upper()
                    nedozvoljeni = []
                    for i, ch in enumerate(temp):
                        if ch == temp2[i]:
                            checkedCells[index][i].changeColor(GREEN)
                            in_box.changeColor(WHITE)
                            nedozvoljeni.append(i)
                        else:
                            checkedCells[index][i].changeColor(DGRAY)
                            in_box.changeColor(WHITE)
                    for i, ch in enumerate(temp):
                        for j, ch2 in enumerate(temp2):
                            if ch == ch2 and j not in nedozvoljeni:
                                checkedCells[index][i].changeColor(YELLOW)
                                n += 1
                                nedozvoljeni.append(j)
                    if(len(nedozvoljeni) != 0):
                        in_box.delAllow = False
                    
                    n += len(nedozvoljeni)
                    #print(n)
        
        for i in range(0, 5):
            temp = input_boxes[i].gatherText().replace(" ", "") 
            if len(temp) == 5 and n != 0:
                input_boxes[i].active = False
                input_boxes[i+1].active = True
                
        win.fill(BGRAY)
        
        for row in checkedCells:
            for cell in row:
                cell.draw(win)
        for row in cellBorders:
            for border in row:
                border.draw(win)
        for box in input_boxes:
            box.draw(win)
        zavrsniTekst.draw(win)
        pygame.display.update()    

if __name__ == '__main__':
    main()