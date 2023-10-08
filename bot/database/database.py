import asyncio
import asyncpg


class Database:
    def __init__(
            self,
            dsn: str,
            loop: asyncio.AbstractEventLoop,
    ) -> None:
        self.dsn = dsn
        self.loop = loop
        self.pool = loop.run_until_complete(asyncpg.create_pool(dsn=dsn, loop=loop))

    async def close_database(self) -> None:
        await self.pool.close()

    async def get_report(self) -> list[asyncpg.Record]:
        response = await self.pool.fetch(
            """
with deleteDuplicates(subject) as (
    select case
        when lower(subject) like '%петербург' or
            lower(subject) like '%питер' then 'Санкт-Петербург'
        --
        -- Template for removing duplicates of any city:
        --
        -- when lower(subject) like '<keyword_for_find_duplicate>' then '<correct_city>'
        --
        else subject
        end, doses_count, ex_days
    from overdue
)
select subject "Субъект РФ", sum(doses_count) "Суммарное количество доз", round(avg(ex_days)) "Среднее просрочено дней"
from deleteDuplicates
group by subject;
"""
        )

        return response
