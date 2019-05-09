import be.app.libs.data as datalib


def setup_routes(factory):
	data_handlers = (datalib.list_, datalib.create, None, datalib.get, datalib.update, datalib.destroy)
	factory.map_resource('/chart/', handlers=data_handlers)
