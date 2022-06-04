import src.views

routes = [
    ('GET', '/scan/{ip}/{start}/{end}', src.views.ports_scanner),
]
