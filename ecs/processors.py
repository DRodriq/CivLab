import pygame
import esper
import components

# Define an InputProcessor (System)
class InputProcessor:
    def process(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ent, (pos, clickable, size, rend) in esper.get_components(components.Position, components.Clickable, components.Size, components.Renderable):
                    rect = pygame.rect.Rect(pos.x, pos.y, size.width, size.height)
                    if rect.collidepoint(event.pos) and clickable.on_click:
                        clickable.on_click(ent)  # Pass the entity to the callback
