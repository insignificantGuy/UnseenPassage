import transformers

from transformers import pipeline


def solve(question, passage):

    ups = pipeline('question-answering',model="deepset/roberta-base-squad2")
    answer = ups(question= question, context = passage )
    
    return answer