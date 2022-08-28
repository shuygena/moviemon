class Moviemon:
    def __init__(self,
                 title="Pokémon",
                 year=1997,
                 director="multiple",
                 poster="not yet available",
                 rating=7.5,
                 type="series",
                 plot="full",
                 actors="Veronica Taylor, Rachael Lillis, Eric Stuart"):
        self.title = title
        self.year = year
        self.director = director
        self.poster = poster
        self.rating = rating
        self.type = type
        self.plot = plot
        self.actors = actors

    def __str__(self):
        return str({
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "poster": self.poster,
            "rating": self.rating,
            "type": self.type,
            "plot": self.plot,
            "actors": self.actors,
        })
