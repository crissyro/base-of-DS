FROM jupyter/minimal-notebook:latest

WORKDIR /home/jupyter

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY notebooks/ /home/jupyter/
COPY python/ /home/jupyter/
COPY misc/ /home/jupyter/

CMD [ "start-notebook.sh" ]

# Команды для запуска
# docker build -t my-jupyter .
# docker run -p 8888:8888 -v $(pwd):/home/jupyter my-jupyter
