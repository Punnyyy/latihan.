import asyncio
import aiohttp

API_KEY = 'c45c0dd80d6bd4b9da19b27a725bec73'
BASE_URL = 'https://api.themoviedb.org/3/movie'

async def fetch_movie(session, movie_id):
    url = f"{BASE_URL}/{movie_id}?api_key={API_KEY}&language=en-US"
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return {
                'title': data['title'],
                'release_date': data['release_date'],
                'overview': data['overview']
            
            }
        else:   
            return {'id': movie_id, 'error': 'Movie not found'}

async def main(movie_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_movie(session, movie_id) for movie_id in movie_ids]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    # Daftar ID film yang ingin diambil informasinya
    movie_ids = [883112, 299536, 306674, 664201, 181812, 974796] 
    movie_data = asyncio.run(main(movie_ids))
    
    for data in movie_data:
        if 'error' in data:
            print(f"Error fetching data for movie ID {data['id']}: {data['error']}")
        else:
            print(f"Title: {data['title']}, Release Date: {data['release_date']}, Overview: {data['overview'][:100]}...")  # Menampilkan 100 karakter pertama dari overview