import pygame

class Sprite:
    def __init__(self, asset_path: str, frame_width: int, frame_height: int) -> None:
        """
        스프라이트 시트를 로드하고 관리합니다.

        :param asset_path: 스프라이트 시트 이미지 파일 경로
        :param frame_width: 각 프레임의 너비
        :param frame_height: 각 프레임의 높이
        """
        self.sheet: pygame.Surface = pygame.image.load(asset_path).convert_alpha()
        self.frame_width: int = frame_width
        self.frame_height: int = frame_height

    def get_sprite_frame(self, frame_x: int, frame_y: int) -> pygame.Surface:
        """
        스프라이트 시트에서 특정 프레임을 인덱스로 가져옵니다.

        :param frame_x: 가져올 프레임의 x 인덱스
        :param frame_y: 가져올 프레임의 y 인덱스
        :return: 잘라낸 이미지 (pygame.Surface)
        """
        rect = pygame.Rect(frame_x * self.frame_width, frame_y * self.frame_height, self.frame_width, self.frame_height)
        frame = self.sheet.subsurface(rect).copy()
        return frame

def get_sprite_frame(asset_path: str, frame_x: int, frame_y: int, frame_width: int, frame_height: int) -> pygame.Surface | None:
    """
    지정된 경로의 이미지에서 특정 프레임을 잘라내어 반환합니다.

    :param asset_path: 이미지 파일 경로
    :param frame_x: 잘라낼 프레임의 x 좌표 (픽셀 단위)
    :param frame_y: 잘라낼 프레임의 y 좌표 (픽셀 단위)
    :param frame_width: 잘라낼 프레임의 너비 (픽셀 단위)
    :param frame_height: 잘라낼 프레임의 높이 (픽셀 단위)
    :return: 잘라낸 이미지 (pygame.Surface)
    """
    try:
        full_image = pygame.image.load(asset_path).convert_alpha()
        char_rect = pygame.Rect(frame_x, frame_y, frame_width, frame_height)
        sprite_frame = full_image.subsurface(char_rect).copy()
        return sprite_frame
    except pygame.error as e:
        print(f"Error loading or slicing sprite: {e}")
        return None
