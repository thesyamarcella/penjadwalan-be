from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List
from sqlalchemy import String, ForeignKey, DateTime, Boolean
from datetime import datetime

from . import Base

class Jadwal(Base):
    __tablename__ = "jadwal"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_slot: Mapped[int] = mapped_column(ForeignKey("slot.id"))
    slot: Mapped["Slot"] = relationship("Slot", back_populates="jadwal", lazy="selectin")
    
    id_ruangan: Mapped[int] = mapped_column(ForeignKey("ruangan.id"))
    ruangan: Mapped["Ruangan"] = relationship("Ruangan", back_populates="jadwal", lazy="selectin")

    id_pengajaran: Mapped[int] = mapped_column(ForeignKey("pengajaran.id"))
    pengajaran: Mapped["Pengajaran"] = relationship("Pengajaran", back_populates="jadwal", lazy="selectin")

    start_date_time: Mapped[datetime] = mapped_column(DateTime)
    end_date_time: Mapped[datetime] = mapped_column(DateTime)

    is_created: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)  

from .slot_model import Slot
from .ruangan_model import Ruangan
from .pengajaran_model import Pengajaran