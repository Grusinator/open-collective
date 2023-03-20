def save_profile_picture(strategy, details, response, user=None, *args, **kwargs):
    url = response.get("picture", None)
    if url and user:
        user.google_profile_picture = url
        user.save()
