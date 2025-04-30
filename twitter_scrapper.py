from twscrape import API
import asyncio

async def main():
    api= API()

    await api.pool.add_account("your_username", "your_password", "your_email_linked_to_account","your_email_oassword")
    
    await api.pool.login_all()

    async for tweet in api.search("elon musk", limit=2):
        print(f"{tweet.date} - @{tweet.user.username}: {tweet.rawContent}")

asyncio.run(main())