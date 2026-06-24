from sqlalchemy import inspect
from database.db import engine


def get_schema():

    inspector = inspect(engine)

    schema = {}

    for table in inspector.get_table_names():

        schema[table] = {
            "columns": [],
            "primary_keys": [],
            "foreign_keys": []
        }

        columns = inspector.get_columns(table)

        for column in columns:

            schema[table]["columns"].append(
                {
                    "name": column["name"],
                    "type": str(column["type"])
                }
            )

        pk = inspector.get_pk_constraint(table)

        schema[table]["primary_keys"] = pk.get(
            "constrained_columns",
            []
        )

        fks = inspector.get_foreign_keys(table)

        for fk in fks:

            schema[table]["foreign_keys"].append(
                {
                    "column":
                        fk["constrained_columns"],
                    "references":
                        fk["referred_table"]
                }
            )

    return schema