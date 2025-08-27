class Task:
    
    def __init__(self, id, title, description, completed = False ) -> None:
        self.id = id
        self.title = title 
        self.description = description
        self.completed = completed

    # retornar o objeto em formato de dicionario
    def to_disc(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "completed" : self.completed
        }
    
