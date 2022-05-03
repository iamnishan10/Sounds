from rest_framework import serializers 
from questions.models import Question
 
 
class QuestionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Question
        fields = ('id',
                'user_id',
                'full_name',
                'd_o_b'
                'nationality',
                'native_language',
                'country',
                'gender',
                'kor_lang_proficiency',
                'study_period',
                'stay_period_kor',
                'study_purpose',
                'study_method',
                'self_assessment_level',
                'topik_level',
                'score',
                'organization'
                'created_at',
                'last_modified_at')