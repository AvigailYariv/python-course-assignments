import datetime
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class AgeCalculator:
    """
    Holds a birth date and computes age in years and months.
    Use AgeCalculator.from_string("DD/MM/YYYY") to create an instance.
    """
    birthdate: datetime.date

    @classmethod
    def from_string(cls, s: str) -> "AgeCalculator":
        try:
            day, month, year = map(int, s.strip().split('/'))
            birth = datetime.date(year, month, day)
        except Exception as exc:
            raise ValueError("Date must be in DD/MM/YYYY format.") from exc
        return cls(birth)

    def calculate(self, today: Optional[datetime.date] = None) -> Tuple[int, int]:
        """
        Return (years, months) representing age at `today`.
        If today is None, uses current date.
        Raises ValueError if birthdate is in the future.
        """
        if today is None:
            today = datetime.date.today()
        if self.birthdate > today:
            raise ValueError("Birthday is in the future.")
        years = today.year - self.birthdate.year
        months = today.month - self.birthdate.month
        days = today.day - self.birthdate.day
        if days < 0:
            months -= 1
        if months < 0:
            years -= 1
            months += 12
        return years, months

# Convenience function
def calculate_age_from_string(s: str) -> Tuple[int, int]:
    return AgeCalculator.from_string(s).calculate()