import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SVG Display")

# Load the SVG image
# Replace 'path/to/your/image.svg' with the actual path to your SVG file
try:
    svg_surface = pygame.image.load('path/to/your/image.svg')
    # You can scale the image if needed
    svg_surface = pygame.transform.scale(svg_surface, (400, 300))
except pygame.error as e:
    print(f"Error loading SVG: {e}")
    pygame.quit()
    exit()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Blit the SVG surface onto the screen
    screen.blit(svg_surface, (100, 100))  # Position at (100, 100)

    # Update the display
    pygame.display.flip()

pygame.quit()