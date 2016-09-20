from import_export import resources
from models import Questions
from import_export.admin import ImportExportModelAdmin


class QuestionResource(resources.ModelResource):

    class Meta:
        model = Questions
        fields = ('question', 'option_1', 'option_2','option_3','option_4','answer')


class QuestionsAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource
