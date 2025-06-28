
from fastapi import FastAPI
from app.webservices.user_web_service import router as api_router

app = FastAPI(title="Confirm App API")
app.include_router(api_router)




"""
class Movie(BaseModel):
    id: Optional[int] = None
    title: str

class MovieCreate(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15, default='My Movie')



app.title = "ConfirmApp"
app.version = "1.0"

movies = [
    {
        'id':1,
        'title':"Action"
    }
]
@app.get('/', tags=['home'])
def home():
    return {"hello":"word"}

@app.get('/movies', tags=['movies'])
def get_movies() -> List[Movie]:
    return movies


@app.get('/movies/{id}',  tags=['movies'])
def movie(id: int):
    return id


@app.get('/movies/', tags=['movies'])
def movie_cate(category: str):
    return category



@app.post('/movies',  tags=['home'])
def create_movie(movie: MovieCreate):
    movies.append(movie.model_dump())

    return movies.pop()


@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
    return movies


@app.delete('/movies/{id}',  tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies

"""