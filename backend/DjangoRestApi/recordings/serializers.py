from rest_framework import serializers 
from questions.models import Question
 
 
class QuestionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Question
        fields = ('id',
                'exam_id',
                'question_id',
                'user_id',
                'device',
                'recording_start_time',
                'recording_end_time',
                'filename',
                'final_submission',
                'created_at',
                'last_modified_at')
