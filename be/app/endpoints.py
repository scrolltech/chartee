import be.app.libs.chart as chartlib


def setup_routes(factory):
    factory.post('/chart/<int:id>/create')(chartlib.create)
    factory.get('/chart/<int:id>')(chartlib.get)
    factory.patch('/chart/<int:id>/update')(chartlib.update)
    factory.delete('/chart/<int:id>/delete')(chartlib.destroy)
