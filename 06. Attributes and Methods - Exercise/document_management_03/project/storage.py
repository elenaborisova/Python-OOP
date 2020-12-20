from document_management_03.project.category import Category
from document_management_03.project.document import Document
from document_management_03.project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list = []
        self.topics: list = []
        self.documents: list = []

    def find_category_by_id(self, category_id: int):
        return [c for c in self.categories if c.id == category_id][0]

    def find_topic_by_id(self, topic_id: int):
        return [t for t in self.topics if t.id == topic_id][0]

    def find_document_by_id(self, document_id: int):
        return [d for d in self.documents if d.id == document_id][0]

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.find_category_by_id(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_topic_by_id(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.find_document_by_id(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int):
        category = self.find_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self.find_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.find_document_by_id(document_id)
        self.documents.remove(document)

    def get_document(self, document_id: int):
        return self.find_document_by_id(document_id)

    def __repr__(self):
        return "\n".join(str(doc) for doc in self.documents)


c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finalize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)