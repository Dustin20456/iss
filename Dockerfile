FROM python:3.9

WORKDIR /iss
COPY ./ /iss
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["iss.py"]
