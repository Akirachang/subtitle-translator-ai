import re

from pydantic import BaseModel, Field, field_validator


class SubtitleBlock(BaseModel):
    block: str = Field(..., description="Raw subtitle block text")
    index: int
    start_time: str
    end_time: str
    text: str

    @field_validator("block", mode="after")
    def parse_block(cls, block):
        lines = block.strip().split("\n")
        if len(lines) < 3:
            raise ValueError("Invalid subtitle block format")

        try:
            index = int(lines[0])
        except ValueError:
            raise ValueError("Index must be an integer")

        time_match = re.match(
            r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})", lines[1]
        )
        if not time_match:
            raise ValueError("Second line must contain valid SRT time range")

        start_time = lines[1]
        end_time = lines[2]
        text = "\n".join(lines[2:]).strip()

        cls.index = index
        cls.start_time = start_time
        cls.end_time = end_time
        cls.text = text

        return block
