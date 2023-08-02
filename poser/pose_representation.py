from dataclasses import dataclass

from poser.rotation_handler import Rotation
from poser.translation_representation import Translation


@dataclass
class Pose(object):
    translation: Translation
    rotation: Rotation

    def __invert__(self) -> "Pose":
        new_rot = ~self.rotation
        return Pose(
            translation=new_rot.transformed_point(~self.translation),
            rotation=new_rot,
        )
