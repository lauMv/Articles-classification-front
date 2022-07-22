
class Article:

    def __init__(self, id, source_file_path, pre_processed_file_path, filename, extraction_date, paper,
                 user_classification, model_classification, article_content, used_in_classifier):
        self.id = id
        self.source_file_path = source_file_path
        self.pre_processed_file_path = pre_processed_file_path
        self.filename = filename
        self.extraction_date = extraction_date
        self.paper = paper
        self.user_classification = user_classification
        self.model_classification = model_classification
        self.article_content = article_content
        self.used_in_classifier = used_in_classifier


