from datetime import date

from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        "slug" : "the-mountains",
        "image" : "tree.jpg",
        "author" : "Yash Rawat",
        "date" : date(2021, 7, 21),
        "title" : "Mountain Hiking",
        "excerpt" : "There's nothing like the views you get while hiking in the mountains! I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content" : """
                    Contrary to popular belief, Lorem Ipsum is not simply random text. 
                    It has roots in a piece of classical Latin literature from 45 BC, 
                    making it over 2000 years old. Richard McClintock, a Latin professor
                    at Hampden-Sydney College in Virginia, looked up one of the more obscure
                    Latin words, consectetur, from a Lorem Ipsum passage, and going through 
                    the cites of the word in classical literature, discovered the undoubtable source. 
                    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum 
                    et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.
                     
                    This book is a treatise on the theory of ethics, very popular during the Renaissance. 
                    The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line 
                    in section 1.10.32.
                    """
    },
    {
        "slug" : "programming-is-great",
        "image" : "forest.jpg",
        "author" : "Elon Musk",
        "date" : date(2022, 4, 5),
        "title" : "Programming is great",
        "excerpt" : "There's nothing like the views you get while hiking in the programing. I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content" : """
                    Contrary to popular sheep, Lorem Ipsum is not simply random text. 
                    It has roots in a piece of classical Latin literature from 45 BC, 
                    making it over 2000 years old. Richard McClintock, a Latin professor
                    at Hampden-Sydney College in Virginia, looked up one of the more obscure
                    Latin words, consectetur, from a Lorem Ipsum passage, and going through 
                    the cites of the word in classical literature, discovered the undoubtable source. 
                    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum 
                    et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.
                     
                    This book is a treatise on the theory of ethics, very popular during the Renaissance. 
                    The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line 
                    in section 1.10.32.
                    """
    },
    {
        "slug" : "new-world",
        "image" : "my_image.jpg",
        "author" : "John Doe",
        "date" : date(2024, 1, 25),
        "title" : "The new world update",
        "excerpt" : "There's nothing like the views you get while hiking in the new world. I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content" : """
                    Contrary to popular ram, Lorem Ipsum is not simply random text. 
                    It has roots in a piece of classical Latin literature from 45 BC, 
                    making it over 2000 years old. Richard McClintock, a Latin professor
                    at Hampden-Sydney College in Virginia, looked up one of the more obscure
                    Latin words, consectetur, from a Lorem Ipsum passage, and going through 
                    the cites of the word in classical literature, discovered the undoubtable source. 
                    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum 
                    et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.
                     
                    This book is a treatise on the theory of ethics, very popular during the Renaissance. 
                    The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line 
                    in section 1.10.32.
                    """
    }
]

def my_func(post):
    return post['date']

def starting_page(request):
    selected_post = sorted(all_posts, key=my_func)
    final_post = selected_post[-2:]
    return render(request,"blog/index.html",{
        "posts" : final_post
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post" : identified_post
    })