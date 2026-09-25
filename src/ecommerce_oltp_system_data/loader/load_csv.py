from pathlib import Path
import psycopg

def load_csv(
    connection: psycopg.Connection,
    table_name: str,
    csv_path: Path,
) -> None:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with connection.cursor() as cursor:
        with csv_path.open(
            mode="r",
            encoding="utf-8",
        ) as file:
            with cursor.copy(
                f"""
                COPY {table_name}
                FROM STDIN
                WITH (
                    FORMAT CSV,
                    HEADER TRUE
                )
                """
            ) as copy:
                while data := file.read(1024 * 1024):
                    copy.write(data)

    print(f"Loaded {csv_path.name} -> {table_name}")