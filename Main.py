import pygame


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.w, self.h = screen.get_size()
        self.running = True
        self.clock = pygame.time.Clock()

    def handling_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        pass

    def display(self):
        self.screen.fill((0, 0, 0))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update(self.clock.get_time()/1_000)
            self.display()
            self.clock.tick()


pygame.init()
win = pygame.display.set_mode((800, 800))
game = Game(win)
game.run()
pygame.quit()
