FROM python:3.9 AS builder
RUN python3.9 -m pip install build --user
COPY /pyproject.toml /tmp/build/pyproject.toml
COPY /setup.py /tmp/build/setup.py
COPY /src /tmp/build/src
WORKDIR /tmp/build
RUN python -m build --sdist --wheel --outdir dist/ .

FROM python:3.9
COPY --from=builder /tmp/build/dist/ssd1306-boot-ip-*.tar.gz /tmp/ssd1306-boot-ip.tar.gz
RUN pip install /tmp/ssd1306-boot-ip.tar.gz && rm /tmp/ssd1306-boot-ip.tar.gz
ENTRYPOINT ["show-ssd1306-boot-ip"]
