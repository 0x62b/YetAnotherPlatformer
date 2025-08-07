import pygame

class Utils:
    @staticmethod
    def load_image(path):
        try:
            image = pygame.image.load(path)
            return image.convert_alpha()
        except pygame.error as e:
            print(f"Unable to load image at {path}: {e}")
            return None

    @staticmethod
    def get_level(level):
        match level:
            case 1:
                import levels.level1
                return levels.level1
            case 2:
                import levels.level2
                return levels.level2
            case 3:
                import levels.level3
                return levels.level3
            case _:
                raise ValueError(f"Unknown level: {level}")