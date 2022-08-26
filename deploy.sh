gunicorn --daemon -w 4 -b 127.0.0.1:5001 HengBlog.wsgi --error-logfile ./log/error.log --access-logfile ./log/access.log # django
# 查看error.log kill掉主进程就可以了