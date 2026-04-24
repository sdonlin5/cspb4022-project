import asyncio
from database.db import drop_all

async def main():
    print("Dropping tables...")
    await drop_all()
    print("All tables removed from database.")

if __name__ == '__main__':
    asyncio.run(main())