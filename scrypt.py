import urllib.request
import cgi

i = 0
img_type = 'post'
result=''
form = cgi.FieldStorage()
url = str(form.getlist('url'))
url = url.replace("']",'')
url = url.replace("['",'')
url = url.replace('m.','')
url = url.replace('https','http')
url = url.replace(' ','')
if url[0:14] == 'http://vk.com/':
	print(1)
	htmlcode = str(urllib.request.urlopen(url).read())
	if 'comment' in htmlcode:
		start_comments_index = htmlcode.find('comment')
	while 'data-src_big="' in htmlcode:
		start_img_url_index = htmlcode.find('data-src_big="')
		if start_comments_index < start_img_url_index and 'comment' in htmlcode:
			img_type = 'comment'
		url_img = htmlcode[start_img_url_index + 14:start_img_url_index + 77]
		url_img = url_img.replace('https','http')
		print(url_img + '1')
		img = urllib.request.urlopen(url_img).read()
		htmlcode = (htmlcode.replace('data-src_big="','',1))
		i += 1
		if img_type='post':
			images_from_post += "<img src='{}'>".format(url_img)
		else:
			images_from_comments += "<img src='{}'>".format(url_img)
else:
	result = '<p>Некоректная ссылка</p>'
if images_from_post=='':
	images_from_post='<p>Нет картинок</p>'
if images_from_comment=='':
	images_from_comment='<p>Нет картинок</p>'
print('''Content-type: text/html\n
<!DOCTYPE html>
<html lang='ru'>\n
	<head>\n
		<meta charset='utf-8'>\n
		<link rel='stylesheet' href='styles.css'>\n
		<link rel='stylesheet' type='text/css' href='https://fonts.googleapis.com/css?family=Open+Sans:400italic,400,600'>\n
		<title>Скачать картинку из ВК на андроид</title>\n
	</head>
	<body>\n
		<h1>Из поста:</h1>\n
		{0}\n
		<h1>Из комментариев:</h1>\n
		{1}\n
	</body>'''.format(images_from_post,images_from_comment))