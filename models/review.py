from dataclasses import dataclass


@dataclass
class Review:
    rating: int
    comment: str
    date: str
    reviewerName: str
    reviewerEmail: str