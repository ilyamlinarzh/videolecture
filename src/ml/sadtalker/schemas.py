from typing import TypedDict, Optional, Literal


class SadTalkerInferenceConfig(TypedDict):
    enhancer: Optional[Literal['gfpgan']]
    still: Optional[bool]
    expression_scale: Optional[float]
    preprocess: Optional[Literal['crop', 'resize', 'full'] | None]
