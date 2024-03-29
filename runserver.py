from aiohttp import web
from site_ctrl import RunServ
import logging 
import settings

def main():

	print("Starting server...")
	
	app = RunServ(
		serve_static = settings.SERVE_STATIC, 
		serve_storage = settings.SERVE_STORAGE, 
		serve_js = settings.SERVE_JS
	)

	if settings.ENABLE_LOGGING:
		if settings.LOG_TO_FILE:
			logging.basicConfig (
				filename='log.txt',
				filemode='a',
				format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
				datefmt='%H:%M:%S',
				level=logging.DEBUG
			)
		else:
			logging.basicConfig(level=logging.DEBUG)
			
	web.run_app(app, port = settings.PORT)


if __name__ == '__main__':
	main()

