STATIC_URL = '/static/' #追加
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
 #画像などのメディアファイルがある場合
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
