import instaloader


L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, "imigrasi_cilegon")
posts = profile.get_posts()
i = 1
for post in posts:
  if i == 13 :
    break
  L.download_post(post, "imigrasi_cilegon")
  i += 1