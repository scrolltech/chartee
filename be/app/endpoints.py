import be.app.libs.chart as chartlib


def setup_routes(factory):
	chart_handlers = (chartlib.list_, chartlib.create, None, chartlib.get_or_none, chartlib.update, chartlib.delete)
	factory.map_resource('/chart/', handlers=chart_handlers)
