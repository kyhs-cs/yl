urls = ['https://www.youtube.com/watch?v=FepDt4KniyQ', 'https://www.youtube.com/watch?v=vsB5iKhFx4g', 'https://example.com', 'https://www.youtube.com/watch?v=9ZGfH0R_tb4', 'https://www.youtube.com/watch?v=Z4vtJTQQojw', 'https://www.youtube.com/watch?v=-bdgTfu-ry4']

for i in range(len(urls)):
    file = open(f'{i}.html', 'w')
    content = f"""<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0; URL={urls[i]}">
  <meta charset="UTF-8">
  <title>Redirecting...</title>
</head>
<body>
  <p>If you are not redirected, <a href="{urls[i]}">click here</a>.</p>
</body>
</html>
"""
    file.write(content)
    file.close()