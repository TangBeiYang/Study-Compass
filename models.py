from dataclasses import dataclass, asdict

@dataclass
class Record:
    date: list[int]
    category: str
    title: str
    tags: list[str]
    status: str
    difficulty: int
    blockers: list[str]
    note: str
    id: int | None = None

    def to_dict(self) -> dict:
        return asdict(self)
    
    def print_record(self):
        if len(self.date) == 3:
            y, m, d = self.date
            date_text = f"{y:04d}-{m:02d}-{d:02d}"
        else:
            date_text = str(self.date)
        print(f"id: {self.id}")
        print(f"date: {date_text}")
        print(f"category: {self.category}")
        print(f"title: {self.title}")
        print(f"tags: {' '.join(self.tags) if self.tags else 'None'}")
        print(f"status: {self.status}")
        print(f"difficulty: {self.difficulty}")
        print(f"blockers: {' '.join(self.blockers) if self.blockers else 'None'}")
        print(f"note: {self.note}")
