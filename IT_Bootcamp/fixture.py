import attrs
from sqlalchemy import Engine
from typing import Any
import pytest
import sqlalchemy as sa

@attrs.frozen(kw_only=True, slots=True)
class UpdateGroupUseCase:
    postgre_fixture: Engine
    mssql_database_engine: Engine
    mssql_with_tables_and_garbage: Any
    superuser_credentials: Any

    def __call__(self, crm_group_id, **values):
        with self.mssql_database_engine.begin() as connection:
            update_query = (
                sa.update(tables.groups_table)
                .where(tables.groups_table.c.ID == crm_group_id)
                .values(**values)
            )
            connection.execute(update_query)
        synchronize(self.superuser_credentials)


@pytest.fixture()
def update_and_sync_group(
    mssql_create_tables,
    postgre_fixture,
    mssql_database_engine,
    superuser_credentials,
) -> UpdateGroupUseCase:
    usecase = UpdateGroupUseCase(
        mssql_with_tables_and_garbage=mssql_create_tables,
        postgre_fixture=postgre_fixture,
        mssql_database_engine=mssql_database_engine,
        superuser_credentials=superuser_credentials,
    )
    return usecase


@attrs.frozen(kw_only=True, slots=True)
class UpdateLessonUseCase:
    postgre_fixture: Engine
    mssql_database_engine: Engine
    mssql_with_tables_and_garbage: Any
    superuser_credentials: Any

    def __call__(self, crm_lesson_id, **values):
        for key, value in values.items():
            with self.mssql_database_engine.begin() as connection:
                update_query = (
                    sa.update(tables.lessons_table)
                    .where(tables.lessons_table.c.ID == crm_lesson_id)
                    .values(**{key: value})
                )
                connection.execute(update_query)

            synchronize(self.superuser_credentials)


@pytest.fixture()
def update_and_sync_lesson(
    mssql_create_tables,
    postgre_fixture,
    mssql_database_engine,
    superuser_credentials,
) -> UpdateLessonUseCase:
    usecase = UpdateLessonUseCase(
        mssql_with_tables_and_garbage=mssql_create_tables,
        postgre_fixture=postgre_fixture,
        mssql_database_engine=mssql_database_engine,
        superuser_credentials=superuser_credentials,
    )
    return usecase
