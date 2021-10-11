from fastapi import APIRouter


posts_fetcher = APIRouter()


@posts_fetcher.get("/get-all-objects/")
def get_all_obj():
    from Logic.models import BlogTable

    objs: list = list(BlogTable.objects.all())
    return objs


@posts_fetcher.get("/{post_id}")
def query_posts(post_id: str):
    from Logic.models import BlogTable

    query = BlogTable.objects.get(Identifier=post_id)
    return [query]
