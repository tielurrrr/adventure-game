FROM python:3.9-slim

ADD main.py .
ADD character.py .
ADD chapter_one.py .
ADD chapter_two.py .
ADD chapter_three.py .
ADD chapter_four.py .
ADD chapter_five.py .
ADD chapter_six.py .
ADD chapter_seven.py .
ADD chapter_eight.py .
ADD chapter_nine.py .
ADD chapter_ten.py .
ADD chapter_eleven.py .
ADD chapter_twelve.py .



CMD ["python", "main.py"]
