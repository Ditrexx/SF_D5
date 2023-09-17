# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# exec(open('script.py').read())
from newapp.models import *

# 1. Создать двух пользователей (с помощью метода User.objects.create_user).
user1 = User.objects.create(username='Ivan', first_name='Navi')
user2 = User.objects.create(username='Jack', first_name='Kcaj')
# 2. Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(authorUser=user1)
Author.objects.create(authorUser=user2)
# 3. Добавить 4 категории в модель Category.
Category.objects.create(name='IT')
Category.objects.create(name='Education')
Category.objects.create(name='Politics')
Category.objects.create(name='Technology')
# 4. Добавить 2 статьи и 1 новость.
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Ivan')), categoryType='NW',
                    title='News 1', text='This is a news.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Ivan')), categoryType='AR',
                    title='Article 1', text='This is an article.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Jack')), categoryType='NW',
                    title='News 2', text='This is different news.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Jack')), categoryType='AR',
                    title='Article 2', text='This is another article.')
# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# Получаем обьекты статей
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
p4 = Post.objects.get(pk=4)
# Получаем объекты категорий
c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Education')
c3 = Category.objects.get(name='Politics')
c4 = Category.objects.get(name='Technology')
# Добавляем категории к статьям
p1.postCategory.add(c1)
p2.postCategory.add(c1, c2, c3, c4)
p3.postCategory.add(c3, c2)
p4.postCategory.add(c4)
# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(commentUser=User.objects.get(username='Ivan'), commentPost=Post.objects.get(pk=1),
                       text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='Jack'), commentPost=Post.objects.get(pk=1),
                       text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='Ivan'), commentPost=Post.objects.get(pk=2),
                       text='comment text2')
Comment.objects.create(commentUser=User.objects.get(username='Jack'), commentPost=Post.objects.get(pk=3),
                       text='comment text2')
Comment.objects.create(commentUser=User.objects.get(username='Jack'), commentPost=Post.objects.get(pk=4),
                       text='comment text3')
# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=1).dislike()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=3).dislike()
# 8. Обновить рейтинги пользователей.
Author.objects.get(authorUser=User.objects.get(username='Ivan')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Jack')).update_rating()
# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
bestAuthor = Author.objects.order_by('-ratingAuthor').first()
print(f'Имя пользователя: {bestAuthor.authorUser.username}, Рейтинг: {bestAuthor.ratingAuthor}')
# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
#bestPost = Post.objects.all().order_by('-rating').values('dateCreation', 'author', 'rating', 'title', )[0]
bestPost = Post.objects.all().order_by('-rating').first()
print(f'Дата добавления: {bestPost.dateCreation}\n'
      f'username автора: {bestPost.author.authorUser.username}\n'
      f'рейтинг: {bestPost.rating}\n'
      f'заголовок и превью лучшей статьи: {bestPost.title}')
# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
comments = Comment.objects.filter(commentPost=bestPost)
comments.values('dateCreation', 'commentUser', 'rating', 'text')
for comment in comments:
    print(f'Дата: {comment.dateCreation}\n'
          f'пользователь: {comment.commentUser.username}\n'
          f'рейтинг: {comment.rating}\n'
          f'текст: {comment.text}\n')
    print('=' * 10 + '\n')
