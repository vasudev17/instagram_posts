from instapy_cli import client

username = 'vasudev_mehra'
password = 'AbbuVasu123*'
image = 'posts/post1.png'
text = 'Tester'

with client(username,password) as cli:
    cli.upload(image, text)
