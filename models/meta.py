from dataclasses import dataclass


@dataclass
class Meta:
    createdAt: str
    updatedAt: str
    barcode: str
    qrCode: str
