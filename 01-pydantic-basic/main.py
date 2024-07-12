from pydantic import BaseModel, Field
import requests

class Post(BaseModel):
    user_id: int = Field(alias='userId')
    id: int
    title: str
    body: str

class Posts(BaseModel):
    posts: list[Post]

url = "https://jsonplaceholder.typicode.com/posts"
req = requests.get(url).json()

posts = Posts(posts=req)

print (posts.model_dump_json())
