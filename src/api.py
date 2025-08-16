import re

from pydantic import BaseModel, Field, model_validator


class SubtitleBlock(BaseModel):
    block: str = Field(..., description="Raw subtitle block text")
    index: int = None
    start_time: str = None
    end_time: str = None
    text: str = None

    @model_validator(mode="after")
    def parse_block(self):
        lines = self.block.strip().split("\n")
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

        start_time, end_time = lines[1].split(" --> ")
        text = "\n".join(lines[2:]).strip().replace("<b>", "").replace("</b>", "")

        self.index = index
        self.start_time = start_time
        self.end_time = end_time
        self.text = text
        return self

    def __str__(self):
        return f"SubtitleBlock(index={self.index}, start_time={self.start_time}, end_time={self.end_time}, text={self.text})"
