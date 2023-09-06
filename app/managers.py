import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def all(self) -> list:
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actor_cursor]

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            f"VALUES (?, ?)",
            (first_name_, last_name_)
        )
        self._connection.commit()

    def update(
            self,
            id_to_upd: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "Where id = ?",
            (new_first_name, new_last_name, id_to_upd)
        )
        self._connection.commit()

    def delete(self, id_to_del: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_del,)
        )
        self._connection.commit()
