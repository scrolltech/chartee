import be.app.libs.chart as chartlib


def setup_routes(factory):
	chart_handlers = (chartlib.list_, chartlib.create_and_publish, None, chartlib.get, chartlib.update_and_publish, chartlib.destroy)
	factory.map_resource('/chart/', handlers=chart_handlers)
	factory.get('/chart/<int:id>/unpublish')(chart_handlers.unpublish)
