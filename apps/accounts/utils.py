def avatar_path(instance, filename):
    phone = instance.phone
    return 'avatars/{0}/{1}'.format(phone, filename)