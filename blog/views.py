from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Leul1",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whils I was enjoying the view",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.
        """
    },
    {
        "slug": "cut-in-woods",
        "image": "woods.jpg",
        "author": "Leul wood",
        "date": date(2021, 7, 21),
        "title": "woods",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whils I was enjoying the view",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.
        """
    },
    {
        "slug": "coding-time",
        "image": "coding.jpg",
        "author": "Leul code",
        "date": date(2018, 8, 5),
        "title": "coding the great",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whils I was enjoying the view",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Dicta quas eius vitae dolorum tenetur modi, quo nulla minima praesentium. 
            Veritatis atque aliquid quidem perferendis repellat eius libero nisi recusandae magni.
        """
    },
]

# Create your views here.
def starting_page(request):
    # sorted_posts = posts.sort(key=get_date)
    sorted_posts = sorted(all_posts, key=lambda post: post["date"])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })
    

def post_detail(request, slug):
    post = next(post for post in all_posts if post["slug"] == slug)
    
    return render(request, "blog/post-detail.html", {"post": post})


