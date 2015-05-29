import web

urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())
render = web.template.render('./')

class index:
    def GET(self, phone):
        if not phone: phone="*%2306%23"
        return render.index(phone)

if __name__ == "__main__":
    app.run()
