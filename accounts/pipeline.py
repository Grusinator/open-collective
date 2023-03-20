def save_google_info(strategy, details, response, user=None, *args, **kwargs):
    profile_picture_url = response.get("picture", None)
    if profile_picture_url and user:
        user.google_profile_picture = profile_picture_url
        user.save()
    refresh_token = kwargs.get('response', {}).get('refresh_token')
    if refresh_token:
        user.google_refresh_token = refresh_token
        user.save()
