import os
from jinja2 import Environment, FileSystemLoader


class Reporter:
    def __init__(self, context=None):
        self.context = context
        self.features = context._runner.features if context else []
        if context:
            self.base_dir = os.path.dirname(os.path.abspath(__file__))
            self.templates_dir = os.path.join(self.base_dir, 'templates')
            self.env = Environment(loader=FileSystemLoader(self.templates_dir))
            self.template = self.env.get_template('report.html')
            self.output_path = os.path.join(os.getcwd(), 'reports')
            os.makedirs(self.output_path, exist_ok=True)
            self.output_report()

    def output_report(self):
        filename = os.path.join(self.output_path, 'index.html')
        with open(filename, 'w') as fh:
            fh.write(
                self.template.render(
                    features=self.features
                )
            )
