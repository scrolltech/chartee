import be.app.libs.chart as chartlib


def setup_routes(factory):
    factory.urls_prefix = '/api/1.0/'
    chart_handlers = (chartlib.list_, chartlib.create_and_publish, None, chartlib.get, chartlib.update_and_publish, chartlib.destroy)
    factory.map_resource('chart/', handlers=chart_handlers)
    factory.get('/api/1.0/chart/{id}/unpublish')(chartlib.unpublish)
