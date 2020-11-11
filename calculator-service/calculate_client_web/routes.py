def setup_routes(app, handler, project_root):
    router = app.router
    h = handler
    router.add_get("/", h.index, name="index")
    router.add_post("/calculate_string", h.calculate_string, name="calculate_string")
    router.add_static("/static/", path=str(project_root / "static"), name="static")
