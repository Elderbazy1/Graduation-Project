from django.shortcuts import render ,get_object_or_404 ,redirect , HttpResponseRedirect ,reverse
from .models import Post , Category , comment , Like_dislike , Replay
from django.contrib.auth.models import User


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.

def home (request):

    posts = Post.objects.all()
    catogary = Category.objects.all()
    context = {
        'posts' : posts,
        'catogary' : catogary
    }
    return render(request,'posts/home.html' ,context)

def addnew(request):

    category = Category.objects.all()
    context = {
        'category': category
    }

    if request.method == 'POST' and "btsubmit" in request.POST:
        titel = None
        Price = None
        Description = None
        Category_id = None

        if 'postTitle' in request.POST:
            titel = request.POST['postTitle']
        else:
            pass
        if 'price' in request.POST:
            Price = request.POST['price']
        else:
            pass
        if 'category' in request.POST:
            Category_id = request.POST['category']
        else:
            pass
        if 'postDescription' in request.POST:
            Description = request.POST['postDescription']
        else:
            pass

        # Retrieve the category instance based on the category ID
        try:
            category_instance = Category.objects.get(id=Category_id)  # Use Category_id instead of Category ##
        except Category.DoesNotExist:  # Use Category instead of category
            category_instance = None


        if titel and Price and Description and category_instance :
            post = Post.objects.create(
                titel = titel,
                Price = Price,
                Description = Description,
                auther = request.user,
                Category_id = category_instance ##
            )
            post.save()

    else:
        pass # error

    return render(request, 'posts/addnew.html',context)

def user_posts (request):
    user_postes = Post.objects.filter(auther=request.user)
    context = {
        'posts': user_postes,
    }
    return render(request, 'posts/allpostes.html', context)

def deletpost (request,postdelet):
    if request.user.is_authenticated and postdelet:
        # Get the post object or return a 404 error if it doesn't exist
        post = get_object_or_404(Post, id=postdelet)

        # Check if the current user is the author of the post
        if request.user == post.auther:
            # Delete the post
            post.delete()
            # Redirect to a success page or another view
            return redirect('home')
        else:
            # Return an error or unauthorized access page
            pass
    else:
        # Return an error or unauthorized access page
        pass

# related_products is important
def show_post(request,show):
    post = get_object_or_404(Post, pk=show)
    post.vie_count += 1
    post.save()
    related_products = Post.objects.filter(Category_id=post.Category_id).exclude(id=show).order_by('-publish_date')[:5] ##
    context = {
        'post': post,
        'related_products': related_products

    }
    return render(request, 'posts/details.html', context)

def add_comment(request, addcomment):

    post = get_object_or_404(Post,pk =addcomment)

    if request.method == 'POST':
        text = None
        if 'userComment' in request.POST:
            text = request.POST['userComment']
        else:
            pass

        if text:
            Comment = comment.objects.create(
                text = text,
                post_id = post,
                auther=request.user)
            Comment.save()

            # Get the URL for the post details page using reverse
        post_detail_url = reverse('showpost', kwargs={'show': post.id})

            # Redirect to the post details page
        return HttpResponseRedirect(post_detail_url)

def reaplaycommnet(request , comment_id):
    comme = get_object_or_404(comment , pk = comment_id)
    if request.method == 'POST':
        text = request.POST['userReply']

        if text:
            repaly = Replay.objects.create(
                text=text,
                comment=comme,
                auther=request.user
            )
            repaly.save()

        # Get the URL for the post details page using reverse
    post_detail_url = reverse('reaplaycommnet', kwargs={'comment_id': comme.id})

        # Redirect to the post details page
    return HttpResponseRedirect(post_detail_url)


def search (request):

        search_name = request.GET.get('Search')
        if search_name:
            search_post = Post.objects.filter(titel__icontains = search_name)
        else:
            search_post = Post.objects.none()

        context = {
            'posts' :search_post
        }

        return render(request, 'posts/home.html', context)

def catogery (request, catogery_id):
    # Retrieve the category object based on the provided category_id
    category = Category.objects.get(id=catogery_id)

    # Get all posts in the specified category
    posts = Post.objects.filter(Category_id=category)

    context = {
        'posts': posts,
    }

    return render(request, 'posts/home.html', context)

# this is very important
def edit_post(request,editpost_id):
    post = get_object_or_404(Post, id=editpost_id)
    categories = Category.objects.all()

    if request.method == 'POST' and "btsubmit" in request.POST:
        # Update post with the submitted data
        post.titel = request.POST.get('postTitle')
        post.Description = request.POST.get('postDescription')
        post.Price = request.POST.get('price')

        # Get the selected category

        category = request.POST.get('category')
        category = get_object_or_404(Category, id=category)

        post.Category_id = category

        # Save the changes
        post.save()

        return redirect('home')  # Redirect to the post list page

    # Render the form with the existing data
    context = {
        'post': post,
        'categories': categories,
    }

    return render(request, 'posts/editpost.html', context)


def like_dislike_post(request, post_id, action):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Check if the user has already liked or disliked the post
    existing_vote = Like_dislike.objects.filter(user=user, post=post)

    if existing_vote:
        # If the user already voted, update the vote
        existing_vote.update(likt=(action == 'l'))
    else:
        # If the user hasn't voted, create a new vote
        like_dislike = Like_dislike(user=user, post=post, likt=(action == 'l'))
        like_dislike.save()

    # Calculate likes and dislikes counts
    likes_count = Like_dislike.objects.filter(post=post, likt=True).count()
    dislikes_count = Like_dislike.objects.filter(post=post, likt=False).count()

    # Update the counts in the Post model
    Post.objects.filter(id=post.id).update(likes_count=likes_count, dislikes_count=dislikes_count)

    return redirect('home')  # Redirect to the post detail page

def show_user(request, name):
    user = get_object_or_404(User, username=name)
    posts = Post.objects.filter(auther__username=user)
    context = {
        'posts':posts
    }
    return render(request, 'posts/userprofile.html', context)

def delete_comment(request,delete_comment):

    comment_id = get_object_or_404(comment,id = delete_comment)
    if comment_id.auther == request.user:
        comment_id.delete()

    return redirect('home')

def delete_replay(request , replay_id):
    replayid = get_object_or_404(Replay , pk = replay_id)
    if replayid.auther == request.user:
        replayid.delete()
    return redirect('home')
# Rest api

@api_view(['GET','POST'])
def show_api (request):

    if request.method == 'GET':
        allpost = Post.objects.all()
        serializer = PostSerializer(allpost,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def show_with_pk(request , pk):
    try:
        all = Post.objects.get(pk=pk)
    except all.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(all)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PostSerializer(all, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class show_api_withclass(APIView):

    def get(self , request):
        data = Post.objects.all()
        serializer = PostSerializer(data , many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

    def post(self ,request ):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.data ,status=status.HTTP_400_BAD_REQUEST)


class show_api_withclass_pk(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except Post.DoesNotExists:
            raise Http404

    def get(self,request , pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request , pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self ,request , pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


