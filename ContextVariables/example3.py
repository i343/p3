import asyncio
from aiocache import Cache

async def main():
    # Configure an in-memory cache
    cache = Cache(Cache.MEMORY)

    # Save a key-value pair
    await cache.set("my_key", "112233")
    print(f"Key 'my_key' saved.")

    # Retrieve the value associated with the key
    value = await cache.get("my_key")
    print(f"Value retrieved for 'my_key': {value}")

    # Delete the key
    await cache.delete("my_key")
    print(f"Key 'my_key' deleted.")

if __name__ == "__main__":
    asyncio.run(main())