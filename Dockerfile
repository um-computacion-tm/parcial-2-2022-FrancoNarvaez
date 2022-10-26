FROM python:3
RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-FrancoNarvaez.git
WORKDIR /parcial-2-2022-FrancoNarvaez
CMD ["python3",  "-m", "unittest"]
