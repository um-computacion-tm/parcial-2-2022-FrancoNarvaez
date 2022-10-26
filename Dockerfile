FROM python:3
RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-FrancoNarvaez.git
WORKDIR /4-in-line
RUN pip install -r requirements.txt
CMD ["python3",  "-m", "unittest"]
