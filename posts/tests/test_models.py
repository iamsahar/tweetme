# from django.test import TestCase
# from posts.models import Post, Comment
# from django.contrib.auth.models import User
# from django.utils import timezone


# class PostModelTest(TestCase):
#     def test_create_post(self):
#         # Create the post
#         post = Post()
#         # Set the attributes
#         u = User(username="username", password="password")
#         u.save()
#         post.author = u
#         post.content = 'My first post'
#         post.date_posted = timezone.now()
#         # Save it
#         post.save()
#         # Check we can find it
#         all_posts = Post.objects.all()
#         self.assertEquals(len(all_posts), 1)
#         only_post = all_posts[0]
#         self.assertEquals(only_post, post)

# class CommentModelTest(TestCase):
#     def test_create_comment(self):
#         # Create the post
#         comment = Comment()
#         # Set the attributes
#         u = User(username="username", password="password")
#         u.save()
#         p = Post(content="content", author = u)
#         p.save()
#         comment.post = p
#         comment.comment = 'My first comment'
#         # Save it
#         comment.save()
#         # Check we can find it
#         all_comments = Comment.objects.all()
#         self.assertEquals(len(all_comments), 1)
#         only_comment = all_comments[0]
#         self.assertEquals(only_comment, comment)
