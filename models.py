from app import db

class urls(db.Model):
    __tablename__ = "urls"

    code = db.Column(db.String(), primary_key=True)
    url = db.Column(db.String())

    def __init__(self, code, url) -> None:
        self.code = code
        self.url = url

    def __repr__(self) -> str:
        return "<code: {}>".format(self.code)