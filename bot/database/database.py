import asyncio
import psycopg2


# Database class for interacting with a PostgreSQL database
class Database:
    def __init__(
            self,
            dsn: str,
            loop: asyncio.AbstractEventLoop,
    ) -> None:
        self.dsn = dsn
        self.loop = loop
        self.conn = psycopg2.connect(dsn=dsn)
        self.cursor = self.conn.cursor()

    # Close the database connection
    async def close_database(self) -> None:
        await self.conn.close()

    # Fetch a report from the database
    async def get_report(self) -> list[tuple]:
        self.cursor.execute(
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

        return self.cursor.fetchall()
