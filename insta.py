from instagrapi import Client
import random



with open ("file.txt", "r") as f:
    username, password =f.read().splitlines()

client= Client()
client.login(username, password)

hashtag="programming"
comments=["Great job!","Well done!","Thanks!"]
medias = client.hashtag_medias_recent(hashtag,20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"beğenilen post numarası {i+1} of hashtag {hashtag}")
    if i%5==0:
        client.user_follow(media.user.pk)
        print(f"takip edilen kullanıcı{media.user.username}")
        client.media_comment(media.id,"Nice")
        comment=random.choice(comments)
        print(f"yorum yapıldı{comment} post numarası={i+1}")